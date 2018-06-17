import os
import pprint

from flask import Flask
from flask import render_template, session
from flask_bootstrap import Bootstrap


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'dbms.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from dbms.db import init_db_schema, insert_default, get_db

    from . import db
    db.init_app(app)

    from . import button
    app.register_blueprint(button.bp)

    # initilize flask_bootstrap
    bootstrap = Bootstrap(app)

    print("")
    pprint.pprint(app.url_map)
    print("")

    @app.route('/')
    def index():
        if session.get('insert') is None:
            session['insert'] = 0
        content = get_db().execute("SELECT * FROM Commodity").fetchall()
        return render_template('enter.html', table='Commodity', content=content)

    return app
