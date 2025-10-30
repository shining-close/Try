import csv

def create_csv_file():
    file = open("ages.csv", "w", newline="")
    writer = csv.writer(file)
    file.close()
    print(f"File 'ages.csv' created successfully.")


create_csv_file()