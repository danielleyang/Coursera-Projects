# Description  
This SQL project focuses using UNION, JOIN, SUM, GROUP BY, ORDER BY etc functions to extract the information from databases. It also transforms a matrix into a table and expresses matrix multiplication as a SQL query.  

# DATE  
07/11/16 - 07/17/16  

# Usage  
The two databases used in this project can be download from [uwescience/datasci_course_materials](https://github.com/uwescience/datasci_course_materials.git)  
` `Create a folder in your local directory and clone the original datafiles  
`git clone https://github.com/uwescience/datasci_course_materials.git`   

` `For part I and III  
`sqlite3 reuters.db`  

` `For part II  
`sqlite3 matrix.db`   

# SQL queries  
` `All of the SQL queries and its results are under this folder  
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

