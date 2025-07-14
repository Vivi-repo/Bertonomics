from fpdf import FPDF  # type: ignore
import csv

def export_to_pdf(data, filename="sentiment_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in data:
        pdf.cell(200, 10, txt=line, ln=True)
    pdf.output(filename)

def export_to_csv(data, filename="sentiment_report.csv"):
    with open(filename, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for line in data:
            writer.writerow([line])


