import os

from qgis.PyQt.QtGui import QTextDocument, QPageSize
from qgis.PyQt.QtPrintSupport import QPrinter
from qgis.PyQt.QtCore import QSizeF

from adapted_docx import Document
from adapted_docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK

from ..models.user_settings import UserSettings

def save_as_pdf(heading, body, architect_identification, new_file_path, caminho_logo1='', caminho_logo2=''):

    user_settings = UserSettings()
    atc_logo_path = user_settings.atc_logo_path
    main_logo_path = user_settings.main_logo_path

    document = QTextDocument()

    document.setDocumentMargin(5)

    # Configuração da impressora
    printer = QPrinter(QPrinter.HighResolution)
    printer.setPageSize(QPageSize(QPageSize.A4))
    printer.setPageMargins(20,10,20,10, QPrinter.Millimeter)

    page_rect = printer.pageRect(QPrinter.Point)

    document.setPageSize(
        QSizeF(
            page_rect.width(),
            page_rect.height()
        )
    )

    print("paperRect:", printer.paperRect(QPrinter.Millimeter))
    print("pageRect:", printer.pageRect(QPrinter.Millimeter))


    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(new_file_path)

    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">

        <style>
                    body {{
                        font-family: Arial;
                        font-size: 8pt;
                        margin: 0;
                    }}
        
                    /* =========================
                    RESTANTE DO DOCUMENTO
                    ========================= */
        
                    .titulo {{
                        margin-top: 40px;
                        text-align: center;
                        font-size: 13pt;
                        font-weight: bold;
                    }}
        
                    .paragrafo {{
                        margin-top: 25px;
                        text-align: justify;
                    }}
        
                    .identificacao {{
                        margin-top: 60px;
                        font-size: 8pt;
                        text-align: right;
                    }}
                </style>
    </head>

    <body>

        <!-- CABEÇALHO -->

        <table
            cellspacing="0"
            cellpadding="0"
            border="0"
            width="100%"
        >
            <tr>

                <td
                    width="33.33%" 
                    style="
                        text-align: center; 
                        vertical-align: bottom;
                    "
                >
                    <img
                        src="{atc_logo_path}"
                        width="140"
                        height="50"
                    >
                </td>

                <td
                    width="33.33%" 
                    style="
                        text-align: center; 
                        vertical-align: center;
                    "
                >
                    <img
                        src="{main_logo_path}"
                        width="80"
                        height="80"
                    >
                </td>

                <td
                    width="33.33%" 
                    style="
                        text-align: right; 
                        vertical-align: bottom;
                    "
                >
                    <div class="texto-cabecalho" style="font-size: 5pt; line-height: 0.5;" >
                        Prefeitura Municipal de Curitiba<br>
                        <br>
                        Companhia de Habitação<br>
                        Popular de Curitiba<br>
                        <br>
                        Rua Barão do Rio Branco, 45<br>
                        80010-180  Centro   Curitiba  PR<br>
                        secretariageralcohab@curitiba.pr.gov.br<br>
                        Tel.: 41 3221-8133 <br>
                        www.cohabct.com.br<br>
                    </div>
                </td>

            </tr>
        </table>

        <!-- TÍTULO -->
        <div class="titulo">
            {heading}
        </div>


        <!-- PARÁGRAFO -->
        <div class="paragrafo">
            {body}
        </div>


        <!-- IDENTIFICAÇÃO FINAL -->
        <div class="identificacao">
            {architect_identification}
        </div>

    </body>
    </html>
    """

    document.setHtml(html)
    # Gera o PDF
    document.print_(printer)

def save_as_docx(heading, body, architect_identification, new_file_path, template_path):
    document = Document(template_path)

    doc_heading = document.add_paragraph(heading)
    doc_heading.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc_heading.runs[-1].add_break(WD_BREAK.LINE)
    doc_heading.runs[-1].add_break(WD_BREAK.LINE)

    doc_body = document.add_paragraph(body)
    doc_body.runs[-1].add_break(WD_BREAK.LINE)
    doc_body.runs[-1].add_break(WD_BREAK.LINE)

    doc_architect_id_paragraph = document.add_paragraph(architect_identification)

    doc_architect_id_paragraph.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    document.save(new_file_path)