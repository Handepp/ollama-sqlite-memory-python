# Ollama SQLite Memory Chatbot

Local AI chatbot using Ollama with persistent conversation memory stored in SQLite.

Designed for low-resource devices (CPU-only laptops) without GPU.

---

## 🚀 Features

- Local LLM using Ollama
- Persistent chat memory with SQLite
- Session-based conversations
- Lightweight design (CPU friendly)
- Simple CLI interface

---

## 🧠 Architecture
User → Python CLI → SQLite Memory → Ollama → Response

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install ollama
```

Make sure Ollama is installed and running:

https://ollama.com

Pull a lightweight model:
```bash
ollama pull llama3.2:1b
```

## 📦 Configuration

Edit config.json:
```json
{
  "model": "llama3.2:1b",
  "system_prompt": "You are Jajang, a helpful AI assistant. Answer clearly and concisely.",
  "stream": false
}
```

## ▶️ How to Run

Run chatbot:
```bash
python app.py
```

## 💬 Example Usage

```text
You: halo selamat malam
AI: Selamat malam! Ada yang bisa saya bantu?

You: nama kamu siapa
AI: Saya Jajang, asisten AI kamu.
```

## 🗄️ Memory System

Chat history is stored in SQLite database:

- Persistent across sessions
- Session-based isolation
- Automatically loaded into model context

## ⚠️ Limitations

- Uses small model (llama3.2:1b)
- Running on CPU only may cause slower responses
- Possible hallucination due to model size
- Limited context window


## 💡 Notes

This project is designed for:

- Learning LLM integration
- Local AI experimentation
- Lightweight chatbot systems
- Embedded / low-resource AI applications

Not intended for production-scale deployment.

## 📄 License

MIT License