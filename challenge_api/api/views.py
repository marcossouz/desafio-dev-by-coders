from django.http import JsonResponse
from django.db.utils import IntegrityError
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
    def get(self, request):
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

    def post(self, request, format=None):
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
    def get(self, request):
        results = list(Transacao.objects.all().values())
        return JsonResponse({'results': results})
