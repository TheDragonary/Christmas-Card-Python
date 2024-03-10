import pygame

# Initialise Pygame
pygame.init()

# Set clock variable
clock = pygame.time.Clock()

# Set up screen resolution
WIDTH = 500
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Set font variable and choose font and font size
font = pygame.font.SysFont("Comic Sans MS", 30)

# Load and play music
pygame.mixer.music.load("assets/Rockin' Around The Christmas Tree.mp3")
pygame.mixer.music.play()

# Creates "To:" input box
toText= ' '
toInput = pygame.Rect(90, 275, 200, 40)
toActive = False

# Creates "From:" input box
fromText= ' '
fromInput = pygame.Rect(90, 325, 200, 40)
fromActive = False

# Sets the number of which snowflakes frame to load
sf_num = 1
snowflakes = pygame.image.load(f"assets/snowflakes/sf{sf_num}.png")

# Create angle variable for rotation
angle = 0

# Function to rotate an image
def blitRotate(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)

# Sets variables for Santa's position and speed
santa_x = 260
santa_y = 300
santa_speed_x = 20
santa_speed_y = 20

# Sets X position for the reindeer and speed
reindeer_x = -5
reindeer_speed_x = 50

# Cat initial position, speed, and jump variables
cat_y = 350
cat_speed_y = 0
gravity = 1
jump = 10
on_ground = True

# Main loop
running = True
while running:
    # Sets FPS to 60
    clock.tick(60)

    # Creates events
    for event in pygame.event.get():
        # Quits game when running is set to False
        if event.type == pygame.QUIT:
            running = False
        # For when the user clicks on the "To:" or "From:" input boxes to type
        if event.type == pygame.MOUSEBUTTONDOWN:
            if toInput.collidepoint(event.pos):
                toActive = True
            else:
                toActive = False
            if fromInput.collidepoint(event.pos):
                fromActive = True
            else:
                fromActive = False
        # Allows the user to delete characters in the input boxes
        if event.type == pygame.KEYDOWN:
            if toActive == True:
                if event.key == pygame.K_BACKSPACE:
                    toText = toText[:-1]
                else:
                    toText += event.unicode
            if fromActive == True:
                if event.key == pygame.K_BACKSPACE:
                    fromText = fromText[:-1]
                else:
                    fromText += event.unicode

    # Sets the background to a light red colour
    screen.fill((255, 200, 200))

    # Initialises the font
    pygame.font.init()

    # Loads the images for santa, decoration, merry christmas image, reindeer, cat and turkey
    # And sets the image size for each
    santa = pygame.image.load("assets/santa.png").convert_alpha()
    santa = pygame.transform.smoothscale(santa, (santa.get_width()/3,santa.get_height()/3))

    decoration = pygame.image.load("assets/decoration.png")

    christmas = pygame.image.load("assets/merrychristmas.png").convert_alpha()
    christmas = pygame.transform.smoothscale(christmas, (christmas.get_width()/6,christmas.get_height()/6))

    reindeer = pygame.image.load("assets/reindeer.png").convert_alpha()
    reindeer = pygame.transform.smoothscale(reindeer, (reindeer.get_width()/1.5, reindeer.get_height()/1.5))

    cat = pygame.image.load("assets/christmascat.png").convert_alpha()
    cat = pygame.transform.smoothscale(cat, (cat.get_width()/2, cat.get_height()/2))

    turkey = pygame.image.load("assets/turkey.png").convert_alpha()
    turkey = pygame.transform.smoothscale(turkey, (turkey.get_width()/3, turkey.get_height()/3))

    # Set the rotation speed for the turkey
    angle += 30

    # Make Santa's position change by the speed variables set earlier
    santa_x += santa_speed_x
    santa_y += santa_speed_y

    # Make the reindeer move horizontally by the number set to the speed variable
    reindeer_x += reindeer_speed_x

    # Apply gravity to the cat
    cat_speed_y += gravity * 2
    cat_y += cat_speed_y * 4

    # Check if the cat is on the ground
    if cat_y >= 350:
        cat_y = 350
        cat_speed_y = 0
        on_ground = True

    # Check if the cat is on the ground, then jump
    if on_ground:
        cat_speed_y = -jump
        on_ground = False

    # Draws each image to the screen and sets their positions
    screen.blit(decoration, (0,-100))
    screen.blit(santa, (santa_x,santa_y))
    screen.blit(christmas, (180,25))
    screen.blit(cat, (275,cat_y))
    blitRotate(screen, turkey, (100,420), angle) # blitRotate function draws and sets the rotation
    screen.blit(reindeer, (reindeer_x,410))

    # If Santa hits the borders of the screen, the speed is multiplied by -1 so it changes direction
    if santa_x + santa.get_width() > WIDTH or santa_x < 0:
        santa_speed_x *= -1
    if santa_y + santa.get_height() > HEIGHT or santa_y < 0:
        santa_speed_y *= -1

    # If the reindeer cross the right side of the screen, it will be moved back behind the left side
    # It is set to 0 minus the width of the reindeer image, so it looks like it moves back around
    # Instead of suddenly teleporting
    if reindeer_x > WIDTH:
        reindeer_x = 0 - reindeer.get_width()

    # Animates the snowflakes frames, when it passes 4, sf_num will be reset to the first frame and repeat
    sf_num += 1
    if sf_num > 4:
        sf_num = 1
    
    # This loads each snowflakes frame and draws it to the screen
    snowflakes = pygame.image.load(f"assets/snowflakes/sf{sf_num}.png")
    snowflakes = pygame.transform.scale(snowflakes, (snowflakes.get_width()*3, snowflakes.get_height()*3))
    screen.blit(snowflakes, (0,0))

    # Draws the "To:" text and input box
    pygame.draw.rect(screen, (0, 0, 0), toInput, 2)
    toSurface = font.render(toText, True, (0, 0, 0))
    screen.blit(toSurface,(toInput.x, toInput.y - 5))
    text1 = font.render("To:", True, (0, 0, 0))
    screen.blit(text1, (40,275))

    # Draws the "From:" text and input box
    pygame.draw.rect(screen, (0, 0, 0), fromInput, 2)
    fromSurface = font.render(fromText, True, (0, 0, 0))
    screen.blit(fromSurface,(fromInput.x, fromInput.y - 5))
    text2 = font.render("From:", True, (0, 0, 0))
    screen.blit(text2, (5,325))

    # Draws the "Happy New Year" text to the screen
    # text3 = font.render("Happy New Year", True, (0, 0, 0), (255, 200, 200))
    # text4 = font.render("2024", True, (0, 0, 0), (255, 200, 200))
    # screen.blit(text3, (WIDTH/2 - text3.get_width()/2, 12))
    # screen.blit(text4, (WIDTH/2 - text4.get_width()/2, 52))

    # Updates the screen
    pygame.display.flip()

# Quits Pygame when you break out of the main loop
pygame.quit()