import pygame, simpleGE

class Ship(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ship.png")
        self.position =(320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x-=self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        if self.isKeyPressed(pygame.K_UP):
            self.y -=self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y +=self.moveSpeed
                 
             
def main():
    game = simpleGE.Scene()
    ship = Ship(game)
    game.sprites = [ship]
    game.start()
    
if __name__ == "__main__":

    main()
