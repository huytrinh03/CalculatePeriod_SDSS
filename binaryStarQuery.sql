-- This query finds binary stars from apogeeStar

SELECT star.apogee_id, star.apstar_id, star.ra, star.dec, star.nvisits,
star.snr, star.vscatter, star.verr
FROM apogeeStar as star
WHERE star.nvisits >= 8 AND star.vscatter > 10*star.verr AND star.snr >= 5
