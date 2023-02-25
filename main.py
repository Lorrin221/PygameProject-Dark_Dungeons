import pygame
import os
import sys
from random import choice

player = None
door = None
treasures = {}
map_list = []
fps = 30
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
treasure_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
FPS = 50
tile_images = {
    'wall': load_image('wall.png'),
    'empty': load_image('floor.jpg')
}
player_image = load_image('Mary_front.png')
treasure_image = load_image('treasure.png')
door_image = load_image('door.png')
tile_width = tile_height = 50

level_complete = False


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
        self.step = pygame.mixer.Sound('data\step.ogg')
        self.step_2 = pygame.mixer.Sound('data\step_2.ogg')
        self.step_3 = pygame.mixer.Sound('data\step_3.ogg')
        for x in treasures.keys():
            x.kill()
            if abs(x.x - self.x) <= 1 and abs(x.y - self.y) <= 1 and treasures[x]:
                x.add(treasure_group)
            if x.x - self.x == 0 and x.y - self.y == 0:
                x.kill()
                treasures[x] = False

    def set_image(self, image):
        self.image = image

    def move_up(self):
        if self.y == 0 and True not in treasures.values():
            return True
        elif self.y - door.y == 1 and self.x == door.x and not (door.bool):
            door.open()
        elif self.y - 1 > -1 and map_list[self.y - 1][self.x].tile_type == 'empty':
            choice([self.step, self.step_2, self.step_3]).play()
            self.y -= 1
            self.rect = self.image.get_rect().move(
                tile_width * self.x + 15, tile_height * self.y + 5)
            map_list[self.y][self.x].set_image()
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

    def move_down(self):
        if self.y == len(map_list) - 1 and True not in treasures.values():
            return True
        elif self.y - door.y == -1 and self.x == door.x and not (door.bool):
            door.open()
        elif self.y + 1 < len(map_list) and map_list[self.y + 1][self.x].tile_type == 'empty':
            choice([self.step, self.step_2, self.step_3]).play()
            self.y += 1
            self.rect = self.image.get_rect().move(
                tile_width * self.x + 15, tile_height * self.y + 5)
            map_list[self.y][self.x].set_image()
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

    def move_left(self):
        if self.x == 0 and True not in treasures.values():
            return True
        elif self.x - door.x == 1 and self.y == door.y and not (door.bool):
            door.open()
        elif self.x - 1 > -1 and map_list[self.y][self.x - 1].tile_type == 'empty':
            choice([self.step, self.step_2, self.step_3]).play()
            self.x -= 1
            self.rect = self.image.get_rect().move(
                tile_width * self.x + 15, tile_height * self.y + 5)
            map_list[self.y][self.x].set_image()
            if self.x - 1 > -1:
                map_list[self.y][self.x - 1].set_image()
                if self.y - 1 > -1:
                    map_list[self.y - 1][self.x - 1].set_image()
                if self.y + 1 < len(map_list):
                    map_list[self.y + 1][self.x - 1].set_image()
            if self.x + 2 < len(map_list[0]):
                map_list[self.y][self.x + 2].set_color()
                if self.y - 1 > -1:
                    map_list[self.y - 1][self.x + 2].set_color()
                if self.y + 1 < len(map_list):
                    map_list[self.y + 1][self.x + 2].set_color()

    def move_right(self):
        if self.x == len(map_list[0]) - 1 and True not in treasures.values():
            return True
        elif self.x - door.x == -1 and self.y == door.y and not (door.bool):
            door.open()
        elif self.x + 1 < len(map_list[0]) and map_list[self.y][self.x + 1].tile_type == 'empty':
            choice([self.step, self.step_2, self.step_3]).play()
            self.x += 1
            self.rect = self.image.get_rect().move(
                tile_width * self.x + 15, tile_height * self.y + 5)
            map_list[self.y][self.x].set_image()
            if self.x + 1 < len(map_list[0]):
                map_list[self.y][self.x + 1].set_image()
                if self.y - 1 > -1:
                    map_list[self.y - 1][self.x + 1].set_image()
                if self.y + 1 < len(map_list):
                    map_list[self.y + 1][self.x + 1].set_image()
            if self.x - 2 > -1:
                map_list[self.y][self.x - 2].set_color()
                if self.y - 1 > -1:
                    map_list[self.y - 1][self.x - 2].set_color()
                if self.y + 1 < len(map_list):
                    map_list[self.y + 1][self.x - 2].set_color()


