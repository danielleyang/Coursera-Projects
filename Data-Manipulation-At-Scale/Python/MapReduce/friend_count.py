import MapReduce
import sys

# Problem 3 Describe a MapReduce algorithm to count the number of friends for each person in a social network

mr = MapReduce.MapReduce()

# Part 1 Mapper
def mapper(record):
    # record is a line of friends.json
    # personA is the key
    # value is always be 1
    # mapper returns tuples of (personA, 1)
    personA = record[0]
    mr.emit_intermediate(personA, 1)

# Part 2 Reducer
def reducer(personA, list_of_ones):
    # personA is the key which is the name of the person
    # reducer phase returns tuples of (personA, num_friends)
    num_friends = 0
    for v in list_of_ones: # sum up all the ones so we know the total number of friends
        num_friends += v
    mr.emit((personA, num_friends))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
