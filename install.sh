#!/bin/bash

# Install the virtualenv package
pip install virtualenv

# Create a virtual environment with the name "venv"
python -m venv venv

# Activate the virtual environment
source venv/Scripts/activate

# Install the requirements from the requirements.txt file
# pip install -r requirements.txt