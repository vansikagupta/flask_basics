from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

#to set some project attributes
app.config.update(
    SECRET_KEY='password',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:Mandal@localhost/catalog_db',
    #SQLALCHEMY_DATABASE_URI='<database>://<userid>:<password>@<server>/<database_name>',
    SQLALCHEMY_TRACK_MODIFICATIONS=True
)

#creates a link between the database and the flask application
db=SQLAlchemy(app)

# multiple decorators per function is allowed
@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask'


# If query string is sent along the request object, we can get it using get method of dict
# works for URL /new/?greeting=Hello
@app.route('/new/')
def query_string(greetings='Hello'):
    query_val = request.args.get('greeting', greetings)
    # if no greeting is passed it takes none
    return '<h1>We are greeting you : {0} </h1>'.format(query_val)


@app.route('/user/')
@app.route('/user/<name>')
def no_query_string(name='user1'):
    return '<h1>We are greeting the user : {0} </h1>'.format(name)


@app.route('/books/')
@app.route('/books/<name>')
def render_books(name='Harry'):
    books = ['The notebook', 'eleven Minutes', 'the Shopaholic', 'The Monk Who sold His Ferrari', 'One Hundred Stitches']
    return render_template('books.html', books=books, name=name)


class Publications(db.Model):
    __tablename__='publications'
    #this was optional overriding
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        #self.id = id
        self.name = name

    def __repr__(self):
        return 'Id is <{}> and Name is <{}>'.format(self.id,self.name)


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)#index will help in referencing
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    #Establish Relation
    pub_id = db.Column(db.Integer, db.ForeignKey('publications.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):
        #here id gets self generated
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)


if __name__ == '__main__':
    db.create_all()
    #this will create all tables that don't exist
    app.run(debug=True)
