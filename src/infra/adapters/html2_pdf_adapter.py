import pdfkit
from src.application.contracts.export_registration_pdf_exporter import ExportRegistrationPdfExporter
from src.domain.entities.registration import Registration


class Html2PdfAdapter(ExportRegistrationPdfExporter):

    def __init__(self) -> None:
        self.__html2pdf = pdfkit

    def generate(self,
                 registration: Registration
                 ) -> str:
        html_content = f"""
        <p>Nome: {registration.get_name}</p>
        <p>CPF: {registration.get_registration_number}</p>
        """
        pdf_options = {
            'path': r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe',
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': 'UTF-8',
            'no-outline': None,
            '--font-family': 'Arial',
            }
        try:
            # Converter HTML para PDF
            pdf=self.__html2pdf.from_string(
                input=html_content,
                options=pdf_options,
                output_path='output.pdf'
                )
            # Ler o conteúdo do PDF convertido
            # with open('output.pdf', 'rb') as f:
                # pdf_content= f.read()

            return pdf
            # return pdf_content.decode('utf-8')  # Retorna o conteúdo do PDF como uma string
        except Exception as e:
            # Formatar a mensagem de exceção e retornar
            # formatter = ExceptionFormatter(e)
            # return formatter.get_html_message()
            raise e
