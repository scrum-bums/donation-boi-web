# Getting setup locally
1. Install Python 3.6+, pip, and pipenv (`pip install pipenv`)
2. Run `pipenv` to create a virtual environment
3. Run `pipenv install`
4. Run `python manage.py migrate`
5. Set the environment variables in `.env.example` and rename the file to `.env`
5. Start the Django server locally using `python manage.py runserver 8000`
6. Access the web app by visiting [localhost:8000](localhost:8000) in your web browser.

# Deploying
- The `master` branch auto-deploys to https://donation-boi-staging.herokuapp.com/
- To deploy to the production site, access the Heroku pipeline and promote the staging build to production