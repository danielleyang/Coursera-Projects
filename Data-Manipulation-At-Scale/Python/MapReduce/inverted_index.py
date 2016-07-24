import MapReduce
import sys

# Problem 1 Create an Inverted index

mr = MapReduce.MapReduce()

# Part 1 Mapper
def mapper(record):
    # record is a line of books.json
    # it has format [document_name, contents_of_that_document]
    # mapper phase returns tuples of (word, document_id)
    document_name = record[0]
    document_contents = record[1]
    words = document_contents.split() # assume all the tokens are separeted by space
    for w in words:
        mr.emit_intermediate(w, document_name) # will generate dictionaries; key is the word; values are the lists of ducument names contain this word

# Part 2 Reducer
def reducer(word, list_of_document_names):
    # word is the key
    # list_of_ducument_names: [document1, document2, document3...]
    # reducer phase returns tuples of (word, list_of_documents_names)
    total_names = []
    for docu in list_of_document_names:
        if docu not in total: # remove the duplicates document names
            total_names.append(docu)
    mr.emit((word, total_names)) # will print out all the tuples

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)