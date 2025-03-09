from fpdf import FPDF
import random
import matplotlib.pyplot as plt
import numpy as np

# Function to generate a chart
def generate_chart(filename):
    x = np.arange(1, 11)
    y = np.random.randint(10, 100, 10)
    plt.figure(figsize=(6, 3))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title('Grafik Kinerja')
    plt.xlabel('Bulan')
    plt.ylabel('Efisiensi (%)')
    plt.grid(True)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

# PDF Class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", style='B', size=12)
        self.cell(0, 10, "Dokumentasi Produk Robot X-2000", ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", size=8)
        self.cell(0, 10, f'Halaman {self.page_no()}', align='C')

    def chapter_title(self, title):
        self.set_font("Arial", style='B', size=14)
        self.cell(0, 10, title, ln=True, align='L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font("Arial", size=11)
        self.multi_cell(0, 10, body)
        self.ln()

# Generate mock text
def generate_text(paragraphs=5):
    text = """Robot X-2000 adalah perangkat otomatisasi canggih yang dirancang untuk meningkatkan efisiensi di sektor industri. 
Dengan teknologi sensor AI dan algoritma pembelajaran mesin, perangkat ini mampu mendeteksi, menganalisis, dan merespons berbagai situasi kerja."""
    return "\n\n".join([text] * paragraphs)

# Sections to be included in the PDF
document_sections = [
    ("Bab 1: Pengenalan", 3),
    ("Bab 2: Deskripsi Produk", 5),
    ("Bab 3: Spesifikasi Teknis", 5),
    ("Bab 4: Panduan Instalasi", 6),
    ("Bab 5: Panduan Penggunaan", 10),
    ("Bab 6: Prosedur Pemeliharaan", 6),
    ("Bab 7: Panduan Troubleshooting", 6),
    ("Bab 8: Diagram Arsitektur Sistem", 3),
    ("Bab 9: Grafik Kinerja", 3),
    ("Bab 10: Panduan Keselamatan", 5),
    ("Lampiran & Glosarium", 4),
]

# Generate PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

for title, paragraphs in document_sections:
    pdf.add_page()
    pdf.chapter_title(title)
    pdf.chapter_body(generate_text(paragraphs))
    
    # Insert charts for relevant sections
    if "Grafik" in title:
        chart_filename = "chart.png"
        generate_chart(chart_filename)
        pdf.image(chart_filename, x=10, y=pdf.get_y(), w=180)
        pdf.ln(80)

# Save PDF
pdf.output("Synthetic_Documentation_Robot_X2000.pdf")

