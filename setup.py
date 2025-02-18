from setuptools import setup, find_packages

setup(
    name="empire-chain",
    version="0.4.7",    
    description="An orchestration framework for all your AI needs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Manas Chopra",
    author_email="manaschopra95826@gmail.com",
    url="https://github.com/manas95826/empire-chain",
    packages=find_packages(),
    install_requires=[
        "openai",
        "anthropic",
        "groq",
        "python-dotenv",
        "requests",
        "PyPDF2",
        "python-docx",
        "qdrant-client",
        "soundfile"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
