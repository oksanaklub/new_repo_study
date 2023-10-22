import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('email3.csv', 'w') as new_csv:
        csv_writer = csv.writer(new_csv, delimiter=',')
        for line in csv_reader:
            csv_writer.writerow(line[2])
