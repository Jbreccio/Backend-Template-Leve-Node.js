# VOXGOD Architecture

VOXGOD is composed of well-defined modules, integrating NLP, speech recognition, and task automation technologies via voice commands.

## Main Modules:

- `core/`: Core with NLP, STT, task management, and voice response engines.
- `interfaces/`: Entry points such as CLI and web interface.
- `utils/`: Auxiliary functions, logging, and configuration.
- `tasks/`: Set of executable commands and functionalities.
- `models/`: Machine learning models or NLP rules (in the future).
- `docs/`: Project documentation.
- `tests/`: Automated tests for each module.
- `docker/`: Contains files for containerizing the application.

## Execution Flow:

1. User sends a voice command via CLI or web interface. 2. `speech_to_text.py` converts audio to text.
3. `nlp_engine.py` interprets the intent of the text.
4. `task_manager.py` directs to the appropriate task.
5. `voice_response.py` sends a voice response.

## Technologies:

- Python 3.10+
- OpenAI Whisper / Vosk for STT
- SpaCy / Transformers for NLP
- Docker for deployment
- FastAPI (optional, web version coming soon)