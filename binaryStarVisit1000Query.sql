-- leave out those who have bitmask #4, #19, #22,
-- caution with those who have bitmask #3, #18, #21, #0

SELECT TOP 1000
star.apogee_id, star.apstar_id, star.ra, star.dec, star.nvisits,
star.snr as starSNR, star.vscatter, star.verr,
starVisit.visit_id,
visit.vhelio, visit.vrelerr, visit.snr as visitSNR, visit.starflag, visit.mjd
FROM apogeeStar as star
JOIN apogeeStarVisit as starVisit on star.apstar_id = starVisit.apstar_id
JOIN apogeeVisit as visit on starVisit.visit_id = visit.visit_id
WHERE star.nvisits >= 8 AND star.vscatter > 10*star.verr AND star.snr >= 5
AND visit.starflag % POWER(2,1) < POWER(2,0) --Condition for 0th to be 0
AND visit.starflag % POWER(2,5) < POWER(2,4) --Condition for 4th to be 0
AND visit.starflag % POWER(2,20) < POWER(2,19) --Condition for 19th bit to be 0
AND visit.starflag % POWER(2,23) < POWER(2,22) --Condition for 22th bit to be 0
order by star.apogee_id ASC