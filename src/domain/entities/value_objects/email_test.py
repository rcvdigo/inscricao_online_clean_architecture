from .email import Email


def test_email():
    try:
        email = Email('email_errado')
    except Exception as ex:
        assert str(ex) == 'E-mail Inválido!'
