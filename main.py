from astropy.timeseries import LombScargle
from astropy import units
from astropy.io import fits
import numpy as np

def fits_conversion(array):
    return

###This method returns the period for each star in a fits file.
def computePeriod(fits_file):
    hdu = fits.open(fits_file, memmap=True)  # Open .fits data file
    data = hdu[1].data  # Get the data
    hdu.close()     # Close the file

    # apogee_id  apstar_id ra  dec nvisits starSNR vscatter  verr  visit_id  vhelio  vrelerr visitSNR  starflag  mjd
    # 2M00000662+7528598 apogee.apo25m.stars.120+12.2M00000662+7528598 0.027622  75.483292 9 827.6752  2.006593  0.08394658  apogee.apo25m.dr17.7545.56933.190 15.74034  0.07290228  233.139 1179648 56933
    period = np.array([])  # An array to store the period corresponding to each star (apogee_id)
    for i in (0, len(data)):
        apogee_id = data[i][0]
        time = np.array([])
        vhelio = np.array([])
        vrelerr = np.array([])

        while (i <= len(data)-1 and data[i][0] == apogee_id):  # iterate through each star using the star's apogee_id
            time = np.append(time, data[i][13])  # Append each visit's data
            vhelio = np.append(vhelio, data[i][9])
            vrelerr = np.append(vrelerr, data[i][10])
            i += 1

        #time = time * units.day  # Add units to the star's data arrays
        #vhelio = vhelio * units.km / units.s
        #vrelerr = vrelerr * units.km / units.s

    frequency, power = LombScargle(time, vhelio, vrelerr).autopower()  # Compute Lomb-Scargle power
    max_frequency = frequency[np.argmax(power)]  # Find the frequency with max power
    period.append([apogee_id, max_frequency])  # Append to the period array


if __name__ == "__main__":
    period_data = computePeriod('/Users/trinhnhathuy/Documents/2.McGill/Academic/3.2022Fall/SideProject_SDSS/binaryStarVisit1000.fits')
