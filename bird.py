"""Птица игрока и её движение."""

import pygame

from settings import (
    BIRD_COLOR,
    BIRD_HEIGHT,
    BIRD_START_X,
    BIRD_START_Y,
    BIRD_WIDTH,
    GRAVITY,
    JUMP_SPEED,
    HEIGHT,
)


class Bird:
    """Представляет птицу, падающую под действием тяжести."""

    def __init__(self):
        """Задаёт начальное положение и скорость птицы."""
        self.y = BIRD_START_Y
        self.velocity = 0
        self.rect = pygame.Rect(0, 0, BIRD_WIDTH, BIRD_HEIGHT)
        self.rect.center = (BIRD_START_X, round(self.y))

    def jump(self):
        """Задаёт скорость движения вверх."""
        self.velocity = JUMP_SPEED

    def update(self, dt):
        """Обновляет скорость и положение с учётом времени."""
        self.velocity += GRAVITY * dt
        self.y += self.velocity * dt
        self.rect.centery = round(self.y)

    def hits_boundary(self):
        """Проверяет касание верхней или нижней границы окна."""
        return self.rect.top <= 0 or self.rect.bottom >= HEIGHT

    def draw(self, screen):
        """Рисует птицу в виде жёлтого овала."""
        pygame.draw.ellipse(screen, BIRD_COLOR, self.rect)

    def hits_pipes(self, pipe_rects):
        """Проверяет столкновение птицы с трубами."""
        return self.rect.collidelist(pipe_rects) != -1
