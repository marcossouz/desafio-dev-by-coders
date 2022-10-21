from django.http import JsonResponse
from django.db.utils import IntegrityError
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import parsers
from rest_framework.views import APIView
from datetime import datetime
from decimal import Decimal
from contextlib import suppress

from .models import CNAB, Transacao


def calcula_saldo(results):
    saldo = 0
    for result in results:
        credito = [l['id'] for l in list(Transacao.objects.filter(sinal='+').values('id'))]
        if result['tipo_id'] in credito:
            saldo += result['valor']
        else:
            saldo -= result['valor']
    return saldo


class CNABView(APIView):
    parser_classes = (parsers.MultiPartParser,)
    loja = openapi.Parameter('loja', openapi.IN_QUERY,
                             description="lista de lojas / lista de transações por loja.",
                             type=openapi.TYPE_STRING)

    file = openapi.Parameter('file',
                             openapi.IN_FORM,
                             required=True,
                             description="Arquivo CNAB no format txt.",
                             type=openapi.TYPE_FILE)

    lojas_response = {
        "200": openapi.Response(
            description="Lista de lojas",
            examples={
                "parameter-all": {
                    "results": [
                        {"nome_loja": "MERCEARIA 3 IRMÃOS"},
                        {"nome_loja": "MERCADO DA AVENIDA"},
                        {"nome_loja": "BAR DO JOÃO"},
                        {"nome_loja": "LOJA DO Ó - FILIAL"},
                        {"nome_loja": "LOJA DO Ó - MATRIZ"}
                    ]
                },
                "parameter-nome_loja":
                    {
                        "results": [
                            {
                                "id": 216,
                                "tipo_id": 12,
                                "data": "2019-03-01",
                                "valor": "122.00",
                                "cpf": "84515254073",
                                "cartao": "6777****1313",
                                "hora": "17:27:12",
                                "dono_loja": "MARCOS PEREIRA",
                                "nome_loja": "MERCADO DA AVENIDA",
                                "transacao": {
                                    "id": 12,
                                    "tipo": 3,
                                    "descricao": "Financiamento",
                                    "natureza": "Saída",
                                    "sinal": "-"
                                }
                            }
                        ],
                        "saldo": "-122.00"
                    },
            }
        )}

    @swagger_auto_schema(manual_parameters=[loja], responses=lojas_response)
    def get(self, request):
        """
            Obter lojas ou transações

            Esse Endpoint irá filtrar as transações e efetuará o calculo do saldo para essa loja.
            Alternativamente, se passar o parametro "all" teremos como retorno a lista de
            lojas disponíveis para carregamento do filtro select.
        """
        if loja := request.GET.get('loja'):
            if loja == 'all':
                results = list(CNAB.objects.all().values('nome_loja').distinct())
                return JsonResponse({'results': results})
            else:
                results = list(CNAB.objects.filter(nome_loja=loja).values())

                for i, r in enumerate(results):
                    transacao = list(Transacao.objects.filter(id=r['tipo_id']).values())[0]
                    results[i].update({'transacao': transacao})

                return JsonResponse({'results': results, 'saldo': calcula_saldo(results)})
        results = list(CNAB.objects.all().values())
        return JsonResponse({'results': results, 'saldo': calcula_saldo(results)})

    @swagger_auto_schema(manual_parameters=[file])
    def post(self, request, format=None):
        """
            Enviar arquivo CNAB no formato txt

            Esse Endpoint tem a função de fazer upload do arquivo CNAB para alimentação do banco de dados
        """
        file = self.request.FILES['file']
        if request.data['file'].content_type != 'text/plain':
            return JsonResponse({'status': 400}, status=400)

        for line in file:
            dado = line.decode()

            try:
                t = Transacao.objects.get(tipo=dado[:1])
                with suppress(IntegrityError):
                    CNAB.objects.create(
                        tipo_id=t.id,
                        data=datetime.strptime(dado[1:9], '%Y%m%d'),
                        valor=Decimal(dado[9:19]) / Decimal(100.00),
                        cpf=dado[19:30],
                        cartao=dado[30:42],
                        hora=f"{dado[42:44]}:{dado[44:46]}:{dado[46:48]}",
                        dono_loja=dado[48:62],
                        nome_loja=dado[62:81].strip()
                    )
            except Transacao.DoesNotExist:
                pass

        return JsonResponse({'status': 'OK'})


class TransacaoView(APIView):
    transacao_response = {
        "200": openapi.Response(
            description="Lista de transacoes",
            examples={
                "results": [
                    {
                        "id": 10,
                        "tipo": 1,
                        "descricao": "Débito",
                        "natureza": "Entrada",
                        "sinal": "+"
                    },
                    {
                        "id": 11,
                        "tipo": 2,
                        "descricao": "Boleto",
                        "natureza": "Saída",
                        "sinal": "-"
                    }
                ]
            }
        )}

    @swagger_auto_schema(responses=transacao_response)
    def get(self, request):
        """
            Obter transações cadastradas no sistema

            Esse Endpoint retorna a lista de transações cadastradas no sistema
        """
        results = list(Transacao.objects.all().values())
        return JsonResponse({'results': results})
