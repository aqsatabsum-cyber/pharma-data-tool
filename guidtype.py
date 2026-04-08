import requests
import csv
import os
from datetime import datetime

LOG_DIR="logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_guid():
    response=requests.get("https://www.uuidtools.com/api/generate/v1")
    guid=response.json()[0]
    return guid

def log_error(filename, reason):
    guid=get_guid()
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[ERROR LOG] Recording error for file: {filename}")
    log_file =os.path.join(LOG_DIR,"error_log.csv")
    file_exists=os.path.isfile(log_file)

    with open(log_file,"a",newline="") as f:
        writer=csv.writer(f)
        if not file_exists:
            writer.writerow(["guid","timestamp","filename","reason"])
        writer.writerow([guid,timestamp,filename,reason])

    print(f"Logged: {guid} | {filename} | {reason}")

log_error("MED_DATA_20230603140200.csv", "Empty file — 0 bytes")
log_error("MED_DATA_20230603140400.csv", "Duplicate batch_id values: [55]")
log_error("MED_DATA_20230603140500.csv", "Invalid reading value 10.5 at row 1")
