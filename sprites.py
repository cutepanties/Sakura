import pygame
from settings import *
VEC = pygame.math.Vector2


class Player(pygame.sprite.Sprite):

    def __init__(self, sakura):
        # some flags and vars
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        # sakura class instance
        self.game = sakura
        # init sprites class 
        pygame.sprite.Sprite.__init__(self)
        self.image = self.game.standing
        # player position, acceleration, velocity vectors
        self.pos = VEC(STARTX, STARTY)
        self.accel = VEC(0,0)
        self.vel = VEC(0,0)
        # get rectangular area of player
        self.rect = pygame.Surface.get_rect(self.image)
        # get width and height of player
        self.player_width = pygame.Surface.get_width(self.image)
        self.player_height = pygame.Surface.get_height(self.image)

    def update(self):
        self.accel = VEC(0,GRAVITY)

        # animate player
        self.animate()

        # check if a key is pressed and add acceleration to the player
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.accel.x = PLAYER_ACCEL
        if pressed[pygame.K_LEFT]:
            self.accel.x = -PLAYER_ACCEL

        # make the player move
        self.accel.x += self.vel.x * PLAYER_FRICT
        self.vel += self.accel
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.accel

        # stop the player from leaving the screen
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH

        # set player position
        self.rect.midbottom = self.pos+(1,1)

    # this function is called only once 
    # in the events() method of sakura
    # if the space key is pressed
    def jump(self):
        # move the player one frame down and check for collision
        self.rect.y += 1
        collide = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1
        # if collide sub 14 from y
        if collide:
            self.vel.y = -14

    # player animation
    def animate(self):
        # get milliseconts since pygame.init()
        time = pygame.time.get_ticks()

        # sets jumping to True 
        # only if the player is not on a platform
        if self.vel.y != 0:
            self.jumping = True
        else:
            self.jumping = False
        # sets walking to True if walking
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False

        # if the player is jumping
        if self.jumping:
            # uses the left looking jump frame
            # if the player is moving left 
            # else uses the right one
            if self.vel.x < 0:
                self.image = self.game.jump_frame_l
            else:
                self.image = self.game.jump_frame_r

        # walk animation
        if self.walking:
            # changes frames every 400 millisecs
            if time - self.last_update > 400:
                self.last_update = time
                # gets frame index
                self.current_frame = (self.current_frame + 1) % len(self.game.walk_left)
                # gets last frame's rect bottom
                bottom = self.rect.bottom
                # left looking frame if walking left
                # else right looking
                if self.vel.x > 0:
                    self.image = self.game.walk_right[self.current_frame]
                if self.vel.x < 0:
                    self.image = self.game.walk_left[self.current_frame]

                self.game.walk_sound.set_volume(0.02)
                self.game.walk_sound.play(0)

                # makes sure the players frame
                # stays on the same y position
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        # use standing frame if player is not moving
        if not self.walking and not self.jumping:
            self.image = self.game.standing


class Platforms(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h):
        # init sprites class 
        pygame.sprite.Sprite.__init__(self)
        # create plarform and color it
        self.image = pygame.Surface((w, h))
        self.image.fill(PINK)
        # set platform's position
        self.rect = pygame.Surface.get_rect(self.image)
        self.rect.x = x
        self.rect.y = y


# image objects
class ImObj(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        # init sprites class
        pygame.sprite.Sprite.__init__(self)
        # save image in image var
        self.image = image
        # set sakuras position
        self.rect = pygame.Surface.get_rect(self.image)
        self.rect.x = x
        self.rect.bottom = y


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pass
