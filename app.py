from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app) 
# Init migrate
migrate = Migrate(app, db)

# Class/Model

class CountryIndex(db.Model):
    __tablename__ = 'country_index'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100))
    code_desc = db.Column(db.String(100))
    indicator = db.Column(db.String(100))
    indicator_desc = db.Column(db.String(100))
    measure = db.Column(db.String(100))
    measure_desc = db.Column(db.String(100))
    inequality = db.Column(db.String(100))
    inequality_desc = db.Column(db.String(100))
    unit_code = db.Column(db.String(100))
    unit_code_desc = db.Column(db.String(100))
    powercode_code = db.Column(db.String(100))
    powercode_desc = db.Column(db.String(100))
    reference_period = db.Column(db.String(100))
    reference_period_desc = db.Column(db.String(100))
    value = db.Column(db.Float)
    flag_code = db.Column(db.String(100))
    flag_code_desc = db.Column(db.String(100))

    def __init__(self, code, code_desc, indicator, indicator_desc, measure, measure_desc, inequality, inequality_desc, unit_code, 
        unit_code_desc, powercode_code, powercode_desc, reference_period, reference_period_desc, value, flag_code, flag_code_desc):

        self.code = code
        self.code_desc = code_desc
        self.indicator = indicator
        self.indicator_desc = indicator_desc
        self.measure = measure
        self.measure_desc = measure_desc
        self.inequality = inequality
        self.inequality_desc = inequality_desc
        self.unit_code = unit_code
        self.unit_code_desc = unit_code_desc
        self.powercode_code = powercode_code
        self.powercode_desc = powercode_desc
        self.reference_period = reference_period
        self.reference_period_desc = reference_period_desc
        self.value = value
        self.flag_code = flag_code
        self.flag_code_desc = flag_code_desc

# Schema
class CountryIndexSchema(ma.Schema):
  class Meta:
    fields = ('code', 'code_desc', 'indicator', 'indicator_desc','value')


# Init schema
country_index_schema = CountryIndexSchema()
countries_index_schema = CountryIndexSchema(many=True, )

# Create a country per index for developing purposes
@app.route('/countryIndex', methods=['POST'])
def add_country_index():
    code = request.json['code']
    code_desc = request.json['code_desc']
    indicator = request.json['indicator']
    indicator_desc = request.json['indicator_desc']
    measure = request.json['measure']
    measure_desc = request.json['measure_desc']
    inequality = request.json['inequality']
    inequality_desc = request.json['inequality_desc']
    unit_code = request.json['unit_code']
    unit_code_desc = request.json['unit_code_desc']
    powercode_code = request.json['powercode_code']
    powercode_desc = request.json['powercode_desc']
    reference_period = request.json['reference_period']
    reference_period_desc = request.json['reference_period_desc']
    value = request.json['value']
    flag_code = request.json['flag_code']
    flag_code_desc = request.json['flag_code_desc']

    new_country_index = CountryIndex(code, code_desc, indicator, indicator_desc, measure, measure_desc, inequality, inequality_desc, unit_code, 
        unit_code_desc, powercode_code, powercode_desc, reference_period, reference_period_desc, value, flag_code, flag_code_desc)

    db.session.add(new_country_index)
    db.session.commit()

    return country_index_schema.jsonify(new_country_index)

# Get all or by filter
@app.route('/countryIndex', methods=['GET'])
def get_products():
    query_string = request.args
    value = query_string.get('value')
    index = query_string.get('index') if query_string.get(
        'index') else 'SW_LIFS'

    if not value:
        all_country_indexes = CountryIndex.query.all()
    else:
        all_country_indexes = CountryIndex.query.filter(
            (CountryIndex.indicator == index) & (CountryIndex.value > value))

    result = countries_index_schema.dump(all_country_indexes)
    return jsonify(result)

# Run Server
if __name__ == '__main__':
  app.run()
