#! /bin/bash

# create a user
export PGUSER="uneku"

# create a db
psql -c "CREATE DATABASE inventory"

# create an extension if not exist
psql inventory -c "CREATE EXTENSION IF NOT EXISTS \"uuid-oossp\";"