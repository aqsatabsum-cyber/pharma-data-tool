import csv
import os
import random

print("="*50)
print("  Pharma Data Tool— Test File Generator")
print("="*50)

output_dir = "test_ftp_data"
os.makedirs(output_dir,exist_ok=True)

HEADERS = ["batch_id","timestamp","reading1","reading2","reading3",
           "reading4","reading5","reading6","reading7","reading8",
           "reading9","reading10"]
def random_readings():
    return [round(random.uniform(0.0, 9.9), 3) for _ in range(10)]

#GOOD FILE 
def generate_valid_file():
    filename="MED_DATA_20230603140104.csv"
    with open(os.path.join(output_dir, filename),"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(HEADERS)
        for batch_id in random.sample(range(1, 200),10):
            writer.writerow([batch_id, "14:01:04"] +random_readings())
    print(f"Generated: {filename}")

#BAD FILE 1:empty file 
def generate_empty_file():
    filename="MED_DATA_20230603140200.csv"
    open(os.path.join(output_dir, filename), "w").close()
    print(f"Generated: {filename}")

#BAD FILE 2:wrong filename format 
def generate_bad_filename():
    filename="med_data_20230603.csv"
    with open(os.path.join(output_dir, filename),"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(HEADERS)
        writer.writerow([55, "14:01:04"] +random_readings())
    print(f"Generated: {filename}")

#BAD FILE 3:wrong headers 
def generate_bad_headers():
    filename="MED_DATA_20230603140300.csv"
    bad_headers=["batch","timestamp","reading1","reading2","reading3",
                   "reading4","reading5","reading6","reading7","reading8",
                   "reading9","reading10"]
    with open(os.path.join(output_dir, filename),"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(bad_headers)
        writer.writerow([55,"14:01:04"] + random_readings())
    print(f"Generated: {filename}")

#BAD FILE 4:duplicate batch IDs
def generate_duplicate_batch_ids():
    filename="MED_DATA_20230603140400.csv"
    with open(os.path.join(output_dir, filename),"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(HEADERS)
        writer.writerow([55,"14:01:04"] +random_readings())
        writer.writerow([55,"14:01:05"] +random_readings())  #duplicate
    print(f"Generated: {filename}")

#BAD FILE 5:reading value too high
def generate_invalid_readings():
    filename="MED_DATA_20230603140500.csv"
    with open(os.path.join(output_dir, filename),"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(HEADERS)
        writer.writerow([55,"14:01:04", 10.5,9.1,1.2,3.4,
                         5.6,7.8,2.1,4.3,6.5,8.7])  #10.5 is invalid
    print(f"Generated: {filename}")

#BAD FILE 6:missing columns on a row 
def generate_missing_columns():
    filename="MED_DATA_20230603140600.csv"
    with open(os.path.join(output_dir, filename),"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(HEADERS)
        writer.writerow([55,"14:01:04",1.1,2.2,3.3])  #only 5 columns
    print(f"Generated: {filename}")

#Running all files
generate_valid_file()
generate_empty_file()
generate_bad_filename()
generate_bad_headers()
generate_duplicate_batch_ids()
generate_invalid_readings()
generate_missing_columns()

print(f"\nDone. 7 test files generated and saved to: {output_dir}")