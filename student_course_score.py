import csv as csv
import sys
import random

def generate_csv_record(num_of_records):
    """Generates and writes student data to a CSV file.

    Args:
        num_of_records (int): The number of student records to generate.

    Returns:
        None
    """

    filename = 'data.csv'
    header = ['Student ID', 'Course ID', 'Marks']

    # Create an empty list to store records
    records = []
    for i in range(num_of_records):
        row = [
            random.randint(101, 110),  # Student ID (101-110)
            random.randint(201, 210),  # Course ID (201-210)
            random.randint(10, 100)    # Marks (10-100)
        ]
        records.append(row)

    # Open the file for writing in 'w' (write) mode
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)  # Write header row
        csvwriter.writerows(records)  # Write data rows

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python student_course_score.py <number_of_records>")
        sys.exit(1)

    # Get the number of records from the command line argument
    num_of_records = int(sys.argv[1])

    generate_csv_record(num_of_records)
