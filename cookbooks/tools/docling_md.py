# """
# This is a simple tool that uses the Empire Chain library to convert a PDF file to markdown.
# Please run the following command to install the necessary dependencies and store keys in .env:
# !pip install empire-chain docling
# """
# from empire_chain.tools.docling import Docling

# docling = Docling()

# converted_doc = docling.convert("https://arxiv.org/pdf/2408.09869")
# docling.save_markdown(converted_doc, "arxiv_2408.09869.md")

# Todo: This is in development!