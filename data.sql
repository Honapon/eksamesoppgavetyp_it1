CREATE USER 'data' @'%' IDENTIFIED BY 'Idrive';

GRANT ALL PRIVILEGES ON *.* TO 'data'@'%' IDENTIFIED BY 'Idrive';

FLUSH PRIVILEGES;

CREATE DATABASE Hoytorptreffet;

CREATE TABLE Participants (
    ParticipantID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    PhoneNumber NVARCHAR(20),
    Address NVARCHAR(200),
    City NVARCHAR(50),
    Country NVARCHAR(50) 
);

CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,
    ParticipantID INT NOT NULL,
    VehicleType NVARCHAR(50) NOT NULL,
    Make NVARCHAR(50),
    Model NVARCHAR(50),
    Year INT,
    RegistrationNumber NVARCHAR(20),
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID)
);

CREATE TABLE ParticipationRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,
    ParticipantID INT NOT NULL,
    EventYear INT NOT NULL,
    Comments NVARCHAR(1000),
    FOREIGN KEY (ParticipantID) REFERENCES Participants(ParticipantID),
    UNIQUE (ParticipantID, EventYear)
);

CREATE TABLE Activities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY,
    ActivityName NVARCHAR(100) NOT NULL,
    Description NVARCHAR(1000),
    Duration INT,
    Organizer NVARCHAR(100)
);