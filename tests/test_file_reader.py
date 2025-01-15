import unittest
from unittest.mock import patch, mock_open, MagicMock
from empire_chain.file_reader import DocumentReader, PDFReader, DocxReader, TxtReader, JSONReader, CSVReader

class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.reader = DocumentReader()
        
    def test_supported_formats(self):
        formats = self.reader.supported_formats()
        expected_formats = ['.pdf', '.docx', '.txt', '.json', '.csv']
        self.assertEqual(sorted(formats), sorted(expected_formats))
        
    def test_unsupported_format(self):
        with self.assertRaises(ValueError):
            self.reader.read("test.xyz")
            
    @patch('PyPDF2.PdfReader')
    def test_pdf_reader(self, mock_pdf_reader):
        mock_page = MagicMock()
        mock_page.extract_text.return_value = "PDF content"
        mock_pdf_reader.return_value.pages = [mock_page]
        
        with patch('builtins.open', mock_open()):
            text = self.reader.read("test.pdf")
            self.assertEqual(text.strip(), "PDF content")
            
    @patch('docx.Document')
    def test_docx_reader(self, mock_document):
        mock_para = MagicMock()
        mock_para.text = "DOCX content"
        mock_document.return_value.paragraphs = [mock_para]
        
        text = self.reader.read("test.docx")
        self.assertEqual(text.strip(), "DOCX content")
            
    def test_txt_reader(self):
        mock_content = "Text content"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            text = self.reader.read("test.txt")
            self.assertEqual(text, mock_content)
            
    def test_json_reader(self):
        mock_content = '{"key": "value"}'
        with patch('builtins.open', mock_open(read_data=mock_content)):
            text = self.reader.read("test.json")
            self.assertIn("key", text)
            self.assertIn("value", text)
            
    def test_csv_reader(self):
        mock_content = "header1,header2\nvalue1,value2"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            text = self.reader.read("test.csv")
            self.assertEqual(text.strip(), "header1,header2\nvalue1,value2")

if __name__ == "__main__":
    unittest.main() 