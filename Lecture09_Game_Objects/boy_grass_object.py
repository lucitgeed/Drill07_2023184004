from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self): # <- 생성자를 이용해서 객체의 초기 상태를 정의
        self.image = load_image("grass.png")

    def update(self): #잔디의 이미지는 움직이지 않으니 pass
        pass

    def draw(self):
        self.image.draw(400,30)

#

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,300), 90
        self.frame = random.randint(0, 10)
        self.image = load_image("run_animation.png")

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
    pass

#
class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(0,800), 599
        self.image = load_image("ball41x41.png")

    def update(self):
        self.y -= random.randint(2, 10)
        pass

    def draw(self):
        if self.y >=90:
            self.image.draw(self.x, self.y)

#
class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image("ball21x21.png")

    def update(self):
        self.y -= random.randint(2, 10)
        pass

    def draw(self):
        if self.y >= 90:
            self.image.draw(self.x, self.y)
    pass




##
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


##
def update_world():
    for objt in world:
        objt.update()

#    grass.update() #잔디의 상태를 (매 프레임마다)업데이트
#    for boy in team: #팀내 모든 소년들에 대해 모두 업데이트
#        boy.update()

    pass


##
def render_world():
    clear_canvas()

    for objt in world:
        objt.draw()

#    grass.draw()
#    for boy in team: #팀단위니까)팀의 boy를 전부 그림
#        boy.draw()

    update_canvas()
    pass

##
def reset_world(): #초기화하는 함수
    global running
    global grass
    global team
    global world

    global balls
    global allballs

    running = True
    world = []

    grass = Grass() #Grass라는 클래스를 이용해서 grass 객체를 생성
    world.append(grass)

    team = [ Boy()  for i in range(11)]   #리스트로 11명의 소년을 찍어냄
    world += team

    balls = [BigBall() for i in range(12)]
    world += balls
    allballs = [SmallBall() for i in range(11)]
    world += allballs


open_canvas()


# initialization code
reset_world()


# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
    pass


# finalization code
close_canvas()
