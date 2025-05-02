-- Ranks country origins of bands by number of fans
-- Columns: origin and nb_fans
-- Ordered by number of fans in descending order
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
