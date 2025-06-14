#!/bin/bash

# Map of CSV filenames (without extension) to target SQL table names
declare -A table_map=(
    ["name_raw"]="name"
    ["location_raw"]="location"
    ["login_raw"]="login"
    ["dob_raw"]="dob"
    ["registered_raw"]="registered"
    ["picture_raw"]="picture"
)

# Time stamp for logging
NOW=`date '+%F %H:%M:%S'`;  # A variable for current date and time

# Fetching data from .env
source .env

# Set paths and connection details
csv_path="$csv_path"
db_name="$db_name"
db_user="$db_user"
db_host="$db_host"
db_passwd="$db_passwd"

export PGPASSWORD="$db_passwd" # so child process psql can use it

# Loop through each CSV and load into corresponding table
for file_base in "${!table_map[@]}"; do
    table_name="${table_map[$file_base]}"
    csv_file="$csv_path/${file_base}.csv"

    if [[ -f "$csv_file" ]]; then
        echo "$NOW - INFO - Importing '$csv_file' into table '$table_name'..." >> logs/pipeline.log
        psql -U "$db_user" -d "$db_name" -h "$db_host" -c "\copy $table_name FROM '$csv_file' DELIMITER ',' CSV HEADER;" \
        && echo "$NOW - INFO - Successfully imported $table_name." >> logs/pipeline.log\
        || echo "$NOW - ERROR - Failed to import into $table_name." >> logs/pipeline.log
    else
        echo "$NOW - ERROR - File not found: $csv_file" >> logs/pipeline.log
    fi
done

# # Clean up password from environment
unset PGPASSWORD