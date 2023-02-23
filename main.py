import pygame
import os
import sys

player = None
treasures = []
# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
treasure_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.tile_type = tile_type
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def set_image(self):
        self.image = tile_images[self.tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * self.pos_x, tile_height * self.pos_y)

    def set_color(self):
        self.image = load_image('black.jpg')
        self.rect = self.image.get_rect().move(
            tile_width * self.pos_x, tile_height * self.pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.x = pos_x
        self.y = pos_y
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def move_up(self):
        if self.y == 0:
            return True
        elif self.y - 1 > -1 and map_list[self.y - 1][self.x].tile_type == 'empty':
            self.y -= 1
            self.rect = self.image.get_rect().move(
                tile_width * self.x + 15, tile_height * self.y + 5)
            if self.y - 1 > -1:
                map_list[self.y - 1][self.x].set_image()
                if self.x - 1 > -1:
                    map_list[self.y - 1][self.x - 1].set_image()
                if self.x + 1 < len(map_list[0]):
                    map_list[self.y - 1][self.x + 1].set_image()
            if self.y + 2 < len(map_list):
                map_list[self.y + 2][self.x].set_color()
                if self.x - 1 > -1:
                    map_list[self.y + 2][self.x - 1].set_color()
                if self.x + 1 < len(map_list[0]):
                    map_list[self.y + 2][self.x + 1].set_color()
            for x in treasures:
                x.image = load_image('black.jpg')
                if abs(x.x - self.x) <= 1 and abs(x.y - self.y) <= 1:
                    x.set_image()
                if x.x - self.x == 0 and x.y - self.y == 0:
                    treasures.pop(treasures.index(x))
                    print(treasures)

    def move_down(self):
        if self.y == len(map_list) - 1:
            return True
        elif self.y + 1 < len(map_list) and map_list[self.y + 1][self.x].tile_type == 'empty':
            self.y += 1
            self.rect = self.image.get_rect().move(
                tile_width * self.x + 15, tile_height * self.y + 5)
            if self.y + 1 < len(map_list):
                map_list[self.y + 1][self.x].set_image()
                if self.x - 1 > -1:
                    map_list[self.y + 1][self.x - 1].set_image()
                if self.x + 1 < len(map_list[0]):
                    map_list[self.y + 1][self.x + 1].set_image()
            if self.y - 2 > -1:
                map_list[self.y - 2][self.x].set_color()
                if self.x - 1 > -1:
                    map_list[self.y - 2][self.x - 1].set_color()
                if self.x + 1 < len(map_list[0]):
                    map_list[self.y - 2][self.x + 1].set_color()
            for x in treasures:
                x.image = load_image('black.jpg')
                if abs(x.x - self.x) <= 1 and abs(x.y - self.y) <= 1:
                    x.set_image()
                if x.x - self.x == 0 and x.y - self.y == 0:
                    treasures.pop(treasures.index(x))
                    print(treasures)

    def move_left(self):
        if self.x == 0:
            return True
        elif self.x - 1 > -1 and map_list[self.y][self.x - 1].tile_type == 'empty':
            self.x -= 1
            self.rect = self.image.get_rect().move(
                tile_width * self.x + 15, tile_height * self.y + 5)
            if self.x - 1 > -1:
                map_list[self.y][self.x - 1].set_image()
                if self.y - 1 > -1:
                    map_list[self.y - 1][self.x - 1].set_image()
                if self.y + 1 < len(map_list[0]):
                    map_list[self.y + 1][self.x - 1].set_image()
            if self.x + 2 < len(map_list[0]):
                map_list[self.y][self.x + 2].set_color()
                if self.y - 1 > -1:
                    map_list[self.y - 1][self.x + 2].set_color()
                if self.y + 1 < len(map_list):
                    map_list[self.y + 1][self.x + 2].set_color()
            for x in treasures:
                x.image = load_image('black.jpg')
                if abs(x.x - self.x) <= 1 and abs(x.y - self.y) <= 1:
                    x.set_image()
                if x.x - self.x == 0 and x.y - self.y == 0:
                    treasures.pop(treasures.index(x))
                    print(treasures)

    def move_right(self):
        if self.x == len(map_list[0]):
            return True
        elif self.x + 1 < len(map_list[0]) and map_list[self.y][self.x + 1].tile_type == 'empty':
            self.x += 1
            self.rect = self.image.get_rect().move(
                tile_width * self.x + 15, tile_height * self.y + 5)
            if self.x + 1 < len(map_list[0]):
                map_list[self.y][self.x + 1].set_image()
                if self.y - 1 > -1:
                    map_list[self.y - 1][self.x + 1].set_image()
                if self.y + 1 < len(map_list[0]):
                    map_list[self.y + 1][self.x + 1].set_image()
            if self.x - 2 > -1:
                map_list[self.y][self.x - 2].set_color()
                if self.y - 1 > -1:
                    map_list[self.y - 1][self.x - 2].set_color()
                if self.y + 1 < len(map_list):
                    map_list[self.y + 1][self.x - 2].set_color()
            for x in treasures:
                x.image = load_image('black.jpg')
                if abs(x.x - self.x) <= 1 and abs(x.y - self.y) <= 1:
                    x.set_image()
                if x.x - self.x == 0 and x.y - self.y == 0:
                    treasures.pop(treasures.index(x))
                    print(treasures)


class Treasure(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(treasure_group, all_sprites)
        self.x = pos_x
        self.y = pos_y
        self.image = load_image('black.jpg')
        self.rect = self.image.get_rect().move(
            tile_width * self.x + 15, tile_height * self.y + 5)

    def set_image(self):
        self.image = treasure_image
        self.rect = self.image.get_rect().move(
            tile_width * self.x, tile_height * self.y)

    def set_color(self):
        self.image = load_image('black.jpg')
        self.rect = self.image.get_rect().move(
            tile_width * self.x, tile_height * self.y)


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    map_list = []
    for y in range(len(level)):
        arr = []
        for x in range(len(level[y])):
            if level[y][x] == '.':
                arr.append(Tile('empty', x, y))
                arr[x].set_color()
            elif level[y][x] == '#':
                arr.append(Tile('wall', x, y))
                arr[x].set_color()
            elif level[y][x] == '@':
                arr.append(Tile('empty', x, y))
                new_player = Player(x, y)
                arr[x].set_image()
            elif level[y][x] == 'T':
                arr.append(Tile('empty', x, y))
                treasures.append(Treasure(x, y))
                arr[x].set_color()
        map_list.append(arr)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y, map_list


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


FPS = 50
tile_images = {
    'wall': load_image('wall.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mario.png')
treasure_image = load_image('treasure.png')
tile_width = tile_height = 50


def terminate():
    pygame.quit()
    sys.exit()


level_complete = False


def start_screen():
    clock = pygame.time.Clock()
    intro_text = ["DARK DUNGEONS", "",
                  "Вы оказались в темном, очень темном подземелии...",
                  "Подземелье состоит из 3 залов, а каждый зал - из коридоров.",
                  "В каждом зале есть сокровища",
                  "Ваша задача - забрать все сокровища и выйти из подземелья",
                  "Вы можете видеть только объекты рядом."]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def end_screen():
    clock = pygame.time.Clock()
    intro_text = ["КОНЕЦ ИГРЫ"]
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    size = WIDTH, HEIGHT = 1000, 550
    screen = pygame.display.set_mode(size)
    start_screen()
    level = load_level('level_1.txt')
    player, level_x, level_y, map_list = generate_level(level)
    if player.x - 1 >= 0:
        map_list[player.y][player.x - 1].set_image()
    if player.x + 1 < len(map_list[0]):
        map_list[player.y][player.x + 1].set_image()
    if player.x + 1 < len(map_list[0]) and player.y - 1 > 0:
        map_list[player.y - 1][player.x + 1].set_image()
    if player.x - 1 > 0 and player.y - 1 > 0:
        map_list[player.y - 1][player.x - 1].set_image()
    if player.y - 1 > 0:
        map_list[player.y - 1][player.x].set_image()
    if player.x + 1 < len(map_list[0]) and player.y + 1 < len(map_list[0]):
        map_list[player.y + 1][player.x + 1].set_image()
    if player.x - 1 > 0 and player.y + 1 < len(map_list[0]):
        map_list[player.y + 1][player.x - 1].set_image()
    if player.y + 1 < len(map_list[0]):
        map_list[player.y + 1][player.x].set_image()
    while not (level_complete):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    level_complete = player.move_up()
                    if level_complete is None:
                        level_complete = False
                if event.key == pygame.K_DOWN:
                    level_complete = player.move_down()
                    if level_complete is None:
                        level_complete = False
                if event.key == pygame.K_RIGHT:
                    level_complete = player.move_right()
                    if level_complete is None:
                        level_complete = False
                if event.key == pygame.K_LEFT:
                    level_complete = player.move_left()
                    if level_complete is None:
                        level_complete = False
        screen.fill('white')
        tiles_group.draw(screen)
        player_group.draw(screen)
        treasure_group.draw(screen)
        pygame.display.flip()
    end_screen()
