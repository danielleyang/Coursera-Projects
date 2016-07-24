import MapReduce
import sys

# Problem 5 Write a MapReduce query to remove the last 10 characters from each string of nucleotides, then remove any duplicates generated

mr = MapReduce.MapReduce()

# Part 1 Mapper
def mapper(record):
    # record is a line of dna.json
    # key: sequence id
    # value: trimmed dna nucleotides
    # mapper returns tuples of (sequence_id, trimmed nucleotide)
    sequence_id = record[0]
    nucleotides = record[1]
    nucleotides_trim = nucleotides[:-10]
    mr.emit_intermediate(nucleotides_trim,sequence_id) # we want the unqiue trimmed nucleotides; therefore nucleotides are used as the key

# Part 2 Reducer
def reducer(nucleotides_trim,sequence_id):
    # reducer returns the trimmed nucleotide
    mr.emit(nucleotides_trim)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
