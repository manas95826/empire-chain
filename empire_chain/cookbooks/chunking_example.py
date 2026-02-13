from empire_chain.utils.chunking import DocumentChunker

# A long sample text
text = "This is a test sentence. " * 100  # 2800+ characters

# Create a chunker with size 300 and overlap 50
chunker = DocumentChunker(chunk_size=300, overlap=50)
chunks = chunker.chunk_text(text)

# Output result
print(f"Total chunks: {len(chunks)}")
for i, chunk in enumerate(chunks[:3]):
    print(f"\n--- Chunk {i+1} ---\n{chunk[:200]}...")  # show only first 200 chars of each
