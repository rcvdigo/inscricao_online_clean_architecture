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
        <p>E-mail: {registration.get_email}</p>
        <p>Data de nascimento: {registration.get_birth_date}</p>
        <p>Data de registro: {registration.get_registration_at}</p>
        """
        wkhtml_path = self.__html2pdf.configuration(
            wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
            )
        pdf_options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': 'UTF-8',
            'no-outline': None,
            }
        try:
            # Converter HTML para PDF
            pdf_content = self.__html2pdf.from_string(
                input=html_content, # Conteudo a ser convertido em PDF
                configuration=wkhtml_path, # Indicando o local de arquivo do gerador de PDF
                options=pdf_options, # Aplicar as configurações da folha no PDF
                # output_path='public/output.pdf', # Linha que faz gerar o arquivo PDF
                cover_first=False # Não gerar capa
                ).decode('latin-1').encode('utf-8').decode('utf-8')
            
            return pdf_content # Retorna o conteúdo do PDF como uma bytes
        except Exception as e:
            raise e
