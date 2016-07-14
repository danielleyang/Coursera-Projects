import sys
import json
import types


def score_dict(sentiment_scores):
    scores = {}  # initialize an empty dictionary
    for line in sentiment_scores:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def generate_state():
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    return states

def score_dict(file):
    scores = {}  # initialize an empty dictionary
    for line in file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def get_location(tweet_file,state_dict):
    #tweets_coordinates = {}
    tweets_place_state = {}
    num_of_unavailable = 0
    for line in tweet_file:
        tweet = json.loads(line)
        #if 'text' in tweet and 'coordinates' in tweet and type(tweet['coordinates']) is not types.NoneType:
            #tweets_coordinates[tweet['text']] = tweet['coordinates']
        if 'text' in tweet and 'place' in tweet and type(tweet['place']) is not types.NoneType:
            if type(tweet['place']['full_name']) is not types.NoneType and 'full_name' in tweet['place']:
                if type(tweet['place']['country']) is not types.NoneType and 'country' in tweet['place']:
                    if tweet['place']['country'] == 'United States':
                        place = tweet['place']['full_name'].split()
                        state = place[-1]
                        tweets_place_state[tweet['text']] = state
        elif 'text' in tweet and 'user' in tweet and type(tweet['user']) is not types.NoneType:
            if type(tweet['user']['location']) is not types.NoneType and 'location' in tweet['user']:
                location = tweet['user']['location'].split(',')
                for sub_locations in location:
                    for states_name in state_dict.keys():
                        if sub_locations == states_name:
                            location_state = sub_locations
                            tweets_place_state[tweet['text']] = location_state
                        elif sub_locations == state_dict[states_name]:
                            location_state = states_name
                            tweets_place_state[tweet['text']] = location_state
            else:
                tweets_place_state[tweet['text']] = 'Not in United States or not available'
                num_of_unavailable += 1
    #print num_of_unavailable #3043 tweets doesn't have a location information
    return tweets_place_state

def get_state_freq(tweet_location):
    state_freq = {}
    for state in tweet_location.values():
        if state in state_freq.keys():
            state_freq[state] += 1;
        else:
            state_freq[state] = 1;
    return state_freq

def get_state_sentiment_scores(scores,tweet_location,state_frequency):
    location_scores = {}
    for tweet in tweet_location.keys():
        sentiment_score = 0
        words = tweet.split()
        for word in words:
            if word in scores:
                sentiment_score = scores[word] + sentiment_score
        state = tweet_location[tweet]
        if state in location_scores.keys():
            location_scores[state] += sentiment_score
        else:
            location_scores[state] = sentiment_score
    for location in location_scores.keys():
        frequency = state_frequency[location]
        location_scores[location] = float (location_scores[location]) / float(frequency)
    sorted_sentiment_scores = sorted([(value, key) for (key, value) in location_scores.items()], reverse=True)
    return sorted_sentiment_scores

def main():
    sentiment_scores = open(sys.argv[1])  #this will be "AFINN-111.txt" file
    tweet_file = open(sys.argv[2]) #this will be "output.txt" living stream tweet file
    scores = score_dict(sentiment_scores)  # save the standard scores and terms into dictionaries rather than in the txt files
    state_dict = generate_state()
    tweet_location = get_location(tweet_file,state_dict) #get all the tweets
    state_frequency = get_state_freq(tweet_location)
    state_sentiment_scores = get_state_sentiment_scores(scores,tweet_location,state_frequency)
    happiest_scores,state = state_sentiment_scores[0]
    print state

if __name__ == '__main__':
    main()
