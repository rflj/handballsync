#!/bin/bash
# Generate an encryption key. Each app should have its own.

# . ./scripts/bash/load_environment.sh
python -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key())'