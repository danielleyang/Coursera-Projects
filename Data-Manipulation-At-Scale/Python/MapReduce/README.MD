# Description  
This assignment is not use MapReduce to do parallel programming.  
It is simply to train me to think in MapReduce for future programming in MapReduce/HaDoop.   

# Date  
07/18/16 - 07/24/16  

# Usage    
The files used in this assignment can be downloaded here:  
`https://github.com/jenny91515/Coursera-Projects.git`   
After downloading, the files for this project can be found under Coursera Projects/Data Manipulation At Scale/Python/MapReduce  

# Tasks Break Down   
All of the SQL queries and its results are under this folder  
## Part I 
  * (a) SELECT: Write a query that is equivalent to the following relational algebra expression.   
        σdocid=10398_txt_earn(frequency)  
        `cat part_a.sql`  

  * (b) SELECT project: Write a SQL statement that is equivalent to the following relational algebra expression.  
        πterm(σdocid=10398_txt_earn and count=1(frequency))    
        `cat part_b.sql`  

  * (c) UNION: Write a SQL statement that is equivalent to the following relational algebra expression.  
        πterm(σdocid=10398_txt_earn and count=1(frequency)) U πterm(σdocid=925_txt_trade and count=1(frequency))  
        `cat part_c.sql`  

  * (d) COUNT: Write a SQL statement to count the number of unique documents containing the word "law" or containing the word "legal" (If a document contains both law and legal, it should only be counted once)    
        `cat part_d.sql`   

  * (e) BIG DOCUMENTS Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms.  
        `cat part_e.sql`  

  * (f) TWO WORDS: Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'.  
        `cat part_f.sql`  

## Part II 
  * (g) MATRIX MULTIPLY: Express A X B as a SQL query, referring to the class lecture for hint  
        `cat part_g.sql`  

## Part III  
  * (h) SIMILARITY MATRIX: Write a query to compute the similarity matrix DDT.  
        `cat part_h.sql`  
  
  * (i) KEYWORD SEARCH: Find the best matching document to the keyword query "washington taxes treasury".  
        `cat part_i.sql`  

# Resource  
[Command Line Shell for SQLite](https://www.sqlite.org/cli.html)  
[Create View](http://www.w3schools.com/sql/sql_view.asp)  
