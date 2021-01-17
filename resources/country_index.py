from flask import jsonify, request, make_response
from models.country_index import CountryIndex
from schemas.country_index import country_index_schema, countries_index_schema
from flask_restful import Resource
from ext import db
from resources.exceptions import ValidationError, exceptions

DEFAULT_INDEX = 'SW_LIFS'

class CountryIndexApi(Resource):
    
    # Get all or by filter
    def get(self):
        query_string = request.args
        value = query_string.get('value')
        index = query_string.get('index') if query_string.get(
            'index') else DEFAULT_INDEX

        if not value:
            all_country_indexes = CountryIndex.query.all()
        else:
            self.validation_get_input(*[("value", value, float), ("index", index, str)])
            all_country_indexes = CountryIndex.query.filter(
                (CountryIndex.indicator == index) & (CountryIndex.value > value))

        result = countries_index_schema.dump(all_country_indexes)
        
        if result:
            return jsonify({"response": result})
        else:
            return make_response(jsonify({"response": "data not found"}), 404)

    def validation_get_input(self, *args):
        try:
            for i in args:
                i[2](i[1])
        except Exception:
            raise ValidationError(i)
