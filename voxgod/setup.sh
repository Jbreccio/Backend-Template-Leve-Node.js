#!/bin/bash

echo "🔧 Starting VOXGOD installation..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Update pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Final message
echo "✅ VOXGOD environment ready to use!"
echo "👉 Activate with: source venv/bin/activate"
echo "👉 Run with: python main.py"

from setuptools import setup, find_packages

setup(
    name='voxgod',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        # outros requisitos
    ],
    entry_points={
        'console_scripts': [
            'voxgod=interfaces.cli:cli',
        ],
    },
)
