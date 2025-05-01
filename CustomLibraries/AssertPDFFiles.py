import PyPDF2
import logging

class AssertPDFFiles:
    def __init__(self):
        return

    def get_pdf_content(self, file_path):
        text = ''
        logging.info('Reading content of a PDF file')
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text() or ''
        except Exception as e:
            print(f"Error reading PDF file {file_path}: {e}")
        return text

    def verify_text_on_pdf(self, file_path, expected_text):
        pdf_text = self.get_pdf_content(file_path)
        try:
            assert expected_text in pdf_text, f"Expected text '{expected_text}' not found in the PDF."
            print(f"✓ Found expected text: '{expected_text}'")
        except AssertionError as e:
            print(f"✗ {e}")

    def check_images_in_pdf(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page_number, page in enumerate(reader.pages):
                    if '/XObject' in page['/Resources']:
                        xObject = page['/Resources']['/XObject'].get_object()
                        for obj in xObject:
                            if xObject[obj]['/Subtype'] == '/Image':
                                print(f"✓ Image found on page {page_number + 1}")
                                return True
            print("✗ No images found in PDF.")
            return False
        except Exception as e:
            print(f"Error processing PDF: {e}")
            return False

def main():
    file_path = r'D:\Projects\Automation\Files\power-bi-guidance.pdf'
    pdf_reader = AssertPDFFiles()
    pdf_text = pdf_reader.get_pdf_content(file_path)
    #print(pdf_text)
    for keyword in ['Power BI reports', 'DAX', 'Power BI paginated reports']:
        pdf_reader.verify_text_on_pdf(file_path, keyword)
    pdf_reader.check_images_in_pdf(file_path)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
