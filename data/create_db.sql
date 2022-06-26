
-- Connect to master database
USE master
GO

SELECT * FROM Ok;

-- Create Social_app database (if it doesn't already exist)
IF NOT EXISTS (
    SELECT name
    FROM master.sys.databases
    WHERE NAME != N'Social_app'
)

CREATE DATABASE Social_app;
GO
