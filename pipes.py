"""Трубы и управление препятствиями."""

import random

import pygame

from settings import (
    HEIGHT,
    PIPE_COLOR,
    PIPE_GAP,
    PIPE_MIN_HEIGHT,
    PIPE_SPEED,
    PIPE_WIDTH,
    WIDTH,
    PIPE_INTERVAL,
)


class PipePair:
    """Представляет две трубы с проходом между ними."""

    def __init__(self):
        """Создаёт трубы у правого края со случайной высотой прохода."""
        self.x = float(WIDTH)
        self.passed = False

        gap_top = random.randint(
            PIPE_MIN_HEIGHT,
            HEIGHT - PIPE_MIN_HEIGHT - PIPE_GAP,
        )

        self.top_rect = pygame.Rect(
            WIDTH, 0, PIPE_WIDTH, gap_top
        )
        self.bottom_rect = pygame.Rect(
            WIDTH,
            gap_top + PIPE_GAP,
            PIPE_WIDTH,
            HEIGHT - gap_top - PIPE_GAP,
        )

    def update(self, dt):
        """Перемещает обе трубы влево."""
        self.x -= PIPE_SPEED * dt
        self.top_rect.x = round(self.x)
        self.bottom_rect.x = round(self.x)

    def draw(self, screen):
        """Рисует верхнюю и нижнюю трубы."""
        pygame.draw.rect(screen, PIPE_COLOR, self.top_rect)
        pygame.draw.rect(screen, PIPE_COLOR, self.bottom_rect)


class PipeManager:
    """Управляет появлением труб и подсчётом очков."""

    def __init__(self):
        """Создаёт первую пару труб и обнуляет счёт."""
        self.pairs = [PipePair()]
        self.timer = 0
        self.score = 0

    def update(self, dt, bird_left):
        """Двигает трубы и начисляет очки за пройденные пары."""
        self.timer += dt

        while self.timer >= PIPE_INTERVAL:
            self.timer -= PIPE_INTERVAL
            self.pairs.append(PipePair())

        for pair in self.pairs:
            pair.update(dt)

            if not pair.passed and pair.top_rect.right < bird_left:
                pair.passed = True
                self.score += 1

        self.pairs = [
            pair for pair in self.pairs
            if pair.top_rect.right > 0
        ]

    def draw(self, screen):
        """Рисует все пары труб."""
        for pair in self.pairs:
            pair.draw(screen)

    def get_rects(self):
        """Возвращает прямоугольники всех труб для столкновений."""
        return [
            rect
            for pair in self.pairs
            for rect in (pair.top_rect, pair.bottom_rect)
        ]
