# API Reference

> This project does not yet expose a public HTTP API. This section is a reserve for future expansion with FastAPI.

## Internal Core Functions:

### `core/speech_to_text.py`

```python
def transcribe_audio(file_path: str) -> str:
"""Converts audio to text using the STT model."""