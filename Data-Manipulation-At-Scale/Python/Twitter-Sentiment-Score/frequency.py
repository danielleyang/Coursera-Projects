import sys
import json
import collections

def get_text(tweet_file):
    tweets_text = []
    for line in tweet_file:
        values = json.loads(line)
        if 'text' in values:
            tweets_text.append(json.loads(line)['text'].encode('utf-8'))
    return tweets_text

def get_words(tweet_texts):
    word_list = []
    for tweet in tweet_texts:
        words = tweet.split()
        for word in words:
            word_list.append(word)
    return word_list

def count_frequency(words):
    counter = collections.Counter(words)
    total_frequency = 0
    for frequency in counter.values():
        total_frequency = total_frequency + frequency
    for term, frequency in counter.items():
        print term, ' ', float(frequency)/float(total_frequency)

def main():
    tweet_file = open(sys.argv[1]) #this will be "output.txt" file; the file you want to count the frequency words
    tweet_texts = get_text(tweet_file)
    words = get_words(tweet_texts) #save all the words into a list
    count_frequency(words)

if __name__ == '__main__':
    main()
