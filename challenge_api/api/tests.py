import pytest
from datetime import datetime
from decimal import Decimal
from api.models import CNAB, Transacao
from rest_framework.test import APIClient

transacao_obj = {'tipo': 2, 'descricao': 'Boleto', 'natureza': 'Saída', 'sinal': '-'}


@pytest.mark.django_db
def test_create_transacao():
    t = Transacao.objects.create(**transacao_obj)
    assert t.tipo == 2
    assert t.descricao == 'Boleto'
    assert t.natureza == 'Saída'
    assert t.sinal == '-'


@pytest.mark.django_db
def test_create_cnab():
    dado = "2201903010000000500232702980567677****8778141808JOSÉ COSTA    MERCEARIA 3 IRMÃOS"
    t = Transacao.objects.create(**transacao_obj)
    cnab = CNAB.objects.create(
        tipo_id=t.id,
        data=datetime.strptime(dado[1:9], '%Y%m%d'),
        valor=Decimal(dado[9:19]) / Decimal(100.00),
        cpf=dado[19:30],
        cartao=dado[30:42],
        hora=f"{dado[42:44]}:{dado[44:46]}:{dado[46:48]}",
        dono_loja=dado[48:62],
        nome_loja=dado[62:81].strip()
    )

    assert cnab.nome_loja == 'MERCEARIA 3 IRMÃOS'
    assert cnab.tipo_id == t.id
    assert cnab.data.__str__() == '2019-03-01 00:00:00'
    assert cnab.valor == Decimal(5)
    assert cnab.cpf == '23270298056'
    assert cnab.cartao == '7677****8778'
    assert cnab.hora == '14:18:08'
    assert cnab.dono_loja.strip() == 'JOSÉ COSTA'
    assert cnab.nome_loja == 'MERCEARIA 3 IRMÃOS'


@pytest.mark.django_db
def test_busca_cnab_loja_api():
    t = Transacao.objects.create(**transacao_obj)
    CNAB.objects.create(tipo_id=t.id, data=datetime.strptime('20190301', '%Y%m%d'), valor=Decimal(5),
                        cpf='23270298056', cartao='7677****8778', hora='14:18:08', dono_loja='JOSÉ COSTA',
                        nome_loja='MERCEARIA 3 IRMÃOS')

    client = APIClient()
    request = client.get('/cnab/?loja=MERCEARIA 3 IRMÃOS', format='json')
    assert request.json()['results'][0]['cartao'] == '7677****8778'
    assert request.json()['results'][0]['cpf'] == '23270298056'
    assert request.json()['results'][0]['valor'] == '5.00'
    assert request.json()['results'][0]['hora'] == '14:18:08'
    assert request.json()['results'][0]['dono_loja'] == 'JOSÉ COSTA'
    assert request.json()['results'][0]['nome_loja'] == 'MERCEARIA 3 IRMÃOS'
    assert request.json()['saldo'] == '-5.00'


@pytest.mark.django_db
def test_busca_cnab_lojas_disponiveis():
    t = Transacao.objects.create(**transacao_obj)
    CNAB.objects.create(tipo_id=t.id, data=datetime.strptime('20190301', '%Y%m%d'), valor=Decimal(30),
                        cpf='23270298056', cartao='7677****8778', hora='14:18:08', dono_loja='JOSÉ COSTA',
                        nome_loja='MERCEARIA 3 IRMÃOS')
    CNAB.objects.create(tipo_id=t.id, data=datetime.strptime('20190301', '%Y%m%d'), valor=Decimal(5),
                        cpf='23270298056', cartao='7677****8778', hora='14:18:08', dono_loja='JOSÉ COSTA',
                        nome_loja='MERCADO DA AVENIDA')

    client = APIClient()
    request = client.get('/cnab/?loja=all', format='json')
    assert {'nome_loja': 'MERCEARIA 3 IRMÃOS'} in request.json()['results']
    assert {'nome_loja': 'MERCADO DA AVENIDA'} in request.json()['results']
    assert len(request.json()['results']) == 2


@pytest.mark.django_db
def test_busca_cnab_saldo():
    transacao_obj_1 = {'tipo': 1, 'descricao': 'Debito', 'natureza': 'Entrada', 'sinal': '+'}
    transacao_obj_2 = {'tipo': 2, 'descricao': 'Boleto', 'natureza': 'Saída', 'sinal': '-'}
    t_1 = Transacao.objects.create(**transacao_obj_1)
    t_2 = Transacao.objects.create(**transacao_obj_2)
    CNAB.objects.create(tipo_id=t_1.id, data=datetime.strptime('20190301', '%Y%m%d'), valor=Decimal(30),
                        cpf='23270298056', cartao='7677****8778', hora='14:18:08', dono_loja='JOSÉ COSTA',
                        nome_loja='MERCEARIA 3 IRMÃOS')
    CNAB.objects.create(tipo_id=t_2.id, data=datetime.strptime('20190301', '%Y%m%d'), valor=Decimal(5),
                        cpf='23270298056', cartao='7677****8778', hora='14:18:08', dono_loja='JOSÉ COSTA',
                        nome_loja='MERCEARIA 3 IRMÃOS')

    client = APIClient()
    request = client.get('/cnab/?loja=MERCEARIA 3 IRMÃOS', format='json')
    assert request.json()['saldo'] == '25.00'
