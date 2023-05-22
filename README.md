# Maxacraft Billing

---

## To run this app:

Create `.env` file and copy all from `.env.example` to it. Set your own values (for now - just copy all from `.env.example`)

Install pipenv:
```
$ pip install --user pipenv
```

Then - integrate it to pycharm https://www.jetbrains.com/help/pycharm/pipenv.html

After integration:

```
$ sh ./run-env.sh
$ pipenv install
$ sh ./run-server.sh
```


## App Structure

`./maxacraft_billing/*` - main app folder

`./maxacraft_billing/settings.py` - config file with database config and e.t.c

`./maxacraft_billing/urls.py` - core urls file, with path configurations

`./maxacraft_billing/api` - api folder

`./maxacraft_billing/api/account` - api entity core folder

`./maxacraft_billing/api/account/models` - api entity database models

`./maxacraft_billing/api/account/controllers` - api entity controllers

`./maxacraft_billing/api/account/controllers/get_account.py` - example api controller with @api_view decorator

`./maxacraft_billing/api/account/views` - api entity views for api

`./maxacraft_billing/api/account/views/get_account.py` - example api controller with class notation, not recommended

`./maxacraft_billing/api/account/urls.py` - example url mapping file for account entity

