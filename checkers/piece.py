import pygame
from .constants import RED, WHITE, GREY, SQUARE_SIZE, CROWN

# The Piece class handles the specifics of individual pieces
class Piece:
    PADDING = 15
    OUTLINE = 5

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2  # dividing square_size by 2 to center piece in square
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING  # define size of piece
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)  # this is the outline of the piece
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    # this is a custom representation of the piece that we can output for debugging purposes if need be
    def __repr__(self):
        return str(self.color)
