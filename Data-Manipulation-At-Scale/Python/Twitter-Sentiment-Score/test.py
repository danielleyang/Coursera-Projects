
import json

file = open("output.txt")

for line in file:
    values = json.loads(line)
    print values
#tweets_text.append(json.loads(line)['text'].encode('utf-8'))