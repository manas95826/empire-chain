from empire_chain.tools.docling import Docling

docling = Docling()

converted_doc = docling.convert("https://arxiv.org/pdf/2408.09869")
docling.save_markdown(converted_doc, "arxiv_2408.09869.md")