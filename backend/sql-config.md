
# Revision Questions
> 1.  What is DBMS:

Database management system is software that store and manage data. It also allows for data modification such as insertion, deletion, and updating.

The DBMS system also manages the database by defining, generating, modifying, and regulating it. It’s built to develop and preserve data while also allowing each business application to retrieve the information it needs.

> 2. What is RDBMS:

RDBMS stands for Relational Database Management System, and it is a software system that is used to store only data in the form of tables. 

Data is handled and stored in rows and columns, which are referred to as tuples and attributes, in this type of system. RDBMS (Relational Database Management System) is a strong data management system that is extensively used across the world.

> 3. What is diffrent betweeen DBMS and RDBMS

DBMS:\
= Data is stored in a database management system (DBMS) as a file\
= Only a single user is supported by the DBMS\
= The data in a typical database may not be stored according to the ACID model(Atomicity, Consistency, Isolation, Durability). this can lead to database discrepancies\
= Client-server architecture is not supported by DBMS\
= There is no correlation between the data

RDBMS:\
= Tables are used to store information\
= It may be used by numerous people\
= Relational databases are more difficult to create, but they are more consistent and organised. They follow the rules of ACID (Atomicity, Consistency, Isolation, Durability)\
= Client-server architecture is supported by RDBMS\
= Data is kept in the form of tables that are linked together via foreign keys

> 4. What is SQL

SQL stand for Structured query language, it is the standard language for RDBMS. It is especially useful in handling organized data comprised of entities (variables) and relations between different entities of the data.

> 5. Explain diffrent betweeen SQL and NOSQL:

SQL\
= Also known as relations database, followa structured datamodel based on tables with rows and columns. \
= They enforce a predefined schema and relationship between data are established throught foreign keys.\
= SQL databases are well-suited for applications requiring complex queries, transactions, and strong consistency, such as financial systems, enterprise applications, and traditional relational data.

NOSQL\
= This database support various data models, including document-oriented, key-value, columns and graph databases.\
= They have schema-less or flexible schemas, allowing for dynamic and unstructured data.\
= NoSQL databases are suitable for handling large volumes of rapidly changing data, such as social media feeds, IoT (Internet of Things) data,real-time analytics, and content management systems.

> 6. What is diffrent between DELETE, DROP and TRUNCATE statement in sql

DELETE : Is used delete row from tables\
DROP : Is used to remove an object from the databas. if you drop the table, all row from the table are deleted and the table structured is remove from the database.\
TRUNCATE : Is used to delete all row from the table and free the space containing the table.

> 7. What is primary key, foreign key and unique key:

PRIMARY : primary key is field or the combination of field that uniqueli identify the each record in the table.it is the one of the special kind of unique key. it cannot be null or empty.A table contain deplicate coulmns, but it cannot more then one primarykey. it always store unique value into colums\
FOREIGN : foreign key use to link one or more table togather. it is also known as refrencing key. foreign key is specified as key that is related to the primary key of other table.\
UNIQUE : unique key is single or combination of field that endure all value store in the columns will ne unique. it means columns does not store duplicate value. Ex. email, roll no

> 8. What is aggregate function:

An aggregate function is a function that performs a calculation on a set of values, and returns a single value.(MIN(), MAX(), COUNT(), AVG(), SUM())