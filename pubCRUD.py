from run import db, Publications

p1 = Publications("Oxford Publications")
p2 = Publications("Paramount Press")
p3 = Publications("Oracle Books Inc")
p4 = Publications("Vintage Books and Comics")
p5 = Publications("Trolls Press")
p6 = Publications("Broadway Press")
p7 = Publications("Downhill Publishers")
p8 = Publications("Kingfisher Inc")
db.session.add_all([p1,p2,p3,p4,p5,p6,p7,p8])
db.session.commit()


#arya = Publications(100,'Arya Publications')
#db.session.add(arya)
#db.session.commit()

#oracle = Publications(101,'Oracle Publications')
#orient = Publications(102,'Orient Publications')
#paramount = Publications(103,'Paramount Publications')
#all_pubs = [oracle, orient, paramount]
#db.session.add_all(all_pubs)
#db.session.commit()

