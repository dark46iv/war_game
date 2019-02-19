import pygame
from pygame.sprite import Sprite
import os


class Alien(Sprite):
    """Класс пришельца"""

    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает его начальную позицию"""

        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # загрузка изображение пришельца и назначение аттрибута rect
        self.image = pygame.image.load(os.path.abspath(os.curdir) + '/images/alien.bmp')
        self.rect = self.image.get_rect()

        # каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной позиции пришельца
        self.x = float(self.rect.x)

    def blitme(self):
        """Выводит позицию пришельца"""

        self.screen.blit(self.image, self.rect)
