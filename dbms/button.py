from flask import Blueprint, render_template, request
import pprint

bp = Blueprint('button', __name__)

@bp.route('/select/<complex>')
def select_btn():
    return render_template('select.html')

@bp.route('/delete')
def delete_btn():
    return render_template('delete.html')

@bp.route('/insert')
def insert_btn():
    return render_template('insert.html')

@bp.route('/update')
def update_btn():
    return render_template('update.html')

@bp.route('/sql_mode', methods=('GET', 'POST'))
def sql_btn():
    if request.method == 'POST':
       query = request.form['sql']
       print("")
       print(query)
       print("")
       pprint.pprint(query)
       print("")
       sql = query.split('\n')
       return render_template('sql.html', sql=sql)
    return render_template('sql.html', sql="")
