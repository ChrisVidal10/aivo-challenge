from ext import db

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