class Treasure(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(treasure_group, all_sprites)
        self.x = pos_x
        self.y = pos_y
        self.image = treasure_image
        self.rect = self.image.get_rect().move(
            tile_width * self.x + 15, tile_height * self.y + 5)


class Door(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, door_group)
        self.x = pos_x
        self.y = pos_y
        self.sound_1 = pygame.mixer.Sound('data\door-opening.mp3')
        self.sound_2 = pygame.mixer.Sound('data\door-closed.mp3')
        self.bool = False
        self.image = door_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def open(self):
        if True in treasures.values():
            self.sound_2.play()
        else:
            self.sound_1.play()
            self.bool = True
            self.kill()


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку стенами ('#')
    return list(map(lambda x: x.ljust(max_width, '#'), level_map))


def generate_level(level):
    global door
    new_player, x, y = None, None, None
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
                treasures[Treasure(x, y)] = True
                arr[x].set_color()
            elif level[y][x] == 'D':
                arr.append(Tile('empty', x, y))
                door = Door(x, y)
                arr[x].set_color()
        map_list.append(arr)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y, map_list


def terminate():
    pygame.quit()
    sys.exit()


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


def run_level(level_name):
    global door
    global screen, size
    global map_list
    global player
    door = None
    map_list = []
    player = None
    f = pygame.font.Font(None, 20)
    level = load_level(level_name)
    level_complete = False
    player, level_x, level_y, map_list = generate_level(level)
    size = WIDTH, HEIGHT = (level_x + 1) * 50, (level_y + 1) * 50
    print(size)
    screen = pygame.display.set_mode(size)
    if player.x - 1 >= 0:
        map_list[player.y][player.x - 1].set_image()
    if player.x + 1 < len(map_list[0]):
        map_list[player.y][player.x + 1].set_image()
    if player.x + 1 < len(map_list[0]) and player.y - 1 >= 0:
        map_list[player.y - 1][player.x + 1].set_image()
    if player.x - 1 >= 0 and player.y - 1 >= 0:
        map_list[player.y - 1][player.x - 1].set_image()
    if player.y - 1 >= 0:
        map_list[player.y - 1][player.x].set_image()
    if player.x + 1 < len(map_list[0]) and player.y + 1 < len(map_list[0]):
        map_list[player.y + 1][player.x + 1].set_image()
    if player.x - 1 >= 0 and player.y + 1 < len(map_list[0]):
        map_list[player.y + 1][player.x - 1].set_image()
    if player.y + 1 < len(map_list[0]):
        map_list[player.y + 1][player.x].set_image()
    pygame.mixer.music.load('data\main_theme.ogg')
    pygame.mixer.music.play(-1)
    while not (level_complete):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.set_image(load_image('mary_back.png'))
                    level_complete = player.move_up()
                    if level_complete is None:
                        level_complete = False
                if event.key == pygame.K_DOWN:
                    player.set_image(load_image('mary_front.png'))
                    level_complete = player.move_down()
                    if level_complete is None:
                        level_complete = False
                if event.key == pygame.K_RIGHT:
                    player.set_image(load_image('Mary_right.png'))
                    level_complete = player.move_right()
                    if level_complete is None:
                        level_complete = False
                if event.key == pygame.K_LEFT:
                    player.set_image(load_image('mary_left.png'))
                    level_complete = player.move_left()
                    if level_complete is None:
                        level_complete = False
        text = f.render(f'Осталось сундуков: {list(treasures.values()).count(True)}', True, 'white')
        place = text.get_rect(
            center=(100, 50))
        screen.fill('white')
        tiles_group.draw(screen)
        player_group.draw(screen)
        treasure_group.draw(screen)
        door_group.draw(screen)
        for x in treasures:
            x.kill()
            if abs(x.x - player.x) <= 1 and abs(x.y - player.y) <= 1 and treasures[x]:
                x.add(treasure_group)
            if x.x - player.x == 0 and x.y - player.y == 0:
                x.kill()
                treasures[x] = False
        door.kill()
        if abs(door.x - player.x) <= 1 and abs(door.y - player.y) <= 1 and not (door.bool):
            door.add(door_group)
        screen.blit(text, place)
        if True not in treasures.values() and not (door.bool):
            door.open()
        pygame.display.flip()
        clock.tick(fps)
    pygame.mixer.music.stop()
    player.kill()
    for x in treasures:
        x.kill()
    return


def end_screen():
    pygame.init()
    clock = pygame.time.Clock()
    intro_text = ["КОНЕЦ ИГРЫ"]
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen = pygame.display.set_mode(size)
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
    run_level('level_1.txt')
    run_level('level_2.txt')
    end_screen()