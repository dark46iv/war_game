import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Инопланетное вторжение")

    # Создание корабля, группы пришельцев и пуль
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # Создание флота пришельцев

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры.

    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        # Обновление движения пришельцев
        gf.update_aliens(ai_settings, aliens)

        # При каждом проходе цикла перерисовывается экран.
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


run_game()


