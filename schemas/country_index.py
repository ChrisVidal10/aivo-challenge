# Schema
from ext import ma

class CountryIndexSchema(ma.Schema):
  
  class Meta:
    fields = ('code', 'code_desc', 'indicator', 'indicator_desc', 'value')


# Init schema
country_index_schema = CountryIndexSchema()
countries_index_schema = CountryIndexSchema(many=True)
