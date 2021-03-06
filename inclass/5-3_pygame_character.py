# 파이게임 비 내리는 코드(클래스)
import pygame
import random

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 480 * 2  # 화면 높이
FPS = 60
CLOUD_NUMBER = 5
RAIN_NUMBER = 10
TITLE = '구름에서 비가 내리는 게임'
CHARACTER_SPEED = 5


class Player:
    def __init__(self, root):
        self.x = 100
        self.y = SCREEN_Y-200
        self.dx = 0
        self.dy = 0
        self.game = root
        self.image = self.game.player_image
        self.hit = 0

    def move(self, key):
        if key == pygame.K_UP:
            self.dy = -CHARACTER_SPEED
            self.dx = 0
        if key == pygame.K_DOWN:
            self.dy = CHARACTER_SPEED
            self.dx = 0
        if key == pygame.K_LEFT:
            self.dx = -CHARACTER_SPEED
            self.dy = 0
        if key == pygame.K_RIGHT:
            self.dx = CHARACTER_SPEED
            self.dy = 0

        if 0 < self.x < SCREEN_X:
            self.x += self.dx
        else:
            self.dx *= -1
            self.x += self.dx

        if 0 < self.y < SCREEN_Y:
            self.y += self.dy
        else:
            self.dy *= -1
            self.y += self.dy

    def draw(self):
        game.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, rain):
        return pygame.Rect(self.x, self.y, 108, 138).collidepoint((rain.x, rain.y))


class Rain:
    def __init__(self, x, y, root):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 28)
        self.bold = random.randint(1, 4)
        self.game = root
        self.len = random.randint(5, 15)
        self.color = pygame.Color('gray')

    def move(self):
        self.y += self.speed
        self.x += 4

    def off_screen(self):
        return self.y > SCREEN_Y

    def draw(self):
        pygame.draw.line(self.game.screen, self.color, (self.x, self.y), (self.x, self.y + self.len), self.bold)



class Cloud:
    def __init__(self, x, root):
        self.x = x
        self.y = random.randint(0, 200)
        self.image = root.image_cloud
        self.game = root
        self.speed = random.randint(3, 10)

    def move(self):
        self.x += self.speed
        if self.x > SCREEN_X:
            self.x = 0

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        for _ in range(RAIN_NUMBER):
            self.game.rains.append(Rain(self.x + random.randint(0, 130), self.y + 70, self.game))

    def click(self):
        pos = pygame.mouse.get_pos()
        rect = self.image.get_rect()
        rect.x = self.x
        rect.y = self.y
        return rect.collidepoint(pos)



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.load_data()
        self.rains = []
        self.clouds = []
        self.player = Player(self)

    def load_data(self):
        # 배경그림 불러오기
        self.image_background = pygame.image.load('../images/back.png').convert_alpha()
        self.image_background = pygame.transform.scale(self.image_background, (SCREEN_X, SCREEN_Y))
        # 구름그림 불러오기
        self.image_cloud = pygame.image.load('../images/cloud.svg').convert_alpha()
        # 플레이어 이미지 불러오기.
        self.player_image = pygame.image.load('../images/dino.png').convert_alpha()
        self.player_image = pygame.transform.scale(self.player_image, (260,200))

    def run(self):
        self.opening()
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()
        self.ending()

    def event(self):
        # 종료 코드 및 플레이어 움직임
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            # 마우스 버튼이 구름 클릭시 구름 제거
            if event.type == pygame.MOUSEBUTTONDOWN:
                for cloud in self.clouds:
                    if cloud.click():
                        self.clouds.remove(cloud)
                        del cloud
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.playing = False
                self.player.move(event.key)

    def update(self):
        # 구름 생성
        while len(self.clouds) < CLOUD_NUMBER:
            self.clouds.append(Cloud(random.randint(1, 20) * SCREEN_X / 20, self))
        # 구름에서 비 생성하고 구름 움직이기
        for cloud in self.clouds:
            cloud.rain()
            cloud.move()
        # 비를 움직이게 하고 화면 밖으로 가면 제거 하기
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain
        # 플레이어 움직임
        self.player.move(0)
        # 플레이어가 비 맞음 체크
        for rain in self.rains:
            if self.player.hit_by(rain):
                self.player.hit += 1
                self.rains.remove(rain)
                del rain
        print(self.player.hit)

    def draw(self):
        # self.screen.fill((255, 255, 255))
        # 배경화면 그리기
        self.screen.blit(self.image_background, (0, 0))
        # 구름 그리기
        for cloud in self.clouds:
            cloud.draw()
        # 비 그리기
        for rain in self.rains:
            rain.draw()
        # 플레이어 그리기
        self.player.draw()


game = Game()
game.run()
pygame.quit()
