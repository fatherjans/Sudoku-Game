import pygame, sys
from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator
import copy


# Draws the game start screen, title, and difficulty level buttons
def draw_game_start(screen):
    # Background color
    background_color = (255, 255, 245)  # Turns background white
    screen.fill(background_color)

    # Initialize title font/color
    start_title_font = pygame.font.Font(None, 100)
    sub_text_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 50)
    text_color = (245, 152, 66)  # Turns text orange

    # Initialize and draw main title
    title_surf = start_title_font.render("Welcome to Sudoku", 0, text_color)
    title_rect = title_surf.get_rect(center=(337, 300))  # Positions the title text (shift if needed)
    screen.blit(title_surf, title_rect)  # Places the title

    # Initialize and draw sub-text
    title_surf = sub_text_font.render("Select Game Mode", 0, text_color)
    title_rect = title_surf.get_rect(center=(337, 400))  # Positions the title text (shift if needed)
    screen.blit(title_surf, title_rect)  # Places the title

    # Easy button
    pygame.draw.line(screen, (245, 152, 66), (50, 500), (200, 500), 8)
    pygame.draw.line(screen, (245, 152, 66), (50, 560), (200, 560), 8)
    pygame.draw.line(screen, (245, 152, 66), (50, 500), (50, 560), 8)
    pygame.draw.line(screen, (245, 152, 66), (200, 500), (200, 560), 8)
    button_font = pygame.font.Font(None, 36)
    button_surf = button_font.render('Easy', 0, (245, 152, 66))
    button_rect = button_surf.get_rect(center=(125, 530))
    screen.blit(button_surf, button_rect)

    # Medium button
    pygame.draw.line(screen, (245, 152, 66), (250, 500), (400, 500), 8)
    pygame.draw.line(screen, (245, 152, 66), (250, 560), (400, 560), 8)
    pygame.draw.line(screen, (245, 152, 66), (250, 500), (250, 560), 8)
    pygame.draw.line(screen, (245, 152, 66), (400, 500), (400, 560), 8)
    button_font = pygame.font.Font(None, 36)
    button_surf = button_font.render('Medium', 0, (245, 152, 66))
    button_rect = button_surf.get_rect(center=(325, 530))
    screen.blit(button_surf, button_rect)

    # Hard button
    pygame.draw.line(screen, (245, 152, 66), (450, 500), (600, 500), 8)
    pygame.draw.line(screen, (245, 152, 66), (450, 560), (600, 560), 8)
    pygame.draw.line(screen, (245, 152, 66), (450, 500), (450, 560), 8)
    pygame.draw.line(screen, (245, 152, 66), (600, 500), (600, 560), 8)
    button_font = pygame.font.Font(None, 36)
    button_surf = button_font.render('Hard', 0, (245, 152, 66))
    button_rect = button_surf.get_rect(center=(525, 530))
    screen.blit(button_surf, button_rect)

    # Handle user input when selecting difficulty level
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 500 <= y <= 560:
                    # Conditions for clicking difficulty level buttons
                    if 50 <= x <= 200:
                        return 30
                    elif 250 <= x <= 400:
                        return 40
                    elif 450 <= x <= 600:
                        return 50
        pygame.display.update()


