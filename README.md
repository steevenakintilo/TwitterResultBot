# TwitterResultBot

A bot that will take a screenshot of your recent mention + direct message and will send it to your discord server to see if you have won one a giveaway
This bot is really usefull if you have several bot and you don't want to check if you won somethig by hand

## Requirements

To make the code work you will need to have Python and Pip installed in your computer

Link to download python: https://www.python.org/downloads/

Link to download pip: https://pip.pypa.io/en/stable/installation/

You also need to download google chrome

Link to download google chrome: https://www.google.com/intl/fr_fr/chrome/

Download all the modules required for the bot to work using this command:

```bash
    pip install -r requirement.txt
```

Then make a weebhook and put the url to the webhook_url.txt file
Here is how to do a weenhook:https://www.svix.com/resources/guides/how-to-make-webhook-discord/

To start the bot just do

```bash
    python main.py
```
## Configuration file
To add account just fill account_username and account_password with the username and password of the account you want to add

```yml
#Account info write the username of all your account
account_username:
  - "test1234"
  - "test4444"
  - "test0000"

#Account info write the password of all your account
account_password:
  - "twitter1234"
  - "twitter4444"
  - "twitter0000"
```
