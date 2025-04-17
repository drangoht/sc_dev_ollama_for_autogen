#!/bin/bash

# --- Install Ollama ---
curl -fsSL https://ollama.com/install.sh | OLLAMA_VERSION=0.3.13 sh

# --- Start Ollama server in background ---
nohup ollama serve &

# --- Wait for warm-up ---
sleep 5

# --- Download a model ---
ollama pull llama3

# --- Create and activate a virtual environment ---
python3 -m venv venv
source venv/bin/activate

# --- Upgrade pip & install requirements ---
pip install --upgrade pip
pip install -r requirements.txt
