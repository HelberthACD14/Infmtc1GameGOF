class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, obj):
        print('{} Tienes vida "{}"'.format(self.name, obj.live))
        
class Publisher:
    def __init__(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.discard(who)
    def dispatch(self, obj):
        for subscriber in self.subscribers:
            subscriber.update(obj)
"""
def main():
    pub = Publisher()
    bob = SubscriberOne('Bob')
    alice = SubscriberTwo('Alice')
    john = SubscriberOne('John')

    pub.register(bob, bob.update)
    pub.register(alice, alice.receive)
    pub.register(john)

    pub.dispatch("It's lunchtime!")
    pub.unregister(john)
    pub.dispatch("Time for dinner")

 
if __name__ == '__main__':
    main()
"""