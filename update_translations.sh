#!/usr/bin/env bash

VENV_DIR=app/env

set +u # workaround for a bug in venv (see: https://github.com/pypa/virtualenv/issues/150)
source $VENV_DIR/bin/activate
set -u

echo "Extracting messages to translate..."
python setup.py extract_messages -o app/locale/app.pot
echo -en "\033[0;32m" # green font
echo "Setup done!"
echo -en "\033[0m" # reset font

echo "Updating the catalog..."
python setup.py update_catalog -o app/locale/app.pot
echo "Setup done!"
echo -en "\033[0m" # reset font
echo "Updating the catalog..."

echo "Extracting messages to translate..."
python setup.py compile_catalog -o app/locale/app.pot
echo -en "\033[0;32m" # green font
echo "Setup done!"
echo -en "\033[0m" # reset font

msginit -l en -o app/locale/en/LC_MESSAGES/app.po --input app/locale/app.pot
msginit -l pl -o app/locale/pl/LC_MESSAGES/app.po --input app/locale/app.pot
msginit -l no -o app/locale/no/LC_MESSAGES/app.po --input app/locale/app.pot

python setup.py compile_catalog -D app -d app/locale
