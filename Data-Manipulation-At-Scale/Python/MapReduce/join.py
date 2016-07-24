import MapReduce
import sys

# Problem 2 Implement a relational join as a MapReduce query

mr = MapReduce.MapReduce()

# Part 1 Mapper
def mapper(record):
    # record is a line of records.json; it has a list of 17 variables
    # id: the second element in the list
    # mapper phase returns tuples of (id, the entire content of the record)
    id = record[1]
    mr.emit_intermediate(id, record)

# Part 2 Reducer
def reducer(id, record):
    # id is the id of the contents
    # reducer phase returns tuples of the combinations of two records
    num_content = len(record) # the number of elements in each record
    for i in range(1,num_content):
        total = []
        for element in contents[0]: # attach the order record first
            total.append(element)
        for element in contents[i]: # attach one line_item record after the order record
            total.append(element)
        mr.emit(total)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)