# tests/test_dependency.py

def test_import_dependencies():
    try:
        import soundfile
        import cffi
        import pycparser
        import empire_chain
    except ImportError as e:
        assert False, f"Import failed: {e}"
