# aivo-challenge
### Repository for Aivo challenge app

1. Initials steps
-- Clone the repository `git clone https://github.com/ChrisVidal10/aivo-challenge.git`
-- Create a virtual environment, `virtualenv env`
-- Activate the virtualenv, `. env/bin/activate`
-- Install all the requirements, `pip install -r requirements.txt`
2. Next step
-- Create the database and fill it with data. 📊 
-- You'll find a little script, please run it, `sh init.sh`. It'll create the database and the table neccesary for load the data into it.
3. Last step
-- Run the command `Flask run` to start the server (http://localhost:5000)
---

### Endpoints

- GET /countryIndex
Return all registries of countries per index and values

- GET /countryIndex?value={Numeric value} 
Return all the registries of countries per default index SW_LIFS and greater than the input value

- GET /countryIndex?value{Numeric value}&index={Index value}
Return all the registries of countries per input index and greater than the input value