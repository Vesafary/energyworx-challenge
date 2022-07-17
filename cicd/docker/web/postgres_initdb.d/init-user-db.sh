#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DATABASE" <<-EOSQL
    CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
    CREATE DATABASE $DB_DATABASE;
    GRANT ALL PRIVILIGES ON DATABASE $DB_DATABASE TO $DB_USER;
EOSQL