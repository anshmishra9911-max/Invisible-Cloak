#!/bin/bash
echo "Installing requirements..."
pip3 install -r requirements.txt
echo ""
echo "First, let's capture background..."
python3 background.py
echo ""
echo "Now running invisibility cloak..."
python3 invisible_cloak.py