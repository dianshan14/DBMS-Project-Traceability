DROP TABLE IF EXISTS Manufacturer
DROP TABLE IF EXISTS Jobber
DROP TABLE IF EXISTS Market
DROP TABLE IF EXISTS Retailer
DROP TABLE IF EXISTS Commodity
DROP TABLE IF EXISTS Sell
DROP TABLE IF EXISTS Distribute

CREATE TABLE Manufacturer(
	Manufacturer_ID INTEGER PRIMARY KEY,
	Manufacturer_name TEXT NOT NULL,
	Commodity_ID INTEGER NOT NULL,
	amount INTEGER NOT NULL
);

CREATE TABLE Jobber(
	Jobber_ID INTEGER PRIMARY KEY,
	Jobber_name TEXT NOT NULL,
	Commodity_ID INTEGER NOT NULL,
	Commodity_stock INTEGER NOT NULL
);

CREATE TABLE Market(
	Market_ID INTEGER PRIMARY KEY,
	Region TEXT NOT NULL,
	Area INTEGER NOT NULL,
	Retailer_amount INTEGER NOT NULL
);

CREATE TABLE Retailer(
	Retailer_ID INTEGER PRIMARY KEY,
	Retailer_name TEXT NOT NULL,
	Commodity_ID INTEGER NOT NULL,
	Commodity_price INTEGER NOT NULL,
	FOREIGN KEY (Market_ID) REFERENCES Market (Market_ID)
);

CREATE TABLE Commodity(
	Commodity_ID INTEGER PRIMARY KEY,
	Commodity_name TEXT NOT NULL,
	Commodity_weight INTEGER NOT NULL,
	FOREIGN KEY (Manufacturer_ID) REFERENCES Manufacturer (Manufacturer_ID)
);

CREATE TABLE Sell(
	FOREIGN KEY (Commodity_ID) REFERENCES Commodity (Commodity_ID) PRIMART KEY,
	FOREICN KEY (Retailer_ID) REFERENCES Retailer (Retailer_ID) PRIMART KEY
);

CREATE TABLE Distribute(
	FOREIGN KEY (Jobber_ID) REFERENCES Jobber (Jobber_ID),
	FOREIGN KEY (Retailer_ID) REFERENCES Retailer (Retailer_ID),
	FOREIGN KEY (Commodity_ID) REFERENCES Commodity (Commodity_ID)
);

