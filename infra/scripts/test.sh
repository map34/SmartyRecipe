#!/usr/bin/env bash

set -e

echo 'Perform simple test that environment is built' ;
source activate TEST;
python backend/server/manage.py test backend/
