from astropy.timeseries import LombScargle
import csv
import numpy as np

def csv_conversion(file_directory, filename):
    fields = ['apogee_id', 'period (days)']
    rows = computePeriod(file_directory)
    filename = filename     # name of csv file

    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields and data rows
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

###This method returns the period for each star in a fits file.
def computePeriod(csv_file):
    file = open(csv_file)  # Open .fits data file
    csvreader = csv.reader(file)    #Use the csv.reader object to read the CSV file
    header = []
    header = next(csvreader)    #Read the field names
    header = next(csvreader)
    data = []                      #Extract the data
    for row in csvreader:
        data.append(row)

    period = np.empty([0,2])  # An array to store the period corresponding to each star (apogee_id)
    i=0
    while (i < len(data)):
        apogee_id = data[i][0]
        time = np.array([])
        vhelio = np.array([])
        vrelerr = np.array([])

        while (i <= len(data)-1 and data[i][0] == apogee_id):  # iterate through each star using the star's apogee_id
            time = np.append(time, int(data[i][13]))  # Append each visit's data
            vhelio = np.append(vhelio, float(data[i][9]))
            vrelerr = np.append(vrelerr, float(data[i][10]))
            i += 1

        if (len(time) <= 1):
            continue

        frequency, power = LombScargle(time, vhelio, vrelerr).autopower(maximum_frequency=1 )
        max_frequency = frequency[np.argmax(power)]  # Find the frequency with max power
        max_period = np.round(1.0/max_frequency, 2)
        period = np.append(period, [[apogee_id, max_period]], axis=0)  # Append to the period array

    return period

if __name__ == "__main__":
    csv_conversion('/Users/trinhnhathuy/Documents/2.McGill/Academic/3.2022Fall/SideProject_SDSS/binaryStarVisit100000.csv', 'binaryStarPeriod100000.csv')