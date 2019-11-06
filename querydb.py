from run import db, Books, Publications

#use dir(Books.query) to explore various options
print(Books.query.all())
#gives all books entries

print(Books.query.first())
#gives first entry

#copy paste at console or add print statements

all = Books.query.all()
all[:3]#gives first three entries

Books.query.filter_by(format='eBook').all()
Books.query.filter_by(format='Hardcover').all()

#query using primary key
Books.query.get(4)

#set limit to the number of rows returned
Books.query.limit(5).all()

#sort data using order_by
Books.query.filter_by(format='Hardcover').order_by(Books.title).all()

#query data from 2 related tables
pub = Publications.query.filter_by(name='Broadway Press').first()
pub.name
pub.id
books_by_pub = Books.query.filter_by(pub_id=pub.id).all()

##################################
#updating a value
u = Books.query.get(2)
u.format = 'Paperback'
db.session.commit()

#################################
#deleting single entry from Books
b = Books.query.get(3)
db.session.delete(b)
db.session.commit()

#deleting from publications (parent table)
pub_to_del = Publications.query.get(6)
Books.query.filter_by(pub_id=pub_to_del.id).delete()
Publications.query.filter_by(id=6).delete()
db.session.commit()