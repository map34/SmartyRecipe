#!/usr/bin/env bash

set -e

echo 'Perform simple lint that environment is built' ;
source activate TEST;
flake8 .;
mypy --ignore-missing-imports --follow-imports=silent backend/
