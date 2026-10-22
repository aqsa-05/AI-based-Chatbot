# AI-Based Chatbot

A command-line conversational chatbot built with Python, PyTorch and Hugging Face Transformers. It runs locally on your own machine using a free, open-source language model from the Hugging Face Hub.

## Features

- Chat with an open-source language model directly in the terminal
- Keeps recent conversation history so replies stay in context
- Configurable generation settings (temperature, top-p, repetition penalty)
- Easy to swap in a different Hugging Face model
- Runs on CPU, with GPU support if available

## Tech Stack

- Python 3.10+
- PyTorch
- Hugging Face Transformers
- Accelerate

## Project Structure

```
AI-based-Chatbot/
├── chatbot_llm.py    # Main chatbot script
├── requirements.txt  # Python dependencies
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aqsa-05/AI-based-Chatbot.git
cd AI-based-Chatbot
```

### 2. Create and activate a virtual environment

```bash
python -m venv my_env

# Windows (PowerShell)
my_env\Scripts\Activate.ps1

# macOS / Linux
source my_env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the chatbot

```bash
python chatbot_llm.py
```

The first run downloads the model and caches it, so you need an internet connection and some free disk space. Type `exit` to quit the chatbot.

## How It Works

1. The script loads a pre-trained model and its tokenizer from Hugging Face.
2. Your message and the recent conversation history are formatted into a prompt.
3. The model generates a reply, which is decoded and printed to the terminal.
4. The new exchange is saved to the history, which is trimmed to the most recent turns.

## Changing the Model

Set `model_name` near the top of `chatbot_llm.py` to any compatible model on the Hugging Face Hub. Some free options:

- `Qwen/Qwen2.5-0.5B-Instruct` (fastest, good for low-end laptops)
- `Qwen/Qwen2.5-1.5B-Instruct` (good balance of quality and speed)
- `HuggingFaceTB/SmolLM2-1.7B-Instruct`

Larger models give better answers but need more RAM and run slower on CPU.

## Troubleshooting

- **Version errors:** keep the main libraries up to date with `pip install -U torch transformers accelerate`.
- **"requires accelerate" error:** run `pip install -U accelerate`.
- **Slow replies:** try a smaller model, or run on a machine with a GPU.

## Notes

Small language models can give inaccurate or made-up answers, so treat their output with care.

## Future Improvements

- Streaming responses as they are generated
- Longer conversation memory
- A web interface

## License

This project is for learning and personal use. Models are subject to their own licenses on the Hugging Face Hub.