# Similar formatting to draw_game_start
def draw_game_over(screen, SG1, save_for_sol):
    screen.fill((255, 255, 245))
    # Check if player won
    if SG1.check_board(save_for_sol) == True:
        # If won display game won msg
        end_title_font = pygame.font.Font(None, 100)
        title_surf = end_title_font.render('Game Won!', 0, (245, 152, 66))

        # Exit button
        pygame.draw.line(screen, (245, 152, 66), (250, 500), (400, 500), 8)
        pygame.draw.line(screen, (245, 152, 66), (250, 560), (400, 560), 8)
        pygame.draw.line(screen, (245, 152, 66), (250, 500), (250, 560), 8)
        pygame.draw.line(screen, (245, 152, 66), (400, 500), (400, 560), 8)

        button_font = pygame.font.Font(None, 36)
        button_surf = button_font.render('Exit', 0, (245, 152, 66))
        button_rect = button_surf.get_rect(center=(325, 530))
        screen.blit(button_surf, button_rect)
    
    # Check if player lost
    elif SG1.check_board(save_for_sol) == False:
        # If lost display game over msg
        end_title_font = pygame.font.Font(None, 70)
        title_surf = end_title_font.render('Game Over! Did not win!', 0, (245, 152, 66))
        title_rect = title_surf.get_rect(center=(675 // 2, 675 // 2 - 150))
        screen.blit(title_surf, title_rect)

        # Button for restart
        pygame.draw.line(screen, (245, 152, 66), (250, 500), (400, 500), 8)
        pygame.draw.line(screen, (245, 152, 66), (250, 560), (400, 560), 8)
        pygame.draw.line(screen, (245, 152, 66), (250, 500), (250, 560), 8)
        pygame.draw.line(screen, (245, 152, 66), (400, 500), (400, 560), 8)
        button_font = pygame.font.Font(None, 36)
        button_surf = button_font.render('Restart', 0, (245, 152, 66))
        button_rect = button_surf.get_rect(center=(325, 530))
        screen.blit(button_surf, button_rect)

    else:
        # If neither won or lost display game over! did not win! msg
        end_title_font = pygame.font.Font(None, 70)
        title_surf = end_title_font.render('Game Over! Did not win!', 0, (245, 152, 66))

    # Center the title on the screen
    title_rect = title_surf.get_rect(center=(675 // 2, 675 // 2 - 150))
    screen.blit(title_surf, title_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            # Quit event: close the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Check if the click is within the restart button area
                if 500 <= y <= 560:
                    # Restart button action
                    if 250 <= x <= 400:
                        if SG1.check_board(save_for_sol) == True:
                            pygame.quit()
                            sys.exit()
                        elif SG1.check_board(save_for_sol) is False:
                            # Draw game start screen
                            removed_cells = draw_game_start(screen)
                            # Initialize new game components
                            screen.fill((255, 255, 245))
                            Board1 = Board(675, 675, screen, 1)
                            SG1 = SudokuGenerator(9, removed_cells)
                            SG1.fill_values()
                            SG1.remove_cells()
                            save_for_reset = copy.deepcopy(SG1.board)
                            # Draw cells on board
                            for r in range(0, 9):
                                for c in range(0, 9):
                                    Cell1 = Cell(SG1.get_board()[r][c], r, c, screen, None)
                                    Cell1.draw(None)

                            # Button for reset
                            pygame.draw.line(screen, (245, 152, 66), (50, 705), (200, 705), 8)
                            pygame.draw.line(screen, (245, 152, 66), (50, 765), (200, 765), 8)
                            pygame.draw.line(screen, (245, 152, 66), (50, 705), (50, 765), 8)
                            pygame.draw.line(screen, (245, 152, 66), (200, 705), (200, 765), 8)
                            button_font = pygame.font.Font(None, 36)
                            button_surf = button_font.render('Reset', 0, (245, 152, 66))
                            button_rect = button_surf.get_rect(center=(125, 735))
                            screen.blit(button_surf, button_rect)

                            # Button for restart
                            pygame.draw.line(screen, (245, 152, 66), (250, 705), (400, 705), 8)
                            pygame.draw.line(screen, (245, 152, 66), (250, 765), (400, 765), 8)
                            pygame.draw.line(screen, (245, 152, 66), (250, 705), (250, 765), 8)
                            pygame.draw.line(screen, (245, 152, 66), (400, 705), (400, 765), 8)
                            button_font = pygame.font.Font(None, 36)
                            button_surf = button_font.render('Restart', 0, (245, 152, 66))
                            button_rect = button_surf.get_rect(center=(325, 735))
                            screen.blit(button_surf, button_rect)

                            # Button for exit
                            pygame.draw.line(screen, (245, 152, 66), (450, 705), (600, 705), 8)
                            pygame.draw.line(screen, (245, 152, 66), (450, 765), (600, 765), 8)
                            pygame.draw.line(screen, (245, 152, 66), (450, 705), (450, 765), 8)
                            pygame.draw.line(screen, (245, 152, 66), (600, 705), (600, 765), 8)
                            button_font = pygame.font.Font(None, 36)
                            button_surf = button_font.render('Exit', 0, (245, 152, 66))
                            button_rect = button_surf.get_rect(center=(525, 735))
                            screen.blit(button_surf, button_rect)

                            # Reset game state variables
                            player = 1
                            game_over = False
                            can_type = False
                            ready_for_ret = False
                            arrow_press = False
                            correct_index = False
                            winner = 0
                            Cell1 = None
                            # Draw the game board
                            Board1.draw()
                            continue

        pygame.display.update()  # Update display

# Main game initialization
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((675, 775))
    pygame.display.set_caption('Sudoku')
    removed_cells = draw_game_start(screen)
    screen.fill((255, 255, 245))
    Board1 = Board(675, 675, screen, 1)
    SG1 = SudokuGenerator(9, removed_cells)
    SG1.fill_values()
    save_for_sol = copy.deepcopy(SG1.board)
    SG1.remove_cells()
    save_for_reset = copy.deepcopy(SG1.board)
    for r in range(0, 9):
        for c in range(0, 9):
            Cell1 = Cell(SG1.get_board()[r][c], r, c, screen, None)
            Cell1.draw(None)
            
    # Button for reset
    pygame.draw.line(screen, (245, 152, 66), (50, 705), (200, 705), 8)
    pygame.draw.line(screen, (245, 152, 66), (50, 765), (200, 765), 8)
    pygame.draw.line(screen, (245, 152, 66), (50, 705), (50, 765), 8)
    pygame.draw.line(screen, (245, 152, 66), (200, 705), (200, 765), 8)
    button_font = pygame.font.Font(None, 36)
    button_surf = button_font.render('Reset', 0, (245, 152, 66))
    button_rect = button_surf.get_rect(center=(125, 735))
    screen.blit(button_surf, button_rect)

    # Button for restart
    pygame.draw.line(screen, (245, 152, 66), (250, 705), (400, 705), 8)
    pygame.draw.line(screen, (245, 152, 66), (250, 765), (400, 765), 8)
    pygame.draw.line(screen, (245, 152, 66), (250, 705), (250, 765), 8)
    pygame.draw.line(screen, (245, 152, 66), (400, 705), (400, 765), 8)
    button_font = pygame.font.Font(None, 36)
    button_surf = button_font.render('Restart', 0, (245, 152, 66))
    button_rect = button_surf.get_rect(center=(325, 735))
    screen.blit(button_surf, button_rect)

    # Button for exit
    pygame.draw.line(screen, (245, 152, 66), (450, 705), (600, 705), 8)
    pygame.draw.line(screen, (245, 152, 66), (450, 765), (600, 765), 8)
    pygame.draw.line(screen, (245, 152, 66), (450, 705), (450, 765), 8)
    pygame.draw.line(screen, (245, 152, 66), (600, 705), (600, 765), 8)
    button_font = pygame.font.Font(None, 36)
    button_surf = button_font.render('Exit', 0, (245, 152, 66))
    button_rect = button_surf.get_rect(center=(525, 735))
    screen.blit(button_surf, button_rect)

    player = 1
    game_over = False
    can_type = False
    ready_for_ret = False
    arrow_press = False
    correct_index = False
    winner = 0
    Cell1 = None
    Board1.draw()

    # Main game loop for user input and event handling
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                # Condition for clicking on buttons on bottom
                if 705 <= y <= 765:
                    # Condition for reset
                    if 50 <= x <= 200:
                        screen.fill((255, 255, 245))
                        Board1.draw()
                        # Button for reset
                        pygame.draw.line(screen, (245, 152, 66), (50, 705), (200, 705), 8)
                        pygame.draw.line(screen, (245, 152, 66), (50, 765), (200, 765), 8)
                        pygame.draw.line(screen, (245, 152, 66), (50, 705), (50, 765), 8)
                        pygame.draw.line(screen, (245, 152, 66), (200, 705), (200, 765), 8)
                        button_font = pygame.font.Font(None, 36)
                        button_surf = button_font.render('Reset', 0, (245, 152, 66))
                        button_rect = button_surf.get_rect(center=(125, 735))
                        screen.blit(button_surf, button_rect)
                        # Button for restart
                        pygame.draw.line(screen, (245, 152, 66), (250, 705), (400, 705), 8)
                        pygame.draw.line(screen, (245, 152, 66), (250, 765), (400, 765), 8)
                        pygame.draw.line(screen, (245, 152, 66), (250, 705), (250, 765), 8)
                        pygame.draw.line(screen, (245, 152, 66), (400, 705), (400, 765), 8)
                        button_font = pygame.font.Font(None, 36)
                        button_surf = button_font.render('Restart', 0, (245, 152, 66))
                        button_rect = button_surf.get_rect(center=(325, 735))
                        screen.blit(button_surf, button_rect)
                        # Button for exit
                        pygame.draw.line(screen, (245, 152, 66), (450, 705), (600, 705), 8)
                        pygame.draw.line(screen, (245, 152, 66), (450, 765), (600, 765), 8)
                        pygame.draw.line(screen, (245, 152, 66), (450, 705), (450, 765), 8)
                        pygame.draw.line(screen, (245, 152, 66), (600, 705), (600, 765), 8)
                        button_font = pygame.font.Font(None, 36)
                        button_surf = button_font.render('Exit', 0, (245, 152, 66))
                        button_rect = button_surf.get_rect(center=(525, 735))
                        screen.blit(button_surf, button_rect)
                        for r in range(0, 9):
                            for c in range(0, 9):
                                Cell1 = Cell(save_for_reset[r][c], r, c, screen, None)
                                Cell1.draw(None)
                        SG1 = SudokuGenerator(9, removed_cells)
                        SG1.board = save_for_reset

                    # Condition for restart
                    elif 250 <= x <= 400:
                        removed_cells = draw_game_start(screen)
                        screen.fill((255, 255, 245))
                        Board1 = Board(675, 675, screen, 1)
                        SG1 = SudokuGenerator(9, removed_cells)
                        SG1.fill_values()
                        SG1.remove_cells()
                        save_for_reset = copy.deepcopy(SG1.board)
                        for r in range(0, 9):
                            for c in range(0, 9):
                                Cell1 = Cell(SG1.get_board()[r][c], r, c, screen, None)
                                Cell1.draw(None)
                        # Button for reset
                        pygame.draw.line(screen, (245, 152, 66), (50, 705), (200, 705), 8)
                        pygame.draw.line(screen, (245, 152, 66), (50, 765), (200, 765), 8)
                        pygame.draw.line(screen, (245, 152, 66), (50, 705), (50, 765), 8)
                        pygame.draw.line(screen, (245, 152, 66), (200, 705), (200, 765), 8)
                        button_font = pygame.font.Font(None, 36)
                        button_surf = button_font.render('Reset', 0, (245, 152, 66))
                        button_rect = button_surf.get_rect(center=(125, 735))
                        screen.blit(button_surf, button_rect)
                        # Button for restart
                        pygame.draw.line(screen, (245, 152, 66), (250, 705), (400, 705), 8)
                        pygame.draw.line(screen, (245, 152, 66), (250, 765), (400, 765), 8)
                        pygame.draw.line(screen, (245, 152, 66), (250, 705), (250, 765), 8)
                        pygame.draw.line(screen, (245, 152, 66), (400, 705), (400, 765), 8)
                        button_font = pygame.font.Font(None, 36)
                        button_surf = button_font.render('Restart', 0, (245, 152, 66))
                        button_rect = button_surf.get_rect(center=(325, 735))
                        screen.blit(button_surf, button_rect)
                        # Button for exit
                        pygame.draw.line(screen, (245, 152, 66), (450, 705), (600, 705), 8)
                        pygame.draw.line(screen, (245, 152, 66), (450, 765), (600, 765), 8)
                        pygame.draw.line(screen, (245, 152, 66), (450, 705), (450, 765), 8)
                        pygame.draw.line(screen, (245, 152, 66), (600, 705), (600, 765), 8)
                        button_font = pygame.font.Font(None, 36)
                        button_surf = button_font.render('Exit', 0, (245, 152, 66))
                        button_rect = button_surf.get_rect(center=(525, 735))
                        screen.blit(button_surf, button_rect)
                        player = 1
                        game_over = False
                        can_type = False
                        ready_for_ret = False
                        arrow_press = False
                        correct_index = False
                        winner = 0
                        Cell1 = None
                        Board1.draw()

                    # Condition for exit
                    elif 450 <= x <= 600:
                        pygame.quit()
                        sys.exit()

                if y < 705:
                    row = y // 75
                    col = x // 75
                    correct_index = True
                if correct_index == True:
                    if SG1.get_board()[row][col] == 0:
                        Cell1 = Cell(SG1.get_board()[row][col], row, col, screen, 2)
                        Cell1.select = True
                        Board1.draw()
                        Cell1.draw(2)
                        Cell1.sketch = True

            # When enter key is pressed
            if event.type == pygame.KEYDOWN:
                val = 0
                if event.key == pygame.K_RETURN:
                    if Cell1 and Cell1.sketch_value != 0:
                        val = Cell1.sketch_value
                        SG1.board[Cell1.row][Cell1.col] = val
                        Cell1.set_cell_value(val)
                        Cell1.state = 3  # Changes the state to 3
                        Cell1.sketch_value = 0
                        Cell1.sketch = False
                        Cell1.draw(3)  # Redraws the cell
                        pygame.display.update()
                # When 1-9 is pressed in cell
                if event.key == pygame.K_1:
                    val = 1
                elif event.key == pygame.K_2:
                    val = 2
                elif event.key == pygame.K_3:
                    val = 3
                elif event.key == pygame.K_4:
                    val = 4
                elif event.key == pygame.K_5:
                    val = 5
                elif event.key == pygame.K_6:
                    val = 6
                elif event.key == pygame.K_7:
                    val = 7
                elif event.key == pygame.K_8:
                    val = 8
                elif event.key == pygame.K_9:
                    val = 9
                # Handle backspace key: clear sketch value, update cell state, and redraw the cell
                elif event.key == pygame.K_BACKSPACE:
                    Cell1.sketched_value(0)
                    Cell1.draw(4)
                    val = Cell1.sketch_value
                    SG1.board[Cell1.row][Cell1.col] = val
                    Cell1.set_cell_value(val)
                    Cell1.state = 2
                    Cell1.sketch = True
                    Cell1.draw(2)
                    pygame.display.update()
                # Draws inside cell
                if val != 0:
                    Cell1.sketched_value(val)
                    Cell1.draw(2)
                # Deletes sketched value
                if event.key == pygame.K_DELETE:
                    Cell1.sketched_value(0)
                    Cell1.draw(4)
                # Up, down, right, left arrows
                if event.key == pygame.K_UP:
                    if row > 0:
                        if SG1.get_board()[row - 1][col] == 0:
                            row -= 1
                    arrow_press = True
                if event.key == pygame.K_DOWN:
                    if row < 8:
                        if SG1.get_board()[row + 1][col] == 0:
                            row += 1
                    arrow_press = True
                if event.key == pygame.K_RIGHT:
                    if col < 8:
                        if SG1.get_board()[row][col + 1] == 0:
                            col += 1
                    arrow_press = True
                if event.key == pygame.K_LEFT:
                    if col > 0:
                        if SG1.get_board()[row][col - 1] == 0:
                            col -= 1
                    arrow_press = True
                if arrow_press == True:
                    if SG1.get_board()[row][col] == 0:
                        Cell1 = Cell(SG1.get_board()[row][col], row, col, screen, 2)
                        Cell1.select = True
                        Board1.draw()
                        Cell1.draw(2)
                        Cell1.sketch = True
                        Cell1.sketched_value(val)
                # Check if puzzle complete, trigger game over if no empty cells left
                if SG1.find_empty() == None:
                    game_over = True
                    pygame.display.update()
                    pygame.time.delay(1000)
                    draw_game_over(screen, SG1, save_for_sol)

            pygame.display.update()
