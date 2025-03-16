import PyPDF2
import fitz  # PyMuPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def extract_text(pdf_path):
    """Extracts text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text

def merge_pdfs(pdf_list, output_path):
    """Merges multiple PDFs into one."""
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

def split_pdf(pdf_path, output_folder):
    """Splits a PDF into individual pages."""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(len(reader.pages)):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[i])
            with open(f"{output_folder}/page_{i+1}.pdf", "wb") as output:
                writer.write(output)

def add_watermark(input_pdf, watermark_text, output_pdf):
    """Adds a text watermark to all pages of a PDF."""
    reader = PyPDF2.PdfReader(input_pdf)
    writer = PyPDF2.PdfWriter()
    
    # Create watermark PDF
    watermark_pdf = "watermark.pdf"
    c = canvas.Canvas(watermark_pdf, pagesize=letter)
    c.setFont("Helvetica", 36)
    c.drawString(200, 500, watermark_text)
    c.save()
    
    watermark = PyPDF2.PdfReader(watermark_pdf).pages[0]
    
    for page in reader.pages:
        page.merge_page(watermark)
        writer.add_page(page)
    
    with open(output_pdf, "wb") as output:
        writer.write(output)

# Example Usage:
# text = extract_text("sample.pdf")
# merge_pdfs(["file1.pdf", "file2.pdf"], "merged.pdf")
# split_pdf("sample.pdf", "output_folder")
# add_watermark("sample.pdf", "CONFIDENTIAL", "watermarked.pdf") +
