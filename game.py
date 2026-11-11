"""Окно и основной цикл игры."""

import pygame

from bird import Bird
from pipes import PipeManager
from settings import (
    BACKGROUND_COLOR,
    FONT_SIZE,
    FPS,
    HEIGHT,
    MESSAGE_LINE_SPACING,
    SCORE_MARGIN,
    TEXT_COLOR,
    WIDTH,
)


class Game:
    """Управляет окном и игровым циклом."""

    def __init__(self):
        """Создаёт окно и начальные объекты игры."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.running = True
        self.bird = Bird()
        self.pipes = PipeManager()
        self.game_over = False
        self.font = pygame.font.Font(None, FONT_SIZE)

    def draw_game_over(self):
        """Рисует сообщение о проигрыше и подсказку перезапуска."""
        messages = (
            "Игра окончена",
            "Нажмите R для новой игры",
        )

        for index, message in enumerate(messages):
            text = self.font.render(message, True, TEXT_COLOR)
            position = (
                WIDTH // 2,
                HEIGHT // 2 + index * MESSAGE_LINE_SPACING,
            )
            self.screen.blit(text, text.get_rect(center=position))

    def run(self):
        """Обрабатывает движение, проигрыш и перезапуск игры."""
        while self.running:
            dt = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.game_over:
                            self.bird.jump()

                    elif event.key == pygame.K_r:
                        if self.game_over:
                            self.bird = Bird()
                            self.pipes = PipeManager()
                            self.game_over = False

            if not self.game_over:
                self.bird.update(dt)
                self.pipes.update(dt, self.bird.rect.left)

                if (
                    self.bird.hits_boundary()
                    or self.bird.hits_pipes(self.pipes.get_rects())
                ):
                    self.game_over = True

            self.screen.fill(BACKGROUND_COLOR)
            self.pipes.draw(self.screen)
            self.bird.draw(self.screen)

            score_text = self.font.render(
                f"Очки: {self.pipes.score}", True, TEXT_COLOR
            )
            self.screen.blit(
                score_text, (SCORE_MARGIN, SCORE_MARGIN)
            )

            if self.game_over:
                self.draw_game_over()

            pygame.display.flip()

        pygame.quit()
