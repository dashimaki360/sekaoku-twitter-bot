import tweepy

class SekaokuTwitter():
    def __init__(self):
        # set tweeter key from ENV
        #TODO
        CONSUMER_KEY = ''
        CONSUMER_SECRET = ''
        ACCESS_TOKEN = ''
        ACCESS_SECRET = ''

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def is_retweeted(self, tweet):
        #TODO
        return True

    def is_included_img(self, tweet):
        #TODO
        return True

    def retweet(self, tweet):
        #TODO
        pass

    def save_image(self, tweet):
        #TODO
        if not self.is_included_img(tweet):
            return False
        return True

    def main(self):
        num_tweets = 25
        tweets = self.api.search(q='"#せかいのおくだ"',
                                 lang='ja',
                                 result_type='recent',
                                 count=num_tweets)
        for tweet in tweets:
            if self.is_retweeted(tweet):
                break
            self.save_image(tweet)
            self.retweet(tweet)


if __name__ == '__main__':
    sekaoku_tw = SekaokuTwitter()
    sekaoku_tw.main()

