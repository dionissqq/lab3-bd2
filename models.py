from neomodel import StructuredNode, StructuredRel, \
    StringProperty, BooleanProperty, RelationshipTo

class Message(StructuredRel):
    text = StringProperty()
    spam = BooleanProperty()
    soup = BooleanProperty()
    death = BooleanProperty()
    raven = BooleanProperty()
    bed = BooleanProperty()
    food = BooleanProperty()
    alch = BooleanProperty()
    rabbit = BooleanProperty()
    sql = BooleanProperty()

class User(StructuredNode):
    username = StringProperty()
    active = BooleanProperty(default = False)
    messages = RelationshipTo('User', 'MESSAGE', model = Message)

    def __str__(self) -> str:
        return 'user_with_id'+str(self.id)

