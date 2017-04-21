import tweepy
from tweepy import Stream

import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)


def resting():
    api = tweepy.API(auth)
    public_tweets = api.home_timeline()

    user = api.me()
    print('Name:     {}'.format(user.name))
    print('Location: {}'.format(user.location))
    print('Friends:  {}'.format(user.friends_count))
    print('Timeline: {}'.format(len(public_tweets)))

    print('-' * 100)

    for tweet in public_tweets:
        print(tweet.text.encode("utf-8"))


class StdOutStreamListener(tweepy.StreamListener):
    def on_data(self, raw_data):
        print(raw_data)

    def on_error(self, status_code):
        print(status_code)


def streaming():
    l = StdOutStreamListener()
    s = Stream(auth, l)
    s.filter(locations=config.locations, track=config.track)


def main():
    print('RESTful API')
    print('=' * 100)

    resting()

    print(' ')
    print('=' * 100)
    print('Streaming has started... Ctrl+C in console or press Stop button on PyCharm Run')
    print('=' * 100)

    streaming()


if __name__ == '__main__':
    main()
