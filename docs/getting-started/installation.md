# Installation Guide

## Prerequisites

Before installing Empire Chain, ensure you have the following prerequisites:

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation Methods

### 1. Using pip (Recommended)

```bash
pip install empire-chain
```

### 2. From Source

To install the latest development version:

```bash
git clone https://github.com/yourusername/empire-chain.git
cd empire-chain
pip install -e .
```

### 3. Development Installation

For development purposes, install with additional dependencies:

```bash
pip install -e ".[dev]"
```

## Verifying Installation

You can verify your installation by running:

```python
import empire_chain
print(empire_chain.__version__)
```

## Dependencies

Empire Chain has the following core dependencies:

- numpy
- pandas
- torch
- transformers
- streamlit
- langchain
- pillow
- matplotlib

These will be automatically installed when you install Empire Chain.

## Optional Dependencies

Some features require additional dependencies:

### For PDF Processing
```bash
pip install "empire-chain[pdf]"
```

### For Image Processing
```bash
pip install "empire-chain[image]"
```

### For Development
```bash
pip install "empire-chain[dev]"
```

## Troubleshooting

### Common Issues

1. **Version Conflicts**
   ```bash
   pip install --upgrade empire-chain
   ```

2. **Missing Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **CUDA Issues**
   Make sure you have compatible CUDA drivers installed if you plan to use GPU acceleration.

If you encounter any issues, please check our [GitHub Issues](https://github.com/yourusername/empire-chain/issues) page or create a new issue. 