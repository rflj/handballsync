#!/bin/bash
set -e

# Load virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
export SECRET_KEY=$(./scripts/generate_encryption_key.sh)
echo $SECRET_KEY
export DEBUG=1
export DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1]"
python ./backend/manage.py runserver
