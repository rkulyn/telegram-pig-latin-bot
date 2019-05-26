## Telegram Pig Latin Translation Bot
https://t.me/pig_latin_bot  
**@pig_latin_bot**

### Dependencies

**Python 3.6** and above.  
**python-telegram-bot** 


### Running program locally
`python3 app.py`

### Deploying on Heroku
`heroku login`  
`git push heroku master`  
`heroku ps:scale pig-bot=1`  

### Environment variables
**ADMIN_ID** -  Admin user ID. Got from telegram.  
**BOT_TOKEN** - Telegram bot access token. Got from botfather.  
**ENV** - "dev", "prod" set proper config for specified environment.
