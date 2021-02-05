# ib-market-data-collector
#### This is a program that collects market data from TWS API. It is modified from the sample code of [TWS API](https://www.interactivebrokers.com.hk/en/index.php?f=45487#tws-api). The whole project initially designed for data extraction of different type of instrument. However, it only supports stock market at the current stage.

# Prerequisites
###1. Interactive Broker Pro account
###2. MariaDB / Mysql Database and client


# Usage
### 1. Installation
```
git clone https://github.com/AlvinTheDeveloper/ib-market-data-collector.git
cd ib-market-data-collector
pip install -r requirements.txt
```

### 2. Config
### 2.1 Run SQL script to create database tables
```mysql -u your_username --host=your_host -p < db_init.sql```
#### 2.2 Rename /config/keyAndConfig.demo.json to /config/keysAndConfig.json
```mv ./config/keysAndConfig.demo.json ./config/keysAndConfig.json```
#### 2.3 Change the database settings.

### 3 Setup watchlist
#### Before the program starts receiving data from API, it fetches watchlist data from the database. You will have to set up the watchlist in the database. My way is to export the watchlist from TWS and import the watchlist data to the database's watchlist table.
#### 3.1 Create a watchlist
#### 3.1.a You can create a watchlist in TWS by following the steps mentioned in [this video](https://www.youtube.com/watch?v=22HfejDRYi0).
#### 3.1.b Once you created a new watchlist, you have to edit the column by following the steps mentioned in [this video](https://www.youtube.com/watch?v=JRW5w3j--Gs)
#### Financial Instrument, Description, and Exchange should be set as same as below:
![Manage columns](doc/Screenshot%202021-01-27%20at%206.27.43%20PM.png "Manage columns")

#### 3.1.c Export your watchlist to the "data" directory. Watch [this video](https://www.youtube.com/watch?v=qOqFhDyNw08) to learn how to export a watchlist.
#### 3.1.d Add the path to CSV file to the array of watchlist_csv property in keysAndConfig.json
#### 3.1.e Run command
```
python3 CsvToDb.py
```

### 4 Run the program
"""
python3 DataCollector.py
"""

 