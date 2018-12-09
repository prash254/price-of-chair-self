__author__ = 'sp'

from src.app import app


app.run(debug=app.config['DEBUG'], port=2558)

