-- Lists all Glam rock bands ranked by longevity
-- Columns: band_name and lifespan (years until 2022)
-- Uses formed and split attributes to calculate lifespan
SELECT 
    band_name,
    (IFNULL(split, 2022) - formed) AS lifespan
FROM 
    metal_bands
WHERE 
    style LIKE '%Glam rock%'
ORDER BY 
    lifespan DESC;
