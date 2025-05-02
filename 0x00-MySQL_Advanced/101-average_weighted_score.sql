-- Creates a stored procedure to compute and store weighted average scores for all users
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Update all users with their weighted average scores
    UPDATE users u
    JOIN (
        SELECT 
            c.user_id,
            SUM(c.score * p.weight) / SUM(p.weight) AS weighted_avg
        FROM 
            corrections c
        JOIN 
            projects p ON c.project_id = p.id
        GROUP BY 
            c.user_id
    ) AS calculations ON u.id = calculations.user_id
    SET u.average_score = calculations.weighted_avg;
END//
DELIMITER ;
