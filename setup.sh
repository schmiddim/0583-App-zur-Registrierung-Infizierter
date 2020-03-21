#!/usr/bin/env bash
# Copyright (C) 2018 Nokia. All rights reserved.

# Enable strict mode
set -euo pipefail

echo "Preparing environment..."

VENV_DIR=app/env

echo "Creating python venv..."
python3 -c "import sys; assert sys.version_info[:3] >= (3, 6, 2), 'Wrong version of Python'"
python3 -m venv --clear $VENV_DIR

set +u # workaround for a bug in venv (see: https://github.com/pypa/virtualenv/issues/150)
source $VENV_DIR/bin/activate
set -u

echo "Installing required packages..."
pip install --upgrade pip setuptools
pip install -e "git+https://github.com/schmiddim/0583-App-zur-Registrierung-Infizierter.git#egg=0583-App-zur-Registrierung-Infizierter" ".[testing]"

echo -en "\033[0;32m" # green font
echo "Setup done!"
echo -en "\033[0m" # reset font
echo "Invoke the following to activate your venv:"
echo "source $VENV_DIR/bin/activate"
echo -en "\033[0;32m" # green font
echo "Setup done!"
echo -en "\033[0m" # reset font

echo "Generate your first revision"
alembic -c development.ini revision --autogenerate -m "init"
echo "Go to this revision..."
alembic -c development.ini upgrade head 
echo -en "\033[0;32m" # green font
echo "Done!"
echo -en "\033[0m" # reset font

echo "Load default data into the database using a script."
initialize_app_db development.ini
echo -en "\033[0;32m" # green font
echo "Done!"
echo -en "\033[0m" # reset font
