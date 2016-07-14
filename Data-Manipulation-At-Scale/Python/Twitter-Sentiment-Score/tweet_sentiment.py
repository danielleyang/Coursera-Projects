import sys
import json

def score_dict(file):
    scores = {}  # initialize an empty dictionary
    for line in file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def get_text(tweet_file):
    tweets_text = []
    for line in tweet_file:
        values = json.loads(line)
        if 'text' in values:
            tweets_text.append(json.loads(line)['text'])
    return tweets_text

def get_score(scores, tweet_texts):
    for tweet in tweet_texts:
        sentiment_score = 0
        words = tweet.split()
        for word in words:
            if word in scores:
                sentiment_score = scores[word] + sentiment_score
        print sentiment_score

def main():
    standard_file = open(sys.argv[1])  #this will be "AFINN-111.txt" file
    tweet_file = open(sys.argv[2]) #this will be "output.txt" file
    scores = score_dict(standard_file) #save the standard scores and terms into dictionaries rather than in the txt files
    tweet_texts = get_text(tweet_file) #get all the tweets
    get_score(scores, tweet_texts) #get the sentiment score and print out sentiment score


if __name__ == '__main__':
    main()


"""
original file
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)
"""