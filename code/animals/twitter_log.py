# twitter_log.py
# --------------
# by Chris Proctor

# TwitterLog acts as a simple log that posts updates to Twitter.
# Requires the python-twitter library, which you can install with:
# sudo pip install python-twitter

# To use TwitterLog, you need OAUTH keys for your account and for the 
# app--the easiest way to do this is to go to apps.twitter.com 
# and create a new app.

# If you want to try it out, here are some keys that will work
# for the demo account @forest_warden:
# consumer_key: "HVU3ROf8ICM4Ye5fbYc0o7EN0"
# consumer_secret: "lbqMC6c7vxyRz8k6GA4IZHuusN9NvvieIGNxvmVASlRBQ01f7e"
# access_key: "3241290962-Srzd64RZIARwbUq6SBLOS2b1A3zbYPWxAA0YrYk"
# access_secret: "wE6TD6vXoLpBQ03ovNvSiyrnjS6CnFYuZWD05A0EMjBNB"

# Here's an example of a forest connected to Twitter:
#   from forest import Forest
#   from twitter_log import TwitterLog
#   tweeter = TwitterLog(
#       "HVU3ROf8ICM4Ye5fbYc0o7EN0", 
#       "lbqMC6c7vxyRz8k6GA4IZHuusN9NvvieIGNxvmVASlRBQ01f7e" ,
#       "3241290962-Srzd64RZIARwbUq6SBLOS2b1A3zbYPWxAA0YrYk", 
#       "wE6TD6vXoLpBQ03ovNvSiyrnjS6CnFYuZWD05A0EMjBNB"
#   )
#   forest = Forest(log=tweeter)

from twitter import Api

class TwitterLog:

    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50
    
    def __init__(self, consumer_key, consumer_secret, access_key, access_secret, log_level=None):
        self.log_level = log_level or self.INFO
        self.api = Api(consumer_key, consumer_secret, access_key, access_secret)
        if not self.api.VerifyCredentials():
            raise ValueError("Could not log in to Twitter with the keys provided.")

    def debug(self, message):
        self.log(message, self.DEBUG)

    def info(self, message):
        self.log(message, self.INFO)
    
    def warning(self, message):
        self.log(message, self.WARNING)

    def error(self, message):
        self.log(message, self.ERROR)

    def critical(self, message):
        self.log(message, self.CRITICAL)

    def log(self, message, level):
        "Post the first 140 characters if the level is at least the log level"
        if level >= self.log_level:
            self.api.PostUpdate(message[:140])
