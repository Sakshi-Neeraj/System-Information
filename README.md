# System-Information
System Information (through Python Program) from GCE-> SQL Cloud Database-> Power BI Connection

Create GCE and Cloud SQL instance in GCP

Connect to GCE using SSH through console

SQL Studio Queries-

CREATE DATABASE system_information;

CREATE TABLE performance (

time TIMESTAMP,

cpu_usage FLOAT,

memory_usage FLOAT,

cpu_interrupts FLOAT,

cpu_calls FLOAT,

memory_used FLOAT,

memory_free FLOAT,

bytes_sent FLOAT,

bytes_received FLOAT,

disk_usage FLOAT

);

GCE Commands-

sudo apt update

sudo apt install python3-pip -y

sudo apt install python3-venv -y

python3 -m venv monitor-env

source monitor-env/bin/activate

pip install psutil psycopg2-binary

python3 monitor.py
