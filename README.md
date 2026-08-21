# Chatbot with Ollama

A simple terminal-based chatbot that uses a local Ollama model to generate responses.

## Features

- Interactive chat in the terminal
- Keeps a conversation history in memory
- Uses a configurable Ollama model
- Lightweight Python project with a clean structure

## Project Structure

```text
chatbot/
├── app/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── config.py
│   ├── conversation.py
│   └── ollama_client.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

- Python 3.9+
- Ollama installed and running locally
- A model available in Ollama (the default is `qwen2.5:0.5b`)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/aleezagit/chatbot.git
cd chatbot
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Pull the model used by the app:

```bash
ollama pull qwen2.5:0.5b
```

## Usage

Run the chatbot:

```bash
python main.py
```

Then type your message in the terminal. Type `exit` to quit.

## Configuration

The app uses the model name defined in `app/config.py`:

```python
MODEL_NAME = "qwen2.5:0.5b"
```

You can change it to another Ollama-supported model if needed.

## How It Works

- `main.py` starts the chatbot
- `ChatBot` handles the terminal interaction
- `Conversation` stores the chat history
- `OllamaClient` sends the messages to the Ollama API and returns the model response

## Troubleshooting

### Ollama is not running

Start Ollama with:

```bash
ollama serve
```

### Model not found

Pull it again:

```bash
ollama pull qwen2.5:0.5b
```

### Dependencies not installed

```bash
pip install -r requirements.txt
```

## License

This project is open source and available for learning and development use.
