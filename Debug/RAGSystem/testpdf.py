import os
import pdfplumber

def process_pdfs(pdf_folder):
    """Extract text from PDFs in the given folder"""
    text_data = ""

    if not os.path.exists(pdf_folder):
        print(f"❌ Folder '{pdf_folder}' does not exist!")
        return ""

    files = os.listdir(pdf_folder)
    print(f"📂 Found Files in '{pdf_folder}':", files)  # Debugging output

    for file in files:
        file_path = os.path.join(pdf_folder, file)
        print(f"🔍 Checking File: {file_path}")

        if file.endswith(".pdf"):
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text_data += page.extract_text() or ""  # Handle None values
            print(f"✅ Processed PDF: {file}")

    return text_data.strip()

# ✅ Run PDF Processing
pdf_text = process_pdfs("pdfs")
print("\n📄 Extracted PDF Text:\n", pdf_text)
