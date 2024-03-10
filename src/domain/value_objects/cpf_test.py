from .cpf import Cpf


def test_cpf():
    try:
        cpf = Cpf('0')
    except Exception as ex:
        assert str(ex) == 'Cpf inválido!!!'
