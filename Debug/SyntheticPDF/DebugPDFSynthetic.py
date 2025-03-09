from fpdf import FPDF
import random
import matplotlib.pyplot as plt
import numpy as np

# Function to generate a chart with dynamic titles
def generate_chart(filename, title):
    x = np.arange(1, 11)
    y = np.random.randint(10, 100, 10)
    plt.figure(figsize=(4, 2))  # Reduced chart size
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title(title)
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
        self.set_font("Times", size=12)
        self.multi_cell(0, 10, body, align='J')
        self.ln(5)  # Paragraph spacing of 1.5 lines

# Generate mock text with more variety
def generate_text(paragraphs=10):
    sentence_templates = [
        "Robot X-2000 adalah {} yang dirancang untuk {}.",
        "Dengan teknologi {} yang canggih, robot ini mampu {} secara {}.",
        "Dalam operasionalnya, Robot X-2000 menggunakan {} untuk {} dan {} secara real-time.",
        "Sistem {} yang ada pada robot ini memungkinkan {} dan {} dalam berbagai kondisi.",
        "Robot ini dilengkapi dengan {} yang dapat {} secara akurat di berbagai lingkungan.",
        "Fitur {} membantu robot ini untuk {} dengan {}.",
        "Desain {} memungkinkan robot ini untuk {} di berbagai industri.",
        "Melalui teknologi {}, robot ini dapat {} tanpa {}.",
        "Daya tahan robot ini sangat tinggi berkat {} dan {}.",
        "Robot ini dapat melakukan {} berkat {} yang terintegrasi dengan {}.",
    ]
    
    words = [
        ["perangkat otomatisasi canggih", "meningkatkan efisiensi di sektor industri"],
        ["AI", "analisis data", "optimasi produksi"],
        ["sensor canggih", "mendeteksi perubahan lingkungan"],
        ["modular", "diadaptasi", "aplikasi industri"],
        ["navigasi otonom", "bergerak", "intervensi manusia"],
        ["sistem pengendalian canggih", "mendeteksi kesalahan", "menangani tantangan"],
        ["energi terbarukan", "mengurangi ketergantungan pada sumber daya tidak terbarukan"],
        ["navigasi GPS", "menghindari rintangan", "memetakan rute optimal"],
        ["komputer terintegrasi", "memproses data secara real-time", "memberikan solusi otomatis"],
        ["material tahan lama", "bertahan dalam kondisi ekstrem"],
    ]
    
    # Generate random sections with more variety in the paragraph content
    paragraphs_list = []
    for _ in range(paragraphs):
        t = random.choice(sentence_templates)
        w = random.choice(words)
        num_placeholders = t.count("{}")
        chosen_words = w[:num_placeholders] if len(w) >= num_placeholders else w + random.choices(w, k=num_placeholders - len(w))
        paragraph = t.format(*chosen_words)
        
        # Add random additional elements (e.g., lists or quotes)
        if random.random() > 0.8:  # 20% chance to add a list
            paragraph += "\n\nFitur-fitur unggulan:\n"
            features = ["Akurasi tinggi dalam mendeteksi objek", "Kemampuan navigasi yang cepat", "Otomatisasi penuh dalam pengoperasian", "Pembaruan perangkat lunak yang berkelanjutan"]
            random.shuffle(features)
            for feature in features[:random.randint(2, 4)]:
                paragraph += f"- {feature}\n"

        if random.random() > 0.8:  # 20% chance to add a technical observation
            paragraph += f"\n\n\"Robot ini memberikan efisiensi yang luar biasa, mengubah cara kita bekerja dalam industri.\" - Tim R&D\n"
        
        paragraphs_list.append(paragraph)

    return "\n\n".join(paragraphs_list)

# Generate PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Insert robot image
robot_image = "Robot.jpg"
pdf.add_page()
if robot_image:
    pdf.image(robot_image, x=30, y=40, w=150)
    pdf.ln(70)

# Generate 50 unique chapter titles
chapter_titles = [
    "Pengenalan", "Spesifikasi Teknis", "Fitur Utama", "Desain dan Struktur",
    "Integrasi Sistem", "Keamanan dan Proteksi", "Pemeliharaan dan Dukungan", "Pemrograman dan AI",
    "Kinerja dan Efisiensi", "Aplikasi Industri", "Konektivitas dan IoT", "Sumber Daya Energi",
    "Daya Tahan dan Ketahanan", "Sensor dan Navigasi", "Pengendalian dan Operasi", "Algoritma dan AI",
    "Uji Coba dan Evaluasi", "Inovasi dan R&D", "Robotika dalam Masa Depan", "Dampak Sosial",
    "Kolaborasi dengan Manusia", "Komponen dan Material", "Analisis Data dan Statistik", "Pembaruan Perangkat Lunak",
    "Penggunaan di Rumah Tangga", "Keunggulan dibanding Model Sebelumnya", "Regulasi dan Standar",
    "Ekonomi dan Biaya Operasional", "Efisiensi Energi", "Persaingan Pasar", "Kemampuan Adaptasi",
    "Lingkungan Operasi", "Metode Pembuatan", "Studi Kasus", "Evaluasi Keberlanjutan",
    "Hubungan dengan AI Generatif", "Konektivitas 5G", "Dukungan Komunitas", "Perbandingan dengan Kompetitor",
    "Pengembangan Masa Depan", "Peningkatan Software", "Respons Terhadap Tantangan", "Studi Ergonomi",
    "Automasi dan Efeknya", "Daya Saing Global", "Keunikan dalam Desain", "Tantangan Pengembangan",
    "Uji Lapangan", "Evaluasi Pengguna", "Proyeksi 10 Tahun Kedepan"
]

# Define chart titles corresponding to chapters
chart_titles = {
    "Kinerja dan Efisiensi": "Grafik Kinerja Robot",
    "Aplikasi Industri": "Penggunaan Robot dalam Industri",
    "Konektivitas dan IoT": "Integrasi IoT dalam Robot",
    "Sensor dan Navigasi": "Akurasi Sensor Navigasi",
    "Algoritma dan AI": "Performa AI pada Robot",
    "Ekonomi dan Biaya Operasional": "Biaya Operasional Robot",
    "Efisiensi Energi": "Konsumsi Energi Robot",
    "Uji Coba dan Evaluasi": "Hasil Evaluasi Kinerja",
    "Daya Tahan dan Ketahanan": "Ketahanan Robot dalam Berbagai Lingkungan",
    "Studi Kasus": "Penerapan Robot dalam Kasus Nyata"
}

# Generate exactly 50 pages with at least 5-10 charts
chart_pages = sorted(random.sample(range(1, 51), random.randint(5, 10)))

for i, title in enumerate(chapter_titles[:50]):
    pdf.add_page()
    pdf.chapter_title(f"Bab {i+1}: {title}")
    
    if title in chart_titles:
        chart_filename = f"chart_{i}.png"
        generate_chart(chart_filename, chart_titles[title])
        pdf.image(chart_filename, x=40, y=60, w=120)  # Adjusted chart size and position
        pdf.ln(90)  # Ensure text starts below the image
    
    pdf.chapter_body(generate_text(10))

# Save PDF
pdf.output("Synthetic_Documentation_Robot_X2000_Variable.pdf")
