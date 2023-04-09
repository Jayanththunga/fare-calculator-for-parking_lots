import csv
from datetime import datetime
header = ['License Plate No.', 'Vehicle Type', 'Entry Time', 'Balance']
text = 'MCLRNF1'
data = [text, 'Car', datetime.now(), 50000]

with open('./dup.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)
