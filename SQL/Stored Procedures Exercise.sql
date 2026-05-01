use Music_01


-- Create a basic SQL stored procedure to return a list of number 1 music albums. 

CREATE PROCEDURE usp_Number_1_Albums 
AS
	BEGIN
		SELECT * 
		FROM Album
		WHERE US_Billboard_200_peak = 1
	END

EXEC usp_Number_1_Albums

--  Create a SQL stored procedure to return a list of rock and roll music albums. 

CREATE PROCEDURE usp_Rock_and_Roll_Albums
AS
BEGIN
	SELECT
		a.Artist,
		b.Title,
		b.Release_date,
		b.Subgenre_ID,
		c.Subgenre
	FROM Album b
	INNER JOIN Artist a
		ON b.Artist_ID = a.Artist_ID
	INNER JOIN Subgenre c
		ON b.Subgenre_ID = c.Subgenre_ID
	WHERE b.Subgenre_ID = 21
	ORDER BY b.Title
END

-- Simplest stored procedure that only performs SUM using 3 parameters.
ALTER PROCEDURE SumThreeValues
	@A INT,
	@B INT,
	@C INT
AS
BEGIN
	DECLARE @Total INT
	SET @Total = @A + @B + @C
	SELECT @Total AS TotalSum
	--PRINT @Total 
END

EXEC SumThreeValues 10,20,30

