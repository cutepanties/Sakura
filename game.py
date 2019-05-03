import pygame
import random
import sprites
from settings import *


class Sakura:

    def __init__(self):
        # flags to check if the player is done playing
        self.done = False
        # initialize pygame, set window title, width and height
        pygame.init()
        pygame.display.set_caption(CAPTION)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # init sprite class
        pygame.sprite.Sprite.__init__(self)
        # init pygame mixer
        pygame.mixer.init()
        # load images
        self.load_images_sounds()
        # init pygame clock for fps
        self.clock = pygame.time.Clock()
        # fonts only for sakuras gathered
        pygame.font.init()
        self.font = pygame.font.Font(FONT,18)

    def load_images_sounds(self):
        # minkie static frame
        self.standing = pygame.image.load(STATIC).convert_alpha()
        # minkie walking frames
        self.walk_right = [pygame.image.load(WALK1).convert_alpha(),
                           pygame.image.load(WALK2).convert_alpha()]
        self.walk_left = []
        for frame in self.walk_right:
            self.walk_left.append(pygame.transform.flip(frame, True, False))
        # minkie jumping frames
        self.jump_frame_r = pygame.image.load(JUMP1).convert_alpha()
        self.jump_frame_l = pygame.transform.flip(self.jump_frame_r, True, False)
        # floating sakuras image
        self.sakuras = pygame.image.load(SAFLO).convert_alpha()
        self.sakuras = pygame.transform.scale(self.sakuras, (30, 30))
        # background
        self.bg_frames = []
        for frame in SNOWSA:
            self.bg_frames.append(pygame.transform.scale((pygame.image.load(frame).convert_alpha()),
                                                        (300,300)))
        # Tree
        self.tree = pygame.image.load(TREE).convert_alpha()
        # tree position x and y
        self.treex = 3250 - pygame.Surface.get_width(self.tree)
        self.treey = 530

        # sound files and volumes
        self.startscreen_sound = pygame.mixer.Sound(STARTSOUND)
        self.startscreen_sound.set_volume(0.5)
        self.gamestart_sound = pygame.mixer.Sound(GAMESTARTSOUND)
        self.gamestart_sound.set_volume(0.6)
        self.bgsound = pygame.mixer.Sound(BGSOUND)
        self.bgsound.set_volume(0.4)
        self.walk_sound = pygame.mixer.Sound(STEPS)
        self.jump_sound = pygame.mixer.Sound(JUMPSOUND)

    def new_game(self):
        # vars
        self.won = False
        self.last_update = 0
        self.current_frame = 0
        # sakuras gathered
        self.gathered = 0
        # player instance
        self.player = sprites.Player(self)
        # create platforms and other objects
        self.platsnobjs()
        # run the game
        self.run()

    # Game loop
    def run(self):
        while not self.done:
            # check for game events
            self.events()
            # draw on the screen 
            self.draw()
            # continuously updates game
            self.update()
            # set the game framerate
            self.clock.tick(120)

    def update(self):
        #print(self.player.pos)
        # update all sprites on screen
        self.all_sprites.update()
    # ~~~~~~~~~~ collisions ~~~~~~~~~~
        # check for collisions for every platform separately
        for plat in self.platforms:
            if self.player.rect.colliderect(plat.rect):
                # if the player is above the plat set the position on top
                if self.player.rect.top < plat.rect.top:
                    self.player.pos.y = plat.rect.top
                    # set the velocity to 0 only if falling
                    if self.player.vel.y > 0:
                        self.player.vel.y = 0
                # hit the bottom of a plat if it's above the player
                if self.player.rect.center[1] > plat.rect.top:
                    self.player.pos.y = plat.rect.bottom + self.player.player_height
                    self.player.vel.y += 1.4
        # check for collisions with sakuras
        collide = pygame.sprite.spritecollide(self.player, self.saflos, True)
        if collide:
            self.gathered += 1
    # ~~~~~~~~~~ Camera movement ~~~~~~~~~~
        # move everything to the left if the player passed screen's 1/2
        if self.player.pos.x > WIDTH/2+10 and self.ground.rect.right > WIDTH:
            # adjust players velocity to moving screen
            self.player.pos.x -= abs(self.player.vel.x)
            # move every platform left
            for obj in self.objtomove:
                if self.player.vel.x > 1:
                    obj.rect.x -= 2

        # move everything right if moving backwards and there are platforms @ -0
        if self.player.pos.x < WIDTH/2+10 and self.ground.rect.x < 0:
            # adjust player velocity to moving screen
            self.player.pos.x += abs(self.player.vel.x)
            # move every platform
            for obj in self.objtomove:
                if self.player.vel.x < -1:
                    obj.rect.x += 2

        # flips the buffers
        pygame.display.flip()

    # event handler
    def events(self):
        for event in pygame.event.get():
            # quit event - quits game
            if event.type == pygame.QUIT:
                self.done = True
            if event.type == pygame.KEYDOWN:
                # jumping
                if event.key == pygame.K_SPACE:
                    self.player.jump()

    def draw(self):
        time = pygame.time.get_ticks()
        # color the screen black
        self.screen.fill((BLACK))

        # ~~~~~~~~ draw snowing sakuras ~~~~~~~~
        # save last frame 
        last_frame = self.bg_frames[self.current_frame]
        if time - self.last_update > 200:
            self.last_update = time
            # iterate through every frame in the list
            self.current_frame = (self.current_frame + 1) % len(self.bg_frames)
            # blit the frame on 6 parts of the screen
            for i in range(3):
                self.screen.blit(self.bg_frames[self.current_frame], (i/3*WIDTH,0))

            for i in range(3):
                self.screen.blit(self.bg_frames[self.current_frame], (i/3*WIDTH,1/2*HEIGHT))
        else:
            # keep blitting the last image on screen
            # if the above condition is not True
            for i in range(3):
                self.screen.blit(last_frame, (i/3*WIDTH,0))

            for i in range(3):
                self.screen.blit(last_frame, (i/3*WIDTH,1/2*HEIGHT))

        # check for collisions with the ending tree
        collide = pygame.sprite.spritecollide(self.player, self.endtree, False,
                                              collided = pygame.sprite.collide_circle_ratio(.7))
        # if player collides with the tree
        # and has gathered all sakuras
        # show game over screen
        if collide and self.gathered == len(SAKURAFLOS):
            self.won = True
            self.done = True
        # show sakuras gathered
        self.textsurf = self.font.render('sakuras gathered - %d' % self.gathered,
                                         False, (WHITE))
        self.screen.blit(self.textsurf,(5,5))
        # draws platforms and player + movements
        self.all_sprites.draw(self.screen)

    def platsnobjs(self):
        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.saflos = pygame.sprite.Group()
        self.objtomove = pygame.sprite.Group()
        self.endtree = pygame.sprite.Group()
        # add player sprite to all groups
        self.all_sprites.add(self.player)
        # create and add to groups the ground platform manually
        # for camera movement control
        self.ground = sprites.Platforms(*GROUND_PLAT)
        self.all_sprites.add(self.ground)
        self.platforms.add(self.ground)
        self.objtomove.add(self.ground)
        # create and add to groups the tree object for later
        # collision detection
        self.treeobj = sprites.ImObj(self.tree, self.treex, self.treey)
        self.endtree.add(self.treeobj)
        self.objtomove.add(self.treeobj)
        self.all_sprites.add(self.treeobj)
        # create and add to groups floating sakuras
        for sa in SAKURAFLOS:
            s = sprites.ImObj(self.sakuras, *sa)
            self.all_sprites.add(s)
            self.saflos.add(s)
            self.objtomove.add(s)
        # create platforms and add the to groups
        for plat in PLATFORMS:
            p = sprites.Platforms(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
            self.objtomove.add(p)

    # function for drawing text on screen
    def draw_text(self, text, size, color, x, y):
        # sets the font
        font = pygame.font.Font(FONT, size)
        # renders the text
        textsurf = font.render(text, True, color)
        # text position on screen
        text_rect = textsurf.get_rect()
        text_rect.midtop = (x,y)
        # blits the text
        self.screen.blit(textsurf, text_rect)

    # start screen
    def start_screen(self):
        # writes on screen stuff about the game
        self.screen.fill(BLACK)
        self.draw_text(CAPTION, 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("arrows to move - space to jump", 22, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("press the space key to play", 22, WHITE, WIDTH/2, HEIGHT*3/4)
        pygame.display.flip()
        # waits the player to press a key to play
        self.wait_for_key()

    # function for start - end screen and
    # the starting and game background sounds.
    # to exit the loop the player has to press a key 
    def wait_for_key(self):
        # play music
        self.startscreen_sound.play(-1)
        waiting = True
        while waiting:
            # screen framerate
            self.clock.tick(30)
            # if player presses the close button
            # the game quits
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.done = True
                # if the player presses the space key
                # it creates a new game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # player pressing space to start playing sound,
                        # start screen and game bg music
                        self.startscreen_sound.stop()
                        self.gamestart_sound.play(0)
                        pygame.time.delay(3000)
                        self.bgsound.play(-1)
                        self.done = False
                        waiting = False


    # game over screen
    def game_over(self):
        # writes stuff on screen
        self.screen.fill(BLACK)
        self.draw_text("Game Over", 60, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("press the space key to play again", 22, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text("~"*30, 22, WHITE, WIDTH/2, HEIGHT*3/4)
        pygame.display.flip()
        # pause the game for 1500ms after winning
        pygame.time.delay(1500)
        # waits for the player to press a key 
        # it they want to play again
        self.wait_for_key()
