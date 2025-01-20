from empire_chain.file_reader import DocumentReader

# Create the reader
reader = DocumentReader()

# First time you use it with a Google Drive link, it will:
# 1. Open your browser for authentication
# 2. Ask you to log in with your Google account
# 3. Ask for permission to access your Drive files
# 4. Save the token for future use
# Note: You might receive a warning that this process is harmful. 
# We have sent it for testing and it will be approved soon.
text = reader.read("https://drive.google.com/file/d/1t0Itw6oGO2iVusp=sharing")

print(text)
# Future uses will use the saved token
# (unless it expires, then it will ask for authentication again) 

text = reader.read("input.pdf")
print(text)