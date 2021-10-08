from modelos.gameConfig import *
from pygame import *
from pygame.sprite import Sprite


class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, obj,baner,screen,zombie):
            print('{} Tienes vida "{}" Levas {}'.format(self.name, obj.live,baner.puntos))
            if baner.puntos%100==0:
               zombie.velocidad+=1
            fuente = font.Font(None, 30)
            texto = fuente.render('Zombie Speed {} Puntos {} -  Vida ({})  '.format(zombie.velocidad,baner.puntos,obj.live), 1, (100,255,255))
            screen.blit(texto, (SCREEN_WIDTH-790, SCREEN_HEIGHT-20))
            #texto = fuente.render("Vida: " + str(self.vida), 1,(240,60,75))
            #creen.blit(texto, (SCREEN_WIDTH-750, SCREEN_HEIGHT-20))
            """
            fuente = font.Font(None, 30)
            texto = fuente.render("Puntos: " + str(self.puntos), 1, (100,255,255))
            screen.blit(texto, (SCREEN_WIDTH-140, SCREEN_HEIGHT-20))
    
            texto = fuente.render("Vida: " + str(self.vida), 1,(240,60,75))
            screen.blit(texto, (SCREEN_WIDTH-750, SCREEN_HEIGHT-20))
            """
        
class Publisher:
    def __init__(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.discard(who)
    def dispatch(self, obj,baner,screen,zombie):
        for subscriber in self.subscribers:
            subscriber.update(obj,baner,screen,zombie)
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