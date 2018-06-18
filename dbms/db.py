import sqlite3
import csv

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db_schema():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))

@click.command('init-schema')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db_schema()
    click.echo("Initialized the database.")

def insert_default():
    db = get_db()
    name = ["Sell", "Distribute", "Retailer", "Manufacturer", "Jobber", "Market", "Commodity"]

    for i, table in enumerate(name):
        with current_app.open_resource("./default_data/" + table + ".csv", 'r') as f:
            if i <= 1:
                times = i+1
            else:
                times = 3
            update = "INSERT INTO " + table + " VALUES (" + "?, "*times + "?)"
            next(f, None)
            reader = csv.reader(f)
            for row in reader:
                db.execute(update, row)
            db.commit()

@click.command('init-data')
@with_appcontext
def init_db_data_command():
    """Insert default value into tables"""
    init_db_schema()
    insert_default()
    get_db().close()
    click.echo("Data is prepared!")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(init_db_data_command)
