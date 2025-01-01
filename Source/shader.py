import pygame
import math

screen = pygame.display.set_mode((1440, 900), pygame.FULLSCREEN)
backgroundColor = (169, 191, 168)

def clearScreen():
    screen.fill(backgroundColor)

def normalize(vec):
    length = math.sqrt(vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2)
    return (vec[0] / length, vec[1] / length, vec[2] / length)

# Lighting calculations
def apply_lighting(diffuse, normal, light_dir, sun):
    width, height = diffuse.get_size()
    lit_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    for y in range(height):
        for x in range(width):
            # Get the pixel colors from the textures
            d_color = diffuse.get_at((x, y))  # Diffuse color
            n_color = normal.get_at((x, y))  # Normal map color

            # Convert normal map RGB to a direction vector
            n = normalize(((n_color.r / 255.0) * 2 - 1, (n_color.g / 255.0) * 2 - 1, (n_color.b / 255.0) * 2 - 1))

            # Calculate dot product between normal and light direction
            intensity = max(0, n[0] * light_dir[0] + n[1] * light_dir[1] + n[2] * light_dir[2]) * 0.75

            # Apply lighting to diffuse color
            if sun:
                lit_color = (
                min(255, int(d_color.r * intensity)),
                min(255, int(d_color.g * intensity)),
                min(255, int(d_color.b * intensity)) * 0.8,
                d_color.a
            )
            else:
                lit_color = (
                    min(255, int(d_color.r * intensity)),
                    min(255, int(d_color.g * intensity)),
                    min(255, int(d_color.b * intensity)) * 0.8,
                    d_color.a
                )

            # Set the pixel on the lit surface
            lit_surface.set_at((x, y), lit_color)

    return lit_surface



def drawObject(obj_pos, light_pos, path,):
    diffuse_texture = pygame.image.load(path + ".png").convert_alpha()
    normal_map = pygame.image.load(path + "_normal.png").convert_alpha()

    light_dir = normalize(((-1) * (obj_pos.x - light_pos.x), (obj_pos.y - light_pos.y), 1))
    lit_texture = apply_lighting(diffuse_texture, normal_map, light_dir, "sun")
    
    screen.blit(lit_texture, obj_pos)
    