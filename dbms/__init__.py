import os
import pprint

from flask import Flask
from flask import render_template
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

    content = list()
    for x in range(101):
        ran = dict()
        ran['id'] = x
        ran['name'] = x * 100
        ran['score'] = x * 15
        ran['grade'] = x
        ran['number'] = x * 3
        content.append(ran)

    @app.route('/')
    def index():
        return render_template('enter.html', content=content)

    from . import button
    app.register_blueprint(button.bp)

    # initilize flask_bootstrap
    bootstrap = Bootstrap(app)

    print("")
    pprint.pprint(app.url_map)
    print("")

    return app
