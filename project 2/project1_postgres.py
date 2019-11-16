##### 
## This section imports the necessary classes and methods from the SQLAlchemy library
####
from sqlalchemy import Column, Integer, String, Float, CHAR, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

#####
## This section creates an engine for the PostgreSQL
## and creates a database session s.
## You will use session s to execute queries.
#####
## old create engine code to load SQLite library
# engine = create_engine('sqlite:///project1.db')

username = 'postgres'
password = 'postgres'
dbname = 'bt5110'
engine = create_engine('postgres://%s:%s@localhost:5432/%s' % (username, password, dbname))

Session = sessionmaker(bind=engine)
s = Session()
Base = declarative_base()
Base.metadata.create_all(engine)
Base.metadata.bind = engine

#####
## This section creates the two results table namely sql_results and orm_results
## to store the results from the two queries, respectively using SQL Query and ORM.
#####
## Create the sql_results table

s.execute("DROP TABLE IF EXISTS sqlresults;")

s.execute("CREATE TABLE IF NOT EXISTS sqlresults (      \
            number INTEGER PRIMARY KEY,                      \
            credit_card_number VARCHAR(20),              \
            merchant_name VARCHAR(50)                    \
            );")

## Create the orm_results table
s.execute("DROP TABLE IF EXISTS ormresults;")

s.execute("CREATE TABLE IF NOT EXISTS ormresults (      \
            number INTEGER PRIMARY KEY,                      \
            credit_card_number VARCHAR(20),              \
            merchant_name VARCHAR(50)                    \
            );")

#####
## SQL Query
## ==============
## In this section you will need to execute a query to the `transactions` table to answer the following question in English
## "Find the credit card numbers and the merchant name for the transactions involving a mastercard for an amount larger than 450 dollars."
##
## 1. Use the execute method from the session s that receives an SQL SELECT query string as an input to get the results set.
## 2. Loop through the results set and execute SQL INSERT INTO queries to insert the results into the `sql_results` table.
#####

## Write query
results = s.execute("SELECT number, credit_card_number, merchant_name FROM transactions WHERE amount > 450 and credit_card_type='mastercard'")

## Insert into the result table
for r in results:
    s.execute("INSERT INTO sqlresults (number, credit_card_number, merchant_name) VALUES (%d, '%s', '%s')" % (r[0], r[1], r[2]))

#####
## ORM
## ==============
## In this section you will need to use ORM to answer the following question in English
## "Find the credit card numbers and the merchant name for the transactions involving a mastercard for an amount larger than 450 dollars."
##
## 1. Create the `Transactions` class wrapper for the ORM (this has been done for you).
## 2. Create the `ORMResults` class wrapper for the ORM.
## 3. Use the `query` and `filter` method from the session s to create the query to get the results set.
## 4. Loop through the results set, create an `ORMResults` object, set the value for each column and use the `add` method 
##    from session s to insert the result into the `orm_results` table.
#####
## Wrapper class for transactions table
class Transactions(Base):
    __tablename__ = 'transactions'
    number = Column(Integer, primary_key = True)
    merchant_name = Column(String(50))
    merchant_code = Column(CHAR(10))
    credit_card_number = Column(String(20))
    credit_card_type = Column(String(30))
    amount = Column(Float())

## ORM Results class
class ORMResults(Base):
    __tablename__ = 'ormresults'
    number = Column(Integer, primary_key = True)
    credit_card_number = Column(String(20))
    merchant_name = Column(String(50))

## Query the transactions table
results = s.query(Transactions.number, Transactions.credit_card_number, Transactions.merchant_name).filter(Transactions.amount > 450).filter(Transactions.credit_card_type == 'mastercard')

## Insert into the ORM Results table
for r in results:
    result = ORMResults()
    result.number = r.number
    result.credit_card_number = r.credit_card_number
    result.merchant_name = r.merchant_name

    s.add(result)

## Commit all the action and save the database
s.commit()
