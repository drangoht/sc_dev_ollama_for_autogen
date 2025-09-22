#!/bin/bash

# --- Install Ollama ---

# curl -fsSL https://ollama.com/install.sh | OLLAMA_VERSION=0.12.1 sh
curl -fsSL https://ollama.com/install.sh | sh
# --- Start Ollama server in background ---
nohup ollama serve &

# --- Wait for warm-up ---
sleep 10

# --- Download a model ---
ollama pull gemma3:12b

# --- Create and activate a virtual environment ---
python3 -m venv venv
source venv/bin/activate

# --- Upgrade pip & install requirements ---
pip install --upgrade pip
pip install -r requirements.txt

pip install flaml[automl]