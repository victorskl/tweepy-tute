import json
from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')

consumer_key = parser['twitter']['consumer_key']
consumer_secret = parser['twitter']['consumer_secret']
access_token = parser['twitter']['access_token']
access_token_secret = parser['twitter']['access_token_secret']

locations = json.loads(parser['filter']['locations'])
track = json.loads(parser['filter']['track'])


def mksample():
    parser['twitter']['consumer_key'] = 'consumer_key'
    parser['twitter']['consumer_secret'] = 'consumer_secret'
    parser['twitter']['access_token'] = 'access_token'
    parser['twitter']['access_token_secret'] = 'access_token_secret'

    with open('config.ini.sample', 'w') as sample:
        parser.write(sample)


def main():
    mksample()


if __name__ == '__main__':
    main()
