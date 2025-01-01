from Source import shader
# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()

clock = pygame.time.Clock()
running = True
dt = 0



player_pos = pygame.Vector2(shader.screen.get_width() / 4 * 3, shader.screen.get_height() / 4)
render_priority = 0

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    shader.clearScreen()
    
    shader.drawObject(pygame.Vector2(100, 100), player_pos, "Assets/Textures/test")

    
        
    pygame.draw.circle(shader.screen, "red", player_pos, 40)
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(30) / 1000

pygame.quit()