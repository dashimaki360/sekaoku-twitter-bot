import os
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

import tweepy

logger = getLogger("sekaoku_bot")
formatter = Formatter('%(asctime)s %(name)s %(funcName)s [%(levelname)s]: %(message)s')
handler = StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(DEBUG)


class SekaokuTwitter(object):
    def __init__(self):
        logger.debug("SekaokuTwetter class init")
        self.USER_ID = 'sekaoku1'

        # set tweeter key from ENV
        CONSUMER_KEY = os.environ['CONSUMER_KEY']
        CONSUMER_SECRET = os.environ['CUNSUMER_SECRET']
        ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
        ACCESS_SECRET = os.environ['ACCESS_SECRET']

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def is_retweeted(self, tweet):
        logger.debug("func: is retweeted")
        return tweet.retweeted

    def is_included_img(self, tweet):
        logger.debug("func: is included img")
        return "media" in tweet.entities

    def retweet(self, tweet):
        logger.debug("func: retweet")
        try:
            self.api.retweet(tweet.id)
            logger.info("retweeted " + tweet.id)
        except:
            logger.info("already retweeted " + tweet.id)

    def favorite(self, tweet):
        try:
            self.api.create_favorite(tweet.id)
            logger.info("favorited " + tweet.id)
        except:
            logger.info("already favorited " + tweet.id)

    def save_image(self, tweet):
        logger.debug("func: save_image")
        #TODO
        logger.info("STILL NOT DEVELOPMENT")
        return True

    def run(self):
        num_tweets = 25  # magic number. if tweet a lot please increment
        tweets = self.api.search(q='"#せかいのおくだ"',
                                 lang='ja',
                                 result_type='recent',
                                 count=num_tweets)
        for tweet in tweets:
            logger.debug(tweet)
            if self.is_retweeted(tweet):
                break
            if self.is_included_img(tweet):
                self.save_image(tweet)
            self.retweet(tweet)


def main():
    sekaoku_tw = SekaokuTwitter()
    sekaoku_tw.run()


if __name__ == '__main__':
    main()

