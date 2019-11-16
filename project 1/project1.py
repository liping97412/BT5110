##### 
## This section imports the necessary classes and methods from the SQLAlchemy library
####
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

#####
## This section creates an engine for the SQLite DB from project1.db 
## and creates a database session s.
## You will use session s to execute queries.
#####
engine = create_engine('sqlite:///project1.db')
Session = sessionmaker(bind=engine)
s = Session()
Base = declarative_base()
Base.metadata.create_all(engine)
Base.metadata.bind = engine

#####
## This section creates the two results table namely sql_results and orm_results with SQL query
## using the execute method from session s to store the results from the two queries, respectively using SQL Query and ORM.
#####
## Create the sql_results table
s.execute("DROP TABLE IF EXISTS sqlresults;")

s.execute("CREATE TABLE IF NOT EXISTS sqlresults (      \
            number INT PRIMARY KEY,                      \
            credit_card_number VARCHAR(50),              \
            merchant_name VARCHAR(50)                    \
            );")

## Create the orm_results table
s.execute("DROP TABLE IF EXISTS ormresults;")

s.execute("CREATE TABLE IF NOT EXISTS ormresults (      \
            number INT PRIMARY KEY,                      \
            credit_card_number VARCHAR(50),              \
            merchant_name VARCHAR(50)                    \
            );")



#####
## SQL Query
## ==============
## In this section you will need to execute a query to the `transactions` table to answer the following question
## "Find the number, credit card number and the merchant name of the transactions involving a mastercard for an amount larger than 450 dollars."
## 1. Use the session object s and its execute method to execute the SQL query as an SQL string. 
## 2. Use the session object s and its `execute` method to insert the results of the SQL query into the table `sqlresults` with SQL insertions as SQL strings.
#####

######### WRITE YOUR CODE HERE



################################


#####
## ORM
## ==============
## In this section you will need to use ORM to answer the following question
## "Find the number, credit card number and the merchant name of the transactions involving a mastercard for an amount larger than 450 dollars."
## 1. Use the session object s and its `query` method to query the class mapped to the `transactions` table. The class mapping has been done for you.
## 2. Map a class to the `ormresults` table.
## 3. Use the session object and its `add` method to add the results of the query to the class mapped to the `ormresults` table. 
#####
## Wrapper class for transactions table
class Transactions(Base):
    __tablename__ = 'transactions'
    number = Column(Integer, primary_key = True)
    merchant_name = Column(String(50))
    merchant_code = Column(String(50))
    credit_card_number = Column(String(50))
    credit_card_type = Column(String(50))
    amount = Column(Float())

######### WRITE YOUR CODE HERE
## Wrapper class for ormresults table




################################



## Commit all the action and save the database
s.commit()

print "success"

### END OF FILE ###
