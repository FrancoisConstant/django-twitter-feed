import tweepy
from django.conf import settings
from django.db import transaction

from twitter_feed.models import Tweet


class ImportTweets:

    def __init__(self):
        self.consumer_key = settings.TWITTER_FEED_CONSUMER_PUBLIC_KEY
        self.consumer_secret = settings.TWITTER_FEED_CONSUMER_SECRET
        self.o_auth_token = settings.TWITTER_FEED_OPEN_AUTH_TOKEN
        self.o_auth_secret = settings.TWITTER_FEED_OPEN_AUTH_SECRET

    def update_tweets(self):
        raw_tweets = self._get_latest_tweets_from_api()
        tweets = [self._tweepy_status_to_tweet(status=status) for status in raw_tweets]
        self._replace_all_tweets(tweets)

    def _get_latest_tweets_from_api(self):
        """
        http://pythonhosted.org/tweepy/html/index.html
        """
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.o_auth_token, self.o_auth_secret)
        api = tweepy.API(auth)

        return api.user_timeline()

    def _tweepy_status_to_tweet(self, status):
        """
        Fields documentation: https://dev.twitter.com/docs/api/1.1/get/statuses/home_timeline
        """
        tweet = Tweet()
        tweet.published_at = status.created_at
        tweet.content = status.text

        return tweet

    @transaction.commit_manually
    def _replace_all_tweets(self, new_tweets):
        try:
            with transaction.commit_manually():
                Tweet.objects.remove_all()

                for tweet in new_tweets:
                    tweet.save()

                transaction.commit()
        except Exception:
            pass