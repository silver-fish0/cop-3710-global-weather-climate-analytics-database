CREATE TABLE Location (
    LocationID INT PRIMARY KEY,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    Elevation DECIMAL(10,2),
    Latitude DECIMAL(9,6) NOT NULL,
    Longitude DECIMAL(9,6) NOT NULL
);

CREATE TABLE WeatherStation (
    StationID VARCHAR(20) PRIMARY KEY,
    StationName VARCHAR(100) NOT NULL,
    InstallationDate DATE NOT NULL,
    LocationID INT NOT NULL,
    FOREIGN KEY (LocationID) REFERENCES Location(LocationID)
);

CREATE TABLE StationMetadata (
    StationID VARCHAR(20) PRIMARY KEY,
    LastCalibrationDate DATE,
    DataSource VARCHAR(100),
    Status VARCHAR(50),
    FOREIGN KEY (StationID) REFERENCES WeatherStation(StationID)
);

CREATE TABLE MeasurementType (
    TypeID INT PRIMARY KEY,
    TypeName VARCHAR(100) NOT NULL,
    Unit VARCHAR(50) NOT NULL,
    Description VARCHAR(255)
);

CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Role VARCHAR(50) NOT NULL,
    Organization VARCHAR(100)
);

CREATE TABLE DailyMeasurement (
    StationID VARCHAR(20) NOT NULL,
    TypeID INT NOT NULL,
    MeasurementDate DATE NOT NULL,
    Value DECIMAL(10,2) NOT NULL,
    QualityFlag VARCHAR(50),
    PRIMARY KEY (StationID, TypeID, MeasurementDate),
    FOREIGN KEY (StationID) REFERENCES WeatherStation(StationID),
    FOREIGN KEY (TypeID) REFERENCES MeasurementType(TypeID)
);

CREATE TABLE UserQuery (
    UserID INT NOT NULL,
    TypeID INT NOT NULL,
    QueryDate TIMESTAMP NOT NULL,
    FiltersApplied VARCHAR(255),
    PRIMARY KEY (UserID, TypeID, QueryDate),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (TypeID) REFERENCES MeasurementType(TypeID)
);
