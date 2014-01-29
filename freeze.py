from flask_frozen import Freezer
from app import app, csv_list


app.config['FREEZER_RELATIVE_URLS'] = True
freezer = Freezer(app)


@freezer.register_generator
def detail():
    for row in csv_list:
        yield {'number': row['number']}


if __name__ == '__main__':
    freezer.freeze()
