#!/bin/bash
set -ex
APP="database"

# Set up dummy Django project
rm -rf /tmp/testproject
mkdir -p /tmp/testproject
django-admin startproject config /tmp/testproject

# Add to INSTALLED_APPS
ln -s "$(pwd)" /tmp/testproject/database
sed -i -E 's/(INSTALLED_APPS *= *\[)/\1\n"database",/' /tmp/testproject/config/settings.py

cp pytest.ini /tmp/testproject/
cd /tmp/testproject

# Run tests
pytest

