#!/bin/bash
CYAN='\033[0;36m'
TRANS='\033[0m'

printf "\n${CYAN}Waiting for Database...${TRANS}\n"
dockerize -wait tcp://database:5432 -timout 30s

printf "\n${CYAN}Applying database migrations...${TRANS}\n"
python manage.py migrate --noinput
printf "\n${CYAN}...finished applying database migrations.${TRANS}\n"

printf "\n${CYAN}Checking for missing database migrations...${TRANS}\n"
python manage.py makemigrations --noinput --dry-run
printf "\n${CYAN}...finished checking for missing database migrations.${TRANS}\n"

printf "\n${CYAN}Starting Django server...${TRANS}\n"
python manage.py runserver 0.0.0.0:8000
