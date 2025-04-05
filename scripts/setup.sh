#!/bin/bash

# Delete .venv folder
rm -r .venv

# Create a Python virtual environment
python3 -m venv .venv

echo 'source .venv/bin/activate' >> ~/.bashrc

# Activate the virtual environment
. ./.venv/bin/activate

# Install development dependencies
python -m pip install -r requirements-dev.txt