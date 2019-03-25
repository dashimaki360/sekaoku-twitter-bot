# -*- coding:utf-8 -*-
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
        PROXY = os.environ['PROXY']
        if not PROXY:
            PROXY = None

        logger.debug("create api obj")
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth, proxy=PROXY)
        logger.debug("create api obj")

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
            logger.error("already retweeted {}".format(tweet.id))

    def favorite(self, tweet):
        try:
            self.api.create_favorite(tweet.id)
            logger.info("favorited " + tweet.id)
        except:
            logger.error("already favorited {}".format(tweet.id))

    def save_image(self, tweet):
        logger.debug("func: save_image")
        #TODO
        logger.info("STILL NOT DEVELOPMENT")
        return True

    def run(self):
        logger.debug("start run")

        tweets = self.api.search(q='"#せかいのおくだ"',
                                 result_type='recent',
                                 count=100)
        logger.debug(len(tweets))

        for tweet in tweets:
            logger.debug(tweet)
            if self.is_retweeted(tweet):
                logger.info("this tweet is already retweeted break")
                break
            if self.is_included_img(tweet):
                self.save_image(tweet)
            self.retweet(tweet)
            self.favorite(tweet)
        logger.debug("end of run")


def main():
    sekaoku_tw = SekaokuTwitter()
    sekaoku_tw.run()


if __name__ == '__main__':
    main()

