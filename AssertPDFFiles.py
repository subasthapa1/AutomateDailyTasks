import argparse
import PyPDF2
class AssertPDFFiles:
    """
    This class contains all the functions necessary to validate PDF files content
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def read_pdf(self):
        text = ''

        try:
            with open(self.file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                num_pages = len(reader.pages)

                for page_num in range(num_pages):
                    page = reader.pages[page_num]
                    text += page.extract_text()
        except Exception as e:
            print(f"Error reading PDF file: {e}")
        return text

    def verify_text_on_pdf(self, expected_text='Manual testing'):
        pdf_text = self.read_pdf()
        assert expected_text in pdf_text, f"Expected text '{expected_text}' not found in the PDF."


def main():
    parser = argparse.ArgumentParser(description='Read a PDF file and print its contents.')
    parser.add_argument('file_path', type=str, help='Path to the PDF file')

    args = parser.parse_args()

    pdf_reader = AssertPDFFiles(args.file_path)
    pdf_text = pdf_reader.read_pdf()
    print(pdf_text)
    pdf_reader.verify_text_on_pdf()


if __name__ == '__main__':
    main()
