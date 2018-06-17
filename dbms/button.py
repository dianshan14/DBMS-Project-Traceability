from flask import Blueprint, render_template, request, session, flash
import pprint
from dbms.db import get_db, init_db_schema, insert_default

bp = Blueprint('button', __name__)

@bp.route('/select/<advance>')
def select_btn(advance):
    query_collection = dict()
    query_collection['select'] = ["SELECT *", "FROM Commodity", "WHERE (Commodity_ID%2 == 0)"]
    query_collection['in'] = ["SELECT Commodity_name, Retailer_name, Commodity_price", "FROM Commodity, Sell, Retailer", "WHERE Commodity.Commodity_ID=Sell.Commodity_ID AND Sell.Retailer_ID=Retailer.Retailer_ID AND", "Commodity.Commodity_ID IN ( SELECT Sell.Commodity_ID FROM Sell )"]
    query_collection['not_in'] = ["SELECT Commodity_name", "FROM Commodity", "WHERE Commodity_ID NOT IN ( SELECT Sell.Commodity_ID", "FROM Sell )"]
    query_collection['exists'] = ["SELECT Manufacturer_name, Commodity_ID, amount", "FROM Manufacturer", "WHERE EXISTS ( SELECT * FROM Commodity WHERE Manufacturer.Commodity_ID=Commodity.Commodity_ID)", "ORDER BY Commodity_ID"]
    query_collection['not_exists'] = ["SELECT Commodity_name", "FROM Commodity", "WHERE NOT EXISTS ( SELECT * FROM Manufacturer WHERE Manufacturer.Commodity_ID=Commodity.Commodity_ID )"]
    query_collection['count'] = ["SELECT count(Commodity_weight)", "FROM Commodity", "WHERE (Commodity_ID%2 == 1)"]
    query_collection['sum'] = ["SELECT sum(Commodity_weight)", "FROM Commodity"]
    query_collection['max'] = ["SELECT max(Commodity_weight)", "FROM Commodity"]
    query_collection['min'] = ["SELECT min(Commodity_weight)", "FROM Commodity"]
    query_collection['avg'] = ["SELECT Manufacturer_ID, avg(Commodity_weight)", "FROM Commodity", "GROUP BY Manufacturer_ID", "ORDER BY avg(Commodity_weight)"]
    query_collection['having'] = ["SELECT Manufacturer_ID, avg(Commodity_weight), sum(Commodity_weight)", "FROM Commodity", "GROUP BY Manufacturer_ID", "HAVING COUNT(Manufacturer_ID)>1"]
    db = get_db()
    sql = query_collection[advance]
    content = db.execute(
        " ".join(sql)
    ).fetchall()
    print(content)
    return render_template('select.html', advance=advance, sql=sql, content=content)

@bp.route('/delete')
def delete_btn():
    db = get_db()
    sql = ["DELETE FROM Commodity", "WHERE Commodity_ID>65310"]
    db.execute(
        " ".join(sql)
    )
    db.commit()
    content = db.execute("SELECT * FROM Commodity").fetchall()
    session['insert'] = 0
    return render_template('delete.html', sql=sql, content=content)

@bp.route('/insert')
def insert_btn():
    db = get_db()
    sql = ["INSERT INTO Commodity", "VALUES (65316, '我是被新增的', 99999, 15)"]
    if not has_inserted():
        db.execute(
            " ".join(sql)
        )
        db.commit()
        session['insert'] = 1
    content = db.execute("SELECT * FROM Commodity").fetchall()
    return render_template('insert.html', sql=sql, content=content)

@bp.route('/update')
def update_btn():
    db = get_db()
    sql = ["UPDATE Commodity", "SET Commodity_weight=Commodity_weight*1.3"]
    res = db.execute(
        " ".join(sql)
    )
    db.commit()
    print(res)
    content = db.execute("SELECT * FROM Commodity").fetchall()
    return render_template('update.html', sql=sql, content=content)

@bp.route('/sql_mode', methods=('GET', 'POST'))
def sql_btn():
    content = None
    sql = None
    if request.method == 'POST':
        db = get_db()
        query = request.form['sql']
        query = "\n".join(query.splitlines())
        #print(query)
        #pprint.pprint(query)
        sql = query.split('\n')

        print("")

        try:
            if sql[0].split(" ")[0].upper() == "SELECT":
                print("{}".format(" ".join(sql)))
                content = db.execute(" ".join(sql)).fetchall()
            else:
                print('{}'.format(" ".join(sql)))
                db.execute(" ".join(sql))
                db.commit()
        except BaseException as e:
            content = None
            print(str(e))
            flash(str(e))

        print("")
    return render_template('sql.html', sql=sql, content=content)

@bp.route('/reset')
def reset_btn():
    init_db_schema()
    insert_default()
    content = get_db().execute("SELECT * FROM Commodity").fetchall()
    print('\033[94m'+"Reset success!" + '\033[0m')
    session['insert'] = 0
    return render_template('enter.html', table='Commodity', content=content)

@bp.route('/tables/<table>')
def table_btn(table):
    content = get_db().execute("SELECT * FROM " + table).fetchall()
    return render_template('enter.html', table=table, content=content)

def has_inserted():
    if session.get('insert') == 1:
        return True
    else:
        return False
