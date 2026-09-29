import pytest
from funcoes import (
    aplicar_desconto,
    calcular_frete,
    calcular_media,
    classificar_imc,
    sacar,
    senha_valida,
)


def test_classificar_imc_abaixo_do_peso():
    assert classificar_imc(18.4) == "Abaixo do peso"


def test_classificar_imc_peso_normal():
    assert classificar_imc(22.0) == "Peso normal"


def test_classificar_imc_acima_do_peso():
    assert classificar_imc(25.1) == "Acima do peso"


def test_classificar_imc_fronteira_25():
    assert classificar_imc(25.0) == "Acima do peso"


def test_sacar_valido():
    assert sacar(100, 40) == 60


def test_sacar_invalido():
    with pytest.raises(ValueError, match="Saldo insuficiente"):
        sacar(50, 100)


def test_calcular_frete_ate_5kg():
    assert calcular_frete(5) == 10.0


def test_calcular_frete_entre_5_e_10kg():
    assert calcular_frete(8) == 20.0


def test_calcular_frete_acima_10kg():
    assert calcular_frete(15) == 35.0


def test_calcular_frete_fronteira_5():
    assert calcular_frete(5) == 10.0


def test_calcular_frete_fronteira_10():
    assert calcular_frete(10) == 20.0


def test_senha_valida():
    assert senha_valida("senha123") is True


def test_senha_curta_demais():
    assert senha_valida("abc1") is False


def test_senha_sem_numero():
    assert senha_valida("senhasegura") is False


def test_senha_exatamente_8_caracteres():
    assert senha_valida("abc12345") is True


def test_aplicar_desconto_valido():
    assert aplicar_desconto(100, 20) == 80.0


def test_aplicar_desconto_zero_porcento():
    assert aplicar_desconto(100, 0) == 100.0


def test_aplicar_desconto_cem_porcento():
    assert aplicar_desconto(100, 100) == 0.0


def test_aplicar_desconto_invalido():
    with pytest.raises(ValueError, match="Desconto inválido"):
        aplicar_desconto(100, -10)


def test_calcular_media_notas_diferentes():
    assert calcular_media([8, 9, 10]) == 9.0


def test_calcular_media_notas_iguais():
    assert calcular_media([7, 7, 7]) == 7.0


def test_calcular_media_uma_nota():
    assert calcular_media([9]) == 9.0


def test_calcular_media_lista_vazia():
    with pytest.raises(ValueError, match="Lista de notas vazia"):
        calcular_media([])