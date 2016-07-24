import MapReduce
import sys

# Problem 4 Implement a MapReduce algorithm to check non-symmetric friend relationships
mr = MapReduce.MapReduce()

# Part 1 Mapper
def mapper(record):
    # record is a line of friends.json
    # person_1 is the key
    # mapper returns tuples of (person_1, person_2)
    person_1 = record[0]
    person_2 = record[1]
    mr.emit_intermediate(person_1, person_2)

# Part 2 Reducer
def reducer(person, list_of_person_friends):
    # key: person
    # value: list_of_person_friends
    # reducer returns tuples of (person, not friend with the person)
    for friend in list_of_person_friends: # for each friend in the list of person friends
        if friend not in mr.intermediate.keys() or person not in mr.intermediate[friend]: # if they are not friends with each other
            mr.emit((person, friend))
            mr.emit((friend,person))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
