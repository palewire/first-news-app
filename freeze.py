from flask_frozen import Freezer
from app import app, csv_list
freezer = Freezer(app)
app.config['FREEZER_RELATIVE_URLS'] = True


@freezer.register_generator
def detail():
    for row in csv_list:
        yield {'number': row['id']}


if __name__ == '__main__':
    freezer.freeze()
