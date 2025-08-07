# VOXGOD

**VOXGOD** is a revolutionary full-stack voice-based automation platform with embedded artificial intelligence for development, infrastructure management, deployment, and more. All done in a Dockerized, secure, and integrated way with your development stack.

## 🚀 Vision

> A voice-controlled DevOps and Developer AI assistant capable of creating, deploying, monitoring, managing, and refactoring projects in real time—just with natural commands.

## 🧠 Key Technologies

- Python 3.11+
- FastAPI
- LangChain
- Whisper (ASR)
- TTS (Coqui.ai / ElevenLabs)
- Docker & Docker Compose
- GitHub API
- OpenAI GPT-4o (via API)
- SQLite (MVP) / PostgreSQL (Production)
- SpeechRecognition
- Pyttsx3 (local TTS fallback)
- Celery + Redis
- Frontend: Tailwind + Next.js *(in Phase 2)*

## 📦 Installation (dev mode)

```bash
git clone https://github.com/SEU-USUARIO/voxgod.git
cd voxgod
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
