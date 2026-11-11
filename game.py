"""Окно и основной цикл игры."""

import pygame

from settings import BACKGROUND_COLOR, FPS, HEIGHT, WIDTH


class Game:
    """Управляет окном и игровым циклом."""

    def __init__(self):
        """Создаёт окно и часы для ограничения частоты кадров."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        """Обрабатывает события и рисует фон."""
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(BACKGROUND_COLOR)
            pygame.display.flip()

        pygame.quit()
