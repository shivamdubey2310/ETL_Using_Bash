# ETL_Using_Bash
ETL using bash, extracting from randomuser.me/api/

- Extracting using bash (curl) from randomuser.me/api/
- Transforming using pandas(python)
- Loaded in postgresql using sqlalchemy
- Scheduled using cronjob.

---

## Instructions
- don't use venv
- You have to create database(not tables) in order to run this etl
- restart terminal if it does not run at once
- To schedule it - use `crontab -e` and in that file write `0 2 * * * /mnt/mydrive/ETL_Using_Bash/Main.sh >> /mnt/mydrive/ETL_Using_Bash/logs/cron.log 2>&1` to schedule it to run every night at 2 AM

----