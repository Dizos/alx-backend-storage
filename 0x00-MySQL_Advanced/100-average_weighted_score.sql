-- Creates a stored procedure to compute and store weighted average score for a user
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE weighted_avg FLOAT;
    
    -- Calculate weighted average score
    SELECT SUM(c.score * p.weight) / SUM(p.weight) INTO weighted_avg
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;
    
    -- Update the user's average_score
    UPDATE users
    SET average_score = weighted_avg
    WHERE id = user_id;
END//
DELIMITER ;
