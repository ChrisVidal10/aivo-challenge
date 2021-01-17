from .country_index import CountryIndexApi

def initialize_routes(api):
    api.add_resource(CountryIndexApi, '/countryIndex')
