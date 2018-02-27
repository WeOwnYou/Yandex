
import pytmx.util_pygame
import os
import pygame
import tile
def load_level(name):
    mapdata = pytmx.load_pygame(os.path.join('data/Maps',name+'.tmx'))
    print(mapdata.layers)
    tiles = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    for y in range(mapdata.height):
        for x in range(mapdata.width):
            image = mapdata.get_tile_image(x, y, 0)
            if image:
                image.set_alpha(None)
                block = tile.Tile(image)
                block.set_position((x*32, y*32))
                tiles.add(block)
            # print(image, end=' ')
        #print()

    for y in range(mapdata.height):
        for x in range(mapdata.width):
            image = mapdata.get_tile_image(x, y, 1)
            if image:
                image.set_alpha(None)
                block = tile.Obstacle(image)
                block.set_position((x*32, y*32))
                obstacles.add(block)
    for i in mapdata.objects:
        finish = i
    return mapdata, tiles, obstacles, finish