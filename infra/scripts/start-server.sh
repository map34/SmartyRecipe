#!/usr/bin/env bash

set -e

source activate TEST;
./infra/scripts/wait-for-postgres.sh python backend/server/manage.py migrate;
python backend/server/manage.py runserver 0.0.0.0:8000;
