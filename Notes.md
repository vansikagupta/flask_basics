# flask_basics
  A basic flask application that helps understand APIs and restful architecture
 
# Notes
 
* API or Application Programming Interface, are contracts that define how to cummunicate with services, what to provide as input      and what to expect as results.
  They are exposed functionalities of Operating Systems and Software applications.
  Using APIs help us focus on functionalities without looking into development of the essentials.
  Modern APIs are standardized and documented and are treated like productized software with their own software development lifecycle SDLC 
* REST is a design pattern or architectural style for designing or architecting APIs

#
* SQLAlchemy is an ORM, Object Relational Mapper
* app.config is a python dict which is used to set environment variables and project attributes
* Writing sql queries to connect Flask application with databases can be very tedious. Using an ORM like SQLAlchemy is very helpful here.
* Job of the ORM is to map python classes/objects into underlying table structures.
# CRUD operations
* create instance 
* db.session.add(<instance of Model Class>)
* db.session.commit()
* session is a temporary space in memory where uncommited actions are stored. 
* query/read data using Model.query method
* For related tables, first query the parent table then use that data as filter to query the child table.
* in order to update, 
	* query the record 
	* override the value
	* commit the db session
* deleting a record is very simple, for single record db.session.delete(record) can be used and for one or more records .delete() can be used on the query object
* In order to delete record from tables where dependencies exist, first delete from parent table then from child table.
