import csv as cs

with open('file.csv', 'w') as file:
    writer = cs.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['John', '25', 'New York'])
    writer.writerow(['Jane', '30', 'London'])
