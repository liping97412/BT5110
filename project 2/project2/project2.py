##### 
## This section imports the necessary classes and methods from the SQLAlchemy library
####
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#####
## This section creates an engine for the PostgreSQL
## and creates a database session s.
## You will use session s to execute queries.
#####
username = 'postgres'
password = 'waflf'
dbname = 'bt5110'
engine = create_engine('postgres://%s:%s@127.0.0.1:5432/%s' % (username, password, dbname))
Session = sessionmaker(bind=engine)
s = Session()


#################
## A method to print the result to a file
#################
def print_query(query, filename):	
    try:
        results = s.execute(query)
    except Exception as e:
        print(e)
        print('Skipping file %s.' % filename)
        s.rollback()
        return
        
    with open(filename, 'w') as out:
        csv_out = csv.writer(out)
        for result in results:
            csv_out.writerow(tuple(result))

    print('Done writing %s.' % filename)



#################
## Write your query here
################

### Change this to your metric number
metricno = "A0186040M"

### Question 1
q1a = """select cus.first_name,cus.last_name
         from customers as cus left join credit_cards as cre
         on cus.ssn=cre.ssn
         where cus.country='Singapore' and cre.type='visa';"""
print_query(q1a, 'q1a.csv')

q1b = """select ssn,count(number)
         from credit_cards
         group by ssn;"""
print_query(q1b, 'q1b.csv')

q1c = """select cus.first_name,cus.last_name,sum(t.amount) as total_expenditure
         from (customers as cus inner join credit_cards as cre on cus.ssn=cre.ssn) inner join transactions as t on cre.number=t.number
         where cus.country='Singapore'
         group by cus.ssn;"""
print_query(q1c, 'q1c.csv')

q1d = """select distinct cus.ssn,cus.first_name,cus.last_name
         from ((customers as cus inner join credit_cards as cre on cus.ssn=cre.ssn) inner join transactions as t on cre.number=t.number)
         inner join merchands as m on t.code=m.code
         where cus.country<>m.country;"""
print_query(q1d, 'q1d.csv')

q1e = """select  distinct cus.ssn
         from (customers as cus inner join credit_cards as cre on cus.ssn=cre.ssn) inner join transactions as t on cre.number=t.number
         where cre.type='visa' and t.datetime between '2017-12-25' and ‘2017-12-26’; """
print_query(q1e, 'q1e.csv')

q1f = """select cre.type,max(t.amount)
         from credit_cards as cre inner join transactions as t
         on cre.number=t.number
         group by cre.type;"""
print_query(q1f, 'q1f.csv')

### Question 2
q2a = """select t.identifier
         from credit_cards as cre inner join transactions as t on cre.number=t.number
         where cre.type||''||t.amount in(
	     select cre.type||''||max(t.amount) as max_amount
             from credit_cards as cre inner join transactions as t on cre.number=t.number
             group by cre.type);"""
print_query(q2a, 'q2a.csv')

q2b = """select t1.identifier
         from transactions as t1 inner join credit_cards as cre1 on t1.number=cre1.number
         where not exists(
	     select 1
	     from transactions as t2 inner join credit_cards as cre2 on t2.number=cre2.number
	     where cre2.type=cre1.type and t2.amount>t1.amount);"""
print_query(q2b, 'q2b.csv')

q2c = """select a.code,a.name
         from (select m.code,m.name,count(distinct cre.type) as count_type
	       from (merchands as m full outer join transactions as t on m.code=t.code)
	       full outer join credit_cards as cre on t.number=cre.number
	       group by m.code,m.name) as a
         where a.count_type<>16;"""
print_query(q2c, 'q2c.csv')

q2d = """select m.code,m.name
         from merchands as m
         where m.code in (
	     select distinct a.code
	     from (
		select t1.code,cre1.type
		from transactions as t1,credit_cards as cre1) as a
	        where not exists (
		    select b.code,b.type
		    from (transactions as t2 inner join credit_cards as cre2 on t2.number=cre2.number) as b
	            where a.code=b.code and a.type=b.type));"""
print_query(q2d, 'q2d.csv')


###########################################

