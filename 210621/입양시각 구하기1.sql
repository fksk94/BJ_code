SELECT HOUR(DATETIME) as HOUR, COUNT(DATETIME) as COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) between 9 and 19
GROUP BY HOUR
ORDER BY HOUR