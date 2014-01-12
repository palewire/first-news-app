import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def index():
    csv_path = './static/baltimore-cctv-locations.csv'
    object_list = csv.DictReader(open(csv_path, 'r'))
    return render_template('index.html',
        object_list=object_list,
    )


if __name__ == '__main__':
    app.run( 
        host="0.0.0.0",
        port=8000,
        use_reloader=True,
        debug=True,
    )

