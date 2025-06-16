from fpdf import FPDF
import os

def save_as_pdf(content, filename, title):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, title, ln=True, align='C')
    pdf.ln(10)

    # Body
    pdf.set_font("Arial", size=12)
    for line in content.split('\n'):
        pdf.multi_cell(0, 10, line)

    output_path = f"{filename}.pdf"
    pdf.output(output_path)
    return output_path
