# stock-alerts

This application is designed to help you moniter your stock portfolio and alert you to any under-performers in your portfolio.

## setup instructions
first dowload our repo and navigate there using your command line.

```sh
cd ~/Desktop/stock-alerts
```

create a virtual environment with the packages and modules you will need to run our app

```sh
conda create -n stock-alerts-env python=3.7 # (first time only)
conda activate stock-alert-env
```

after creating this environment, go ahead and install all the packages found in our "requirements.txt" file

```sh
pip install -r requirements.txt
```

### env needs
    you will need the following in your .env file
    ALPHAVANTAGE_API_KEY= ""
    SENDGRID_API_KEY=""
    MY_EMAIL_ADDRESS=""
    MY_NAME=""

## running the app

at this point you should be able to run our application without any hiccups. We recommend that you create a list of all your stock tickers before beginning.

our app functions through sending you an email based off of the stocks that you have added to the data base. To begin the process of creating your database use the update file.

```sh
python app/update.py
```

This will ask you whether you would like to add or delete a stock from your portfolio. Based on your choice, you will be able to carry either of them out.

Once you have selected your action please input your stock's ticker symbol to add it to the csv data base.

After this please update your email preferences in the .env file so you can successfully send yourself an email.

Once you have added all of your stocks you can run the app through 

```sh
python app/stock_alerts.py
```

This will send an email to your indicated account with an indication of how many stocks are under-performing along with an excel attachment that provides further data.

If you would like to make this a daily email we recommend creating a heroku account and set the time sequence to daily.

Enjoy the app.