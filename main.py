from profile import*
import csv


def readCSV(filename):
    profiles = []
    with open(filename, encoding="UTF-8") as f:
        reader = csv.reader(f)
        reader.__next__()
        for line in reader:
            profiles.append(Profile(*line[1:]))
    return profiles




if __name__ == '__main__':
    profiles = readCSV("data.csv")
    for profile in profiles:
        print(profile)
        