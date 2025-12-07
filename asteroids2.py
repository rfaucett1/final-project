import pygame, simpleGE, random

class Ship(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ship.png")
        self.setSize(200, 200)
        self.position =(30, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_UP):
            self.y -=self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y +=self.moveSpeed
        if self.isKeyPressed(pygame.K_SPACE):
            self.scene.bullet.fire()
    
class Bullet(simpleGE.Sprite):
    def __init__(self, scene):
      super().__init__(scene)
      self.colorRect("white", (5, 5))
      self.setBoundAction(self.HIDE)
      self.reset()
        
    def fire(self):
        self.position = (self.scene.ship.x, self.scene.ship.y)
        self.speed = 12
        self.setAngle(self.scene.ship.imageAngle)
        
    def reset(self):
        self.position = (-100, -100)
        self.speed = 0
        
    
class Rock(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("rock.png")
        self.reset()
        
    def process(self):
        self.imageAngle += self.rotSpeed
        
    def reset(self):        
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.position = (x, y)
        
        scale = random.randint(10, 40)
        self.setImage("rock.png")
        self.setSize(scale, scale)
        
        self.speed = random.randint(0, 6)
        self.setAngle(random.randint(0, 360))
        self.rotSpeed = random.randint(-5, 5)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.ship = Ship(self)
        self.bullet = Bullet(self)
        
        self.rocks = []
        for i in range(10):
            self.rocks.append(Rock(self))
            
        self.sprites = [self.bullet, self.ship, self.rocks]
           
        
    def process(self):
        for rock in self.rocks:
            if self.ship.collidesWith(rock):
                rock.reset()
            if self.bullet.collidesWith(rock):
                rock.reset()
                self.bullet.reset()

def main():
    game = Game()    
    game.start()
    
if __name__ == "__main__":
    main()