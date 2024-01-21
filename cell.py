import pygame


class Cell:
    def __init__(self, value, row, col, screen, state):
        # Initialize a Cell instance with stated parameters
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.select = False  # Shows if the cell is selected
        self.width = 75
        self.height = 75
        self.state = state # Differentiates permanent, sketched, and entered values
        self.sketch = False # For if cell can be sketched in draw
        self.read_to_ret = False
        self.sketch_value = 0

    def set_cell_value(self, value):
        # Assign the cell a numerical value
        self.value = value

    def sketched_value(self, value):
        # Set the sketched value of the cell
        self.sketch_value = value

    def draw(self, state):
        # State 1 is permanent, state 2 is sketched, state 3 is entered, state 4 is just 0 value
        x_plane = self.col * self.width
        y_plane = self.row * self.height
        # Randomly generated numbers
        if self.value != 0:  # If value does not equal 0 show value
            text_font = pygame.font.Font(None, 36)
            text_surf = text_font.render(str(self.value), True, (0,0,0))
            text_rect = text_surf.get_rect(center=(x_plane + self.width//2, y_plane + self.height//2))
            self.screen.blit(text_surf, text_rect)
        if self.value == 0:
            self.state = 4
        # Outline in red
        if self.select:  # Outlines the cell in red if true
            if self.state != 0:
                pygame.draw.rect(self.screen, (255, 0, 0), (x_plane, y_plane, self.width, self.height), 4)
                self.sketch = True
        # Sketch value small in corner and blue
        if self.sketch == True and self.sketch_value != 0:
            text_font = pygame.font.Font(None, 29)
            text_surf = text_font.render(str(self.sketch_value), True, (0, 0, 255))
            text_rect = text_surf.get_rect(center=((x_plane + self.width // 2) - 15, (y_plane + self.height // 2) - 15))
            self.screen.blit(text_surf, text_rect)
        # When state is 3 (entered value), fill cell with white
        if self.state == 3:
            pygame.draw.rect(self.screen, (255, 255, 245), (x_plane+5, y_plane+5, self.width-10, self.height-11))
            if self.sketch_value != 0:
                text_font = pygame.font.Font(None, 36)
                text_surf = text_font.render(str(self.sketch_value), True, (0, 0, 0))
                text_rect = text_surf.get_rect(center=((x_plane + self.width // 2)-3, (y_plane + self.height // 2) - 3))
                self.screen.blit(text_surf, text_rect)
                # Relines orange for unselect
                pygame.draw.rect(self.screen, (245, 152, 66), (x_plane, y_plane, self.width, self.height), 4)
        # When enter sketched value normal in blue center
        if self.value != 0 and self.state == 2:
            text_font = pygame.font.Font(None, 36)
            text_surf = text_font.render(str(self.value), True, (0, 0, 255))
            text_rect = text_surf.get_rect(center=(x_plane + self.width // 2, y_plane + self.height // 2))
            self.screen.blit(text_surf, text_rect)
        # Deletes value in cell
        if self.value == 0 and self.sketched_value == 0 and self.state == 4:
            pygame.draw.rect(self.screen, (255, 255, 245),(x_plane + 5, y_plane + 5, self.width - 10, self.height - 11))
            if self.sketch == True and self.sketch_value != 0:  # Returns back to the sketch state
                text_font = pygame.font.Font(None, 29)
                text_surf = text_font.render(str(self.sketch_value), True, (0, 0, 255))
                text_rect = text_surf.get_rect(
                    center=((x_plane + self.width // 2) - 15, (y_plane + self.height // 2) - 15))
                self.screen.blit(text_surf, text_rect)
