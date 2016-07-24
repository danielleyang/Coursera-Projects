# Description  
This assignment is not use MapReduce to do parallel programming.  
It is simply to train me to think in MapReduce for future programming in MapReduce/HaDoop.   

# Date  
07/18/16 - 07/24/16  

# Usage    
The files used in this assignment can be downloaded here:  
`https://github.com/jenny91515/Coursera-Projects.git`   

After downloading, the files for this project can be found under  
Coursera Projects/Data Manipulation At Scale/Python/MapReduce  

# Tasks
## Problem 1 Create an Inverted index  
Given a set of documents, an inverted index is a dictionary where each word is associated with a list of the document identifiers in which that word appears.
  * (a) Mapper Input  
The input is a 2-element list: [document_id, text], where document_id is a string representing a document identifier and text is a string representing the text of the document. The document text may have words in upper or lower case and may contain punctuation. You should treat each token as if it was a valid word; that is, you can just use value.split() to tokenize the string.  
  * (b) Reducer Input  
 The output should be a (word, document ID list) tuple where word is a String and document ID list is a list of Strings 

  `python inverted_index.py books.json`  

## Problem 2 Implement a relational join as a MapReduce query  
Your MapReduce query should produce the same result as this SQL query executed against an appropriate database.  
`SELECT *`  
`FROM Orders, LineItem`  
`WHERE Order.order_id = LineItem.order_id`  
  * (a) Mapper Input  
Each input record is a list of strings representing a tuple in the database. Each list element corresponds to a different attribute of the table. The first item (index 0) in each record is a string that identifies the table the record originates from. This field has two possible values:  
"line_item" indicates that the record is a line item.  
"order" indicates that the record is an order.  
The second element (index 1) in each record is the order_id. LineItem records have 17 attributes including the identifier string. Order records have 10 elements including the identifier string.
  * (b) Reducer Input  
The output should be a joined record: a single list of length 27 that contains the attributes from the order record followed by the fields from the line item record. Each list element should be a string.    

  `python join.py records.json`  

## Problem 3 Describe a MapReduce algorithm to count the number of friends for each person in a social network   
  * (a) Mapper Input  
Each input record is a 2 element list [personA, personB] where personA is a string representing the name of a person and personB is a string representing the name of one of personA's friends. Note that it may or may not be the case that the personA is a friend of personB.  
  * (b) Reducer Input  
The output should be a pair (person, friend_count) where person is a string and friend_count is an integer indicating the number of friends associated with person.    

  `python friend_count.py friends.json`  

## Problem 4 Implement a MapReduce algorithm to check non-symmetric friend relationships   
  * (a) Mapper Input  
Each input record is a 2 element list [personA, personB] where personA is a string representing the name of a person and personB is a string representing the name of one of personA's friends. Note that it may or may not be the case that the personA is a friend of personB.  
  * (b) Reducer Input  
The output should be all pairs (friend, person) such that (person, friend) appears in the dataset but (friend, person) does not.    

  `python asymmetric_friendships.py friends.json`  
 
## Problem 5 Write a MapReduce query to remove the last 10 characters from each string of nucleotides, then remove any duplicates generated   
  * (a) Mapper Input  
Each input record is a 2 element list [sequence id, nucleotides] where sequence id is a string representing a unique identifier for the sequence and nucleotides is a string representing a sequence of nucleotides.  
  * (b) Reducer Input  
The output from the reduce function should be the unique trimmed nucleotide strings.  

  `python unique_trims.py dna.json`  

## Problem 6 Design a MapReduce algorithm to compute the matrix multiplication A x B   
  * (a) Mapper Input  
The input to the map function will be a row of a matrix represented as a list. Each list will be of the form [matrix, i, j, value] where matrix is a string and i, j, and value are integers. The first item, matrix, is a string that identifies which matrix the record originates from. This field has two possible values: "a" indicates that the record is from matrix A and "b" indicates that the record is from matrix B.  
  * (b) Reducer Input  
The output from the reduce function will also be a row of the result matrix represented as a tuple. Each tuple will be of the form (i, j, value) where each element is an integer.  

  `python multiply.py matrix.json`  
  

