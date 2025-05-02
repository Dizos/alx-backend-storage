-- Creates a function SafeDiv that safely divides two numbers
-- Returns a / b or 0 if b = 0
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    RETURN IF(b = 0, 0, a / b);
END//
DELIMITER ;
