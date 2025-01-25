from empire_chain.tools.file_reader import DocumentReader
reader = DocumentReader()

text = reader.read("https://drive.google.com/file/d/1t0Itw6oGO2iVusp=sharing")
print(text)

text = reader.read("input.pdf")
print(text)