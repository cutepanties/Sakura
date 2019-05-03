# Sakura settings

# Window caption
CAPTION = "Sakura"

# Colors
WHITE = (255,255,255)
PINK = (255,100,255)
BLACK = (8,10,25)

# Window width and height
WIDTH = 900
HEIGHT = 600

# Filenames
STATIC = 'minkie/static.png'
JUMP1 = 'minkie/jump2.png'
WALK1 = 'minkie/walk1.png'
WALK2 = 'minkie/walk2.png'
SAFLO = 'stuff/saflo.png'
FONT = 'stuff/Mario-Kart-DS.ttf'
TREE = 'stuff/tree.png'
SNOWSA = ['stuff/sakback/frame_00.png', 'stuff/sakback/frame_01.png',
          'stuff/sakback/frame_02.png', 'stuff/sakback/frame_03.png',
          'stuff/sakback/frame_04.png', 'stuff/sakback/frame_05.png',
          'stuff/sakback/frame_06.png', 'stuff/sakback/frame_07.png',
          'stuff/sakback/frame_08.png', 'stuff/sakback/frame_09.png',
          'stuff/sakback/frame_10.png', 'stuff/sakback/frame_11.png',
          'stuff/sakback/frame_12.png', 'stuff/sakback/frame_13.png',
          'stuff/sakback/frame_14.png', 'stuff/sakback/frame_15.png',
          'stuff/sakback/frame_16.png', 'stuff/sakback/frame_17.png',
          'stuff/sakback/frame_18.png', 'stuff/sakback/frame_19.png']
STARTSOUND = 'sound-files/startscreen.wav'
ENEMYSOUND = 'sound-files/spyrosbip.mp3'
GAMESTARTSOUND = 'sound-files/go.wav'
STEPS = 'sound-files/step-floor.wav'
JUMPSOUND = 'sound-files/jumping.wav'
BGSOUND = 'sound-files/the_field_of_dreams.wav'


# Player starting position
STARTX = 50
STARTY = 300

# Player movement
GRAVITY = 0.5
PLAYER_ACCEL = 0.3
PLAYER_FRICT = -0.12

# Platforms
PLAT_WIDTH = 150
PLAT_HEIGHT = 20
GROUND_PLAT = (0, 4/5*HEIGHT, 3000, HEIGHT/5)
PLATFORMS = [(WIDTH/2, 310, PLAT_WIDTH, PLAT_HEIGHT),
            (150, 240, PLAT_WIDTH, PLAT_HEIGHT),
            (650, 160, PLAT_WIDTH, PLAT_HEIGHT),
            (1010, 145, PLAT_WIDTH, PLAT_HEIGHT),
            (1140, 250, PLAT_WIDTH, PLAT_HEIGHT),
            (1410, 180, PLAT_WIDTH, PLAT_HEIGHT),
            (1635, 249, PLAT_WIDTH, PLAT_HEIGHT),
            (1735, 365, PLAT_WIDTH, PLAT_HEIGHT),
            (1900, 150, PLAT_WIDTH, PLAT_HEIGHT),
            (2260, 240, PLAT_WIDTH, PLAT_HEIGHT),
            (2440, 150, PLAT_WIDTH, PLAT_HEIGHT),
            (2600, 290, PLAT_WIDTH, PLAT_HEIGHT)]

# Positions of sakura trees
SAKURAFLOS = [(175, 240), (255, 240), (443, 480), (655, 160),
             (1020, 145), (1080, 480), (1145, 250), (1415, 180),
             (1500, 480), (1640, 249), (1700, 480), (1740, 365),
             (1815, 480), (1970, 480), (2270, 240), (2450, 150)]
