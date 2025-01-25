"""
This is a simple file reader that uses the Empire Chain library to read a file.
It supports 
1. PDF files (.pdf)
2. Microsoft Word documents (.docx)
3. Text files (.txt)
4. JSON files (.json)
5. CSV files (.csv)
6. Google Drive files (.gdrive)
"""
from empire_chain.tools.file_reader import DocumentReader
reader = DocumentReader()

text = reader.read("https://drive.google.com/file/d/1t0Itw6oGO2iVusp=sharing")
print(text)

text = reader.read("input.pdf")
print(text)