#!/bin/sh

set +x
OLD_PWD=$PWD
ROOT_DIR=$(dirname $0)
cd $ROOT_DIR
if [ ! -d .venv ] ; then
  mkdir -p .venv
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install --upgrade pif git+git://github.com/saschpe/pygodaddy.git#egg=pygodaddy
python3 godaddy-dyndns.py
deactivate
cd $OLD_PWD
