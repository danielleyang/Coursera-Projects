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
    tweet_scores = {}
    for tweet in tweet_texts:
        sentiment_score = 0
        words = tweet.split()
        for word in words:
            if word in scores:
                sentiment_score = scores[word] + sentiment_score
        tweet_scores[tweet] = sentiment_score
    return tweet_scores

def new_word_list(scores, tweet_texts):
    new_word = []
    for tweet in tweet_texts:
        words = tweet.split()
        for word in words:
            if word in scores:
                pass
            else:
                new_word.append(word)
    return new_word

def new_word_score(tweet_texts,tweet_scores,new_words):
    for new_word in new_words:
        positive = 0
        negative = 0
        total = 0
        for tweet in tweet_texts:
            if new_word in tweet:
                if tweet_scores[tweet]> 0:
                    positive += 1
                else:
                    negative +=1
                total += 1
        new_word_score = (float(positive - negative))/float(total)
        print new_word, ' ', new_word_score

def main():
    standard_file = open(sys.argv[1])  #this will be "AFINN-111.txt" file
    tweet_file = open(sys.argv[2]) #this will be "output.txt" file
    scores = score_dict(standard_file) #save the standard scores and terms into dictionaries rather than in the txt files
    tweet_texts = get_text(tweet_file) #get all the tweets
    tweet_scores = get_score(scores, tweet_texts) #get the sentiment score and print out sentiment score
    new_words = new_word_list(scores, tweet_texts)
    new_word_score( tweet_texts,tweet_scores,new_words)


if __name__ == '__main__':
    main()
