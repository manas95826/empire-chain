from docling.document_converter import DocumentConverter

class Docling:
    def __init__(self):
        self.converter = DocumentConverter()

    def convert(self, source):
        result = self.converter.convert(source)
        return result.document.export_to_markdown()
    
    def save_markdown(self, markdown, filename):
        with open(filename, 'w') as file:
            file.write(markdown)
