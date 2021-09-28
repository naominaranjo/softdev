import csv

temp = {
  "Legal": 0.8,
  "Education, training and library": 6.1,
}

def readFile(file):
    dict = {}
    with open(file, newline='') as csvfile:
        occupations = csv.reader(csvfile, delimiter=',', quotechar='"')
        x = 0
        for row in occupations:
            if x == 0:
                x = x + 1
            else:
                dict[row[0]] = float(row[1])
    return dict

stuff = readFile('occupations.csv')
print(stuff)
