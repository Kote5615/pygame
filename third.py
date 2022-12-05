import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.flag = False

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.flag is False:
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size),
                                     1)

                if self.flag is True:
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size),
                                     self.board[y][x])

    def get_cell(self, mouse_pos):
        board_width = self.width * self.cell_size
        board_height = self.height * self.cell_size
        if self.left < mouse_pos[0] < self.left + board_width:
            if self.top < mouse_pos[1] < self.top + board_height:
                cell_coords = (mouse_pos[1] - self.left) // self.cell_size, (mouse_pos[0] - self.top) // self.cell_size
                return cell_coords
        else:
            return None

    def color(self, cell):
        coorx, coory = cell[0], cell[1]
        for x in range(self.height):
            self.board[x][coory] = (self.board[x][coory] + 1) % 2
        for y in range(self.width):
            self.board[coorx][y] = (self.board[coorx][y] + 1) % 2
        self.board[coorx][coory] = (self.board[coorx][coory] + 1) % 2

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell != None:
            self.color(cell)
            self.flag = True
        # print(self.cell)





    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


if __name__ == '__main__':
    pygame.init()
    size = width, height = 700, 700

    screen = pygame.display.set_mode(size)
    board = Board(5, 7)
    board.set_view(100, 100, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render()
        pygame.display.flip()
    pygame.quit()
