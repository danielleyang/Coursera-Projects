import sys
import json
import types
import collections

def get_hashtags(tweet_file):
    hashtags = []
    for line in tweet_file:
        tweet = json.loads(line)
        if 'entities' in tweet and type(tweet['entities']) is not types.NoneType:
            if 'hashtags' in tweet['entities'] and type(tweet['entities']['hashtags']) is not types.NoneType:
                for elements in tweet['entities']['hashtags']:
                    if 'text' in elements.keys():
                        hashtags.append(elements['text'])
    return hashtags

def get_top_ten(hashtags):
    count = collections.Counter(hashtags)
    sort_count = sorted([(value, key) for (key, value) in count.items()], reverse=True)
    for items in sort_count[0:10]:
        frequency,hashtag = items
        print hashtag, ' ', frequency

def main():
    tweet_file = open(sys.argv[1]) #this will be "output.txt" living stream tweet file
    hashtags = get_hashtags(tweet_file)
    get_top_ten(hashtags)

if __name__ == '__main__':
    main()
