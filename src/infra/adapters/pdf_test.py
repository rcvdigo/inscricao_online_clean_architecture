from src.domain.entities.registration import Registration
from .html2_pdf_adapter import Html2PdfAdapter


class MockRegistration(Registration):
    pass


def test():
    pdf = Html2PdfAdapter()
    a = MockRegistration(name='Ana Silva',
                         email='ana@example.com',
                         birth_date='1990-05-15',
                         registration_number='12345678901',
                         registration_at='2024-03-12 17:34:46')
    print()
    print(a.get_birth_date)
    print(a.get_registration_at)

    pdf.generate(registration=a)
