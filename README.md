# ETL Pipeline Using Bash & Python

![ETL Pipeline](https://img.shields.io/badge/ETL-Pipeline-blue)
![Bash](https://img.shields.io/badge/Bash-4EAA25?logo=gnu-bash&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)

A robust ETL (Extract, Transform, Load) pipeline that extracts user data from the RandomUser.me API, processes it using Python/Pandas, and loads it into a PostgreSQL database with automated scheduling via cron jobs.

## 🚀 Features

- **Data Extraction**: Automated data retrieval from [RandomUser.me API](https://randomuser.me/api/) using Bash/curl
- **Data Transformation**: Efficient data processing with Python and Pandas
- **Database Loading**: Structured data storage in PostgreSQL using SQLAlchemy
- **Automated Scheduling**: Cron job automation for daily pipeline execution
- **Comprehensive Logging**: Full pipeline logging for monitoring and debugging
- **Normalized Database Schema**: Properly structured relational database design

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   RandomUser    │    │   Python        │    │   PostgreSQL    │
│   API           │──▶│   Transform     │──▶│   Database      │
│   (Source)      │    │   (Process)     │    │   (Target)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
        ▲                        ▲                     ▲
        │                        │                     │
   Bash/curl              Pandas/SQLAlchemy      Normalized Schema
```

## 📚 Prerequisites

Before running this ETL pipeline, ensure you have:

- **Linux/Unix environment** (tested on Linux)
- **Bash shell** (version 4.0+)
- **Python 3.7+** with pip
- **PostgreSQL** database server
- **curl** command-line tool
- **crontab** for scheduling (optional)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ETL_Using_Bash.git
   cd ETL_Using_Bash
   ```

2. **Install Python dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Create PostgreSQL database**:
   ```sql
   CREATE DATABASE your_database_name;
   ```

4. **Configure environment variables**:
   Create a `.env` file in the project root:
   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=your_database_name
   DB_USER=your_username
   DB_PASSWORD=your_password
   ```

5. **Make scripts executable**:
   ```bash
   chmod +x Main.sh BashScripts/*.sh
   ```

## 🚀 Usage

### Manual Execution

Run the complete ETL pipeline:
```bash
./Main.sh
```

### Individual Components

- **Extract data only**:
  ```bash
  ./BashScripts/Extraction.sh
  ```

- **Transform data only**:
  ```bash
  python3 PythonScripts/Transform.py
  ```

- **Create database tables**:
  ```bash
  python3 PythonScripts/CreateTable.py
  ```

- **Load data only**:
  ```bash
  ./BashScripts/Load.sh
  ```

## 🗄️ Database Schema

The pipeline creates a normalized database schema with the following tables:

- **person** - Main user information table
- **name** - User names (first, last, title)
- **location** - Address and location data
- **login** - Authentication details
- **dob** - Date of birth information
- **registered** - Registration timestamps
- **picture** - Profile picture URLs

> 📄 See `DB_Schema.txt` for detailed schema specifications.

## ⏰ Scheduling

To automate the pipeline execution:

1. **Open crontab editor**:
   ```bash
   crontab -e
   ```

2. **Add the following line** to run daily at 2:00 AM:
   ```bash
   0 2 * * * /path/to/your/project/Main.sh >> /path/to/your/project/logs/cron.log 2>&1
   ```

3. **Verify cron job**:
   ```bash
   crontab -l
   ```

## 📁 Project Structure

```
ETL_Using_Bash/
├── Main.sh                 # Main pipeline orchestrator
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── DB_Schema.txt         # Database schema documentation
├── .env                  # Environment variables (create this)
├── BashScripts/
│   ├── Extraction.sh     # Data extraction script
│   └── Load.sh          # Data loading script
├── PythonScripts/
│   ├── Transform.py     # Data transformation logic
│   └── CreateTable.py   # Database table creation
├── data/                # Raw and processed data files
│   ├── raw_data.csv    # Original extracted data
│   └── *_raw.csv       # Transformed data files
└── logs/               # Pipeline execution logs
    ├── pipeline.log    # Main pipeline logs
    └── cron.log       # Cron job execution logs
```

## 📊 Logs

The pipeline generates comprehensive logs:

- **`logs/pipeline.log`**: Main pipeline execution logs with timestamps
- **`logs/cron.log`**: Cron job execution logs and errors

Monitor logs in real-time:
```bash
tail -f logs/pipeline.log
```

## ⚠️ Important Notes

- **Database Creation**: You must manually create the PostgreSQL database before running the pipeline
- **No Virtual Environment**: This project is designed to run without Python virtual environments
- **Terminal Restart**: If the pipeline doesn't run initially, try restarting your terminal
- **File Permissions**: Ensure all shell scripts have execute permissions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
---

**Built with ❤️ using Bash, Python, and PostgreSQL**