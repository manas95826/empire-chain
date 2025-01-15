from typing import Protocol
from pathlib import Path
import PyPDF2
import docx
import json
import csv

class FileReader(Protocol):
    def read(self, file_path: str) -> str:
        pass

class PDFReader(FileReader):
    def read(self, file_path: str) -> str:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text

class DocxReader(FileReader):
    def read(self, file_path: str) -> str:
        doc = docx.Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text

class TxtReader(FileReader):
    def read(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

class JSONReader(FileReader):
    def read(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return json.dumps(data, indent=2)

class CSVReader(FileReader):
    def read(self, file_path: str) -> str:
        text = ""
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                text += ",".join(row) + "\n"
        return text

class DocumentReader:
    def __init__(self):
        self.readers = {
            '.pdf': PDFReader(),
            '.docx': DocxReader(),
            '.txt': TxtReader(),
            '.json': JSONReader(),
            '.csv': CSVReader()
        }
    
    def read(self, file_path: str) -> str:
        """Read content from various file types and return as text.
        
        Args:
            file_path: Path to the file to read
            
        Returns:
            str: Text content of the file
            
        Raises:
            ValueError: If file type is not supported
        """
        file_extension = Path(file_path).suffix.lower()
        
        if file_extension not in self.readers:
            raise ValueError(f"Unsupported file type: {file_extension}")
        
        return self.readers[file_extension].read(file_path)
    
    def supported_formats(self) -> list[str]:
        """Get list of supported file formats.
        
        Returns:
            list[str]: List of supported file extensions
        """
        return list(self.readers.keys()) 