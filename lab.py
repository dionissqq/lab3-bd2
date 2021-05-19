from models import User, Message
from neomodel import db
db.set_connection('bolt://neo4j:lab3@localhost:7687')

# results, meta = db.cypher_query('MATCH (n1)-[r]->(n2) WHERE r.bed=true and  r.sql=true RETURN n1')
# for u in results:
#     print('user_with_id', u[0].id)

print('choose option')
print('1)get users that sent messages with tags')
print('2)get users by connection len')
print('3)get users connection')
print('4)get spam connections')
print('5)get users that sent tags but are not connected')

m = input()
if m == '1':
    string = ''
    query1 = 'MATCH (n1)-[r]->(n2) WHERE '
    query2 = ' RETURN n1'
    my_tags = ''
    while True:
        string = input()
        if string=='exit':
            if len(my_tags):
                my_tags = my_tags[:-4]
            break
        my_tags+= 'r.'+string+'=true'
        my_tags+= ' and '

    q = query1+my_tags+query2
    print(q)
    results, meta = db.cypher_query(q)
    for u in results:
        print('user_with_id', u[0].id)
elif m == '2':
    inp = input()
    num = int()
    query1 = 'MATCH (n1)-[*'
    query2 = ']->(n2) RETURN n1, n2'
    q = query1+inp+query2
    print(q)
    results, meta = db.cypher_query(q)
    for u in results:
        print('user_from_id', u[0].id,'user_to_id', u[1].id)

elif m == '3':
    u1 = 'user'+input()
    u2 = 'user'+input()
    q = 'MATCH (a:User {username:"'+u1+'"}),(v:User {username:"'+u2+'"}),p = allShortestPaths((a)-[*]-(v)) WITH p RETURN p'
    results, meta = db.cypher_query(q)
    for u in results[0][0].nodes:
        print ('user',u.id,'->')

elif m=='4':
    q = '''
        MATCH p = (n1)-[]-(n2)
        WITH *, relationships(p) AS p
        WHERE all(r IN relationships(p) WHERE r.spam=true)
        return n1,n2
    '''
    results, meta = db.cypher_query(q)
    for u in results:
        print ('user',u[0].id,'->',u[1].id)
    
elif m=='5':
    string = ''
    query1 = 'MATCH (n)-[k]->(), (n1) where '
    query2 = ' id(n)<>id(n1) and not exists((n)-[*]-(n1)) return n, n1'
    my_tags = ''
    while True:
        string = input()
        if string=='exit':
            break
        my_tags+= 'k.'+string+'=true'
        my_tags+= ' and '

    q = query1+my_tags+query2
    print(q)