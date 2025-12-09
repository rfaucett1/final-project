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
        
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
             
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("galaxy.png")
        self.ship = Ship(self)
        self.bullet = Bullet(self)
        self.score = 0
        self.lblScore = LblScore()
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 20              
        self.lblTime = LblTime()
        
        self.rocks = []
        for i in range(10):
            self.rocks.append(Rock(self))
            
        self.sprites = [self.bullet,
                        self.ship,
                        self.rocks,
                        self.lblScore,
                        self.lblTime]
           
        
    def process(self):
        for rock in self.rocks:
            if rock.collidesWith(self.ship):
                rock.reset()
            if rock.collidesWith(self.bullet):
                rock.reset()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()
            
class Instructions(simpleGE.Scene):
    def __init__(self, prevScore):
        super().__init__()
                
        self.prevScore = prevScore
                
        self.setImage("galaxy.png")
        self.response = "Quit"
               
        
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines =[
        "You are a space explorer sent on a mission.",
        "Move with left and right arrow keys.",
        "Use the space bar to clear Asteroids."
        "Get as many Asteroids as you can",
        "in the time provided",
        "",
        "Good Luck"]
        
        self.directions.center = (320, 240)
        self.directions.size = (500, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 400)
        
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Last Score: 0"
        self.lblScore.center = (320, 400)
        
class Pause(simpleGE.Scene):
    def __init__(self, Game):
        super().__init__()
        
        self.pause = Pause
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 400)
        
        self.btnReset = simpleGE.Button()
        self.btnPlay.text = "Reset"
        self.btnPlay.center = (100, 400)
        
        def doEvents(self, event):
            if event.type == pygame.KEYRIGHT:
                if event.key == pygame.K_p:
                    if self.pause.visible:
                        self.pause.hide()
                else:
                    self.pause.show()
        
    
def main():
    keepGoing = True
    lastScore = 0
    
    while keepGoing:
        instructions = Instructions(lastScore)
        instructions.start()
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            lastScore = game.score
            
        else:
            keepGoing = False
    
if __name__ == "__main__":
    main()