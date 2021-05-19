from neomodel import db
from models import User, Message
from tags import get_random_string, get_random_tag_sequence, get_random_user

db.set_connection('bolt://neo4j:lab3@localhost:7687')

for i in range(100):
    User(username = 'user'+str(i)).save()

for i in range(100):
    users = User.nodes.all()
    user1 = get_random_user(users)
    user2 = get_random_user(users)
    message_tags = get_random_tag_sequence()
    message_tags['text'] = get_random_string()
    user1.messages.connect(user2, message_tags)
