"""The Pong Game."""
import sys

from pygame2.color import Color
from pygame2.ebs import *
try:
    import pygame2.video as video
    import pygame2.sdl.events as sdlevents
    import pygame2.sdl.timer as sdltimer
    import pygame2.sdl.keycode as sdlkc
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PADDLE_SPEED = 3
BALL_SPEED = 3

class CollisionSystem(Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(CollisionSystem, self).__init__()
        self.componenttypes = (Velocity, video.Sprite)
        self.ball = None
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def _overlap(self, item):
        sprite = item[1]
        if sprite == self.ball.sprite:
            return False

        left, top, right, bottom = sprite.area
        bleft, btop, bright, bbottom = self.ball.sprite.area

        return bleft < right and bright > left and \
            btop < bottom and bbottom > top

    def process(self, world, componentsets):
        collitems = filter(self._overlap, componentsets)
        if len(collitems) != 0:
            self.ball.velocity.vx = -self.ball.velocity.vx

            sprite = collitems[0][1]
            ballcentery = self.ball.sprite.y + self.ball.sprite.size[1] // 2
            halfheight = sprite.size[1] // 2
            stepsize = halfheight // 10
            degrees = 0.7
            paddlecentery = sprite.y + halfheight
            if ballcentery < paddlecentery:
                factor = (paddlecentery - ballcentery) // stepsize
                self.ball.velocity.vy = -int(round(factor * degrees))
            elif ballcentery > paddlecentery:
                factor = (ballcentery - paddlecentery) // stepsize
                self.ball.velocity.vy = int(round(factor * degrees))
            else:
                self.ball.velocity.vy = - self.ball.velocity.vy

        if self.ball.sprite.y <= self.miny or \
                self.ball.sprite.y + self.ball.sprite.size[1] >= self.maxy:
            self.ball.velocity.vy = - self.ball.velocity.vy

        if self.ball.sprite.x <= self.minx or \
                self.ball.sprite.x + self.ball.sprite.size[0] >= self.maxx:
            self.ball.velocity.vx = - self.ball.velocity.vx


class MovementSystem(Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(MovementSystem, self).__init__()
        self.componenttypes = (Velocity, video.Sprite)
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def process(self, world, componentsets):
        for velocity, sprite in componentsets:
            swidth, sheight = sprite.size
            sprite.x += velocity.vx
            sprite.y += velocity.vy

            sprite.x = max(self.minx, sprite.x)
            sprite.y = max(self.miny, sprite.y)

            pmaxx = sprite.x + swidth
            pmaxy = sprite.y + sheight
            if pmaxx > self.maxx:
                sprite.x = self.maxx - swidth
            if pmaxy > self.maxy:
                sprite.y = self.maxy - sheight


class TrackingAIController(Applicator):
    def __init__(self, miny, maxy):
        super(TrackingAIController, self).__init__()
        self.componenttypes = (PlayerData, Velocity, video.Sprite)
        self.miny = miny
        self.maxy = maxy
        self.ball = None

    def process(self, world, componentsets):
        for pdata, vel, sprite in componentsets:
            if not pdata.ai:
                continue

            sheight = sprite.size[1]
            centery = sprite.y + sheight // 2
            if self.ball.velocity.vx < 0:
                # ball is moving away from the AI
                if centery < self.maxy // 2 - PADDLE_SPEED:
                    vel.vy = PADDLE_SPEED
                elif centery > self.maxy // 2 + PADDLE_SPEED:
                    vel.vy = -PADDLE_SPEED
                else:
                    vel.vy = 0
            else:
                bcentery = self.ball.sprite.y + self.ball.sprite.size[1] // 2
                if bcentery < centery + sheight // 3:
                    vel.vy = -PADDLE_SPEED
                elif bcentery > centery - sheight // 3:
                    vel.vy = PADDLE_SPEED
                else:
                    vel.vy = 0


class Renderer(video.SpriteRenderer):
    def __init__(self, window):
        super(Renderer, self).__init__(window)

    def process(self, world, componentsets):
        video.fill(self.surface, BLACK)
        super(Renderer, self).process(world, componentsets)


class Velocity(Component):
    def __init__(self):
        super(Velocity, self).__init__()
        self.vx = 0
        self.vy = 0


class PlayerData(Component):
    def __init__(self):
        super(PlayerData, self).__init__()
        self.ai = False
        self.points = 0


class Player(Entity):
    def __init__(self, world, posx=0, posy=0, ai=False):
        self.sprite = video.Sprite(size=(20, 100), bpp=32)
        video.fill(self.sprite, WHITE)
        self.sprite.position = posx, posy
        self.velocity = Velocity()
        self.playerdata = PlayerData()
        self.playerdata.ai = ai


class Ball(Entity):
    def __init__(self, world, posx=0, posy=0):
        self.sprite = video.Sprite(size=(20, 20), bpp=32)
        video.fill(self.sprite, WHITE)
        self.sprite.position = posx, posy
        self.velocity = Velocity()


def run():
    video.init()
    window = video.Window("The Pong Game", size=(800, 600))
    window.show()

    world = World()

    movement = MovementSystem(0, 0, 800, 600)
    collision = CollisionSystem(0, 0, 800, 600)
    renderer = Renderer(window)
    aicontroller = TrackingAIController(0, 600)

    world.add_system(aicontroller)
    world.add_system(movement)
    world.add_system(collision)
    world.add_system(renderer)

    player1 = Player(world, 0, 250)
    player2 = Player(world, 780, 250, True)
    ball = Ball(world, 390, 290)
    ball.velocity.vx = - BALL_SPEED
    collision.ball = ball
    aicontroller.ball = ball

    while True:
        event = sdlevents.poll_event(True)
        if event is not None:
            if event.type == sdlevents.SDL_QUIT:
                break
            if event.type == sdlevents.SDL_KEYDOWN:
                if event.key.keysym.sym == sdlkc.SDLK_UP:
                    player1.velocity.vy = -PADDLE_SPEED
                elif event.key.keysym.sym == sdlkc.SDLK_DOWN:
                    player1.velocity.vy = PADDLE_SPEED
            elif event.type == sdlevents.SDL_KEYUP:
                if event.key.keysym.sym in (sdlkc.SDLK_UP, sdlkc.SDLK_DOWN):
                    player1.velocity.vy = 0
        sdltimer.delay(10)
        world.process()

if __name__ == "__main__":
    sys.exit(run())
