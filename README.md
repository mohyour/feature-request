# Flask Microblog

### Setup
- Create a virtual environmnet
- Activate virtuall environment
- Install requirements - `pip install -r requirements.txt`
- Create .flaskenv file and populate:

  .flaskenv example:
  ```
  export FLASK_APP=main.py
  export SECRET_KEY=<secret>
  export DATABASE_URI=<database_uri>
  ```

Database Migration

`flask db init` - creates database migration folder
`flask db migrate` - Generates automatic migration script
`flask db upgrade` - Apply database migration

Start the app using `flask run`


### Test and Coverage
cd into the tests directory - `cd tests`
- Run test with `python test.py`
- Run coverage with `coverage run test.py` to run the test and gather data
- Use coverage report to report on the results - `coverage report -m`
- For html presentation, run `coverage html`. Notice the htmlcov folder



