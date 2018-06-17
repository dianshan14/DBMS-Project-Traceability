import sqlite3
import csv

db = sqlite3.connect("dbms.sqlite")
db.row_factory = sqlite3.Row

result = db.execute(
        "SELECT Retailer_ID, Retailer_name, Commodity_ID, Commodity_price"
        " FROM Retailer"
        " WHERE Retailer_ID>1005"
        ).fetchall()

for res in result:
    print(res["Retailer_ID"])

db.close()
