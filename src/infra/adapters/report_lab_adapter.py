from io import BytesIO
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from src.application.contracts.export_registration_pdf_exporter import ExportRegistrationPdfExporter
from src.domain.entities.registration import Registration


class ReportLabAdapter(ExportRegistrationPdfExporter):
    def __init__(self) -> None:
        self.__bytes_io = BytesIO
        self.__letter = letter
        self.__inch = inch
        self.__simple_doc_template = SimpleDocTemplate
        self.__paragraph = Paragraph
        self.__get_sample_style_sheet = getSampleStyleSheet

    
    def generate(self, registration: Registration) -> bytes:
        # Criar um buffer de bytes para armazenar o PDF
        buffer = self.__bytes_io()
        
        # Configurações da folha PDF
        pdf_options = {
            'topMargin': 0.75 * self.__inch,
            'rightMargin': 0.75 * self.__inch,
            'bottomMargin': 0.75 * self.__inch,
            'leftMargin': 0.75 * self.__inch,
            'encoding': 'utf-8',
        }

        # Conteúdo html a ser convertido para PDF
        html_content = f"""
        <p>Nome: {registration.get_name}</p>
        <p>CPF: {registration.get_registration_number}</p>
        <p>E-mail: {registration.get_email}</p>
        <p>Data de nascimento: {registration.get_birth_date}</p>
        <p>Data de registro: {registration.get_registration_at}</p>
        """
        try:
            # Criar o documento PDF
            doc = self.__simple_doc_template(buffer, pagesize=self.__letter, **pdf_options)

            # Configurar o estilo do parágrafo
            styles = self.__get_sample_style_sheet()
            style = styles["Normal"]

            # Converter o HTML em parágrafos do ReportLab
            content = []
            for line in html_content.split('\n'):
                content.append(self.__paragraph(line.strip(), style))

            # Adicionar os parágrafos ao documento
            doc.build(content)
            return buffer.getvalue()
        except Exception as e:
            raise e
