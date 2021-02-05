import json
import datetime
import csv
from lib import db

conn = db.DB()

with open('config/keysAndConfig.json') as f:
    keysAndConfig = json.load(f)


def importWatchListData():
    for path in keysAndConfig['path']['watchlist_csv']:
        with open(path, newline='') as csv_file:
            watchlist_reader = csv.reader(csv_file, delimiter=',')
            l = list()
            for idx, row in enumerate(watchlist_reader):
                l.append(row)
                if idx > 0:
                    ibDescription = row[1].lower()
                    instrType = None
                    if 'stock' in ibDescription:
                        instrType = 'STK'
                    elif 'futures' in ibDescription:
                        instrType = 'FUT'
                    elif 'options' in ibDescription:
                        instrType = 'OPT'
                    elif 'commodity' in ibDescription:
                        instrType = 'CMDTY'

                    conn.query(
                        'INSERT INTO algo_trade.watchlist(symbol,instr_type,exchange) VALUES (%s,%s,%s) ON DUPLICATE KEY UPDATE symbol=VALUES(symbol),instr_type=VALUES(instr_type),exchange=VALUES(exchange);',
                        [row[0].split(" ")[0], instrType, row[2]])
                    conn.commit()


if __name__ == "__main__":
    importWatchListData()
