import pygame
import time
import random
import csv
import os

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
dis_width = 800
dis_height = 600

# Create display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by GitHub Copilot')

# Set clock
clock = pygame.time.Clock()

# Set snake block size and speed
snake_block = 10
snake_speed = 15

# Define font styles
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# CSV file for storing scores
score_file = 'C:/Users/arnow/OneDrive/Documenten/MCT/3MCT/AI/Snake Game/snakescores.csv'

def save_score(score):
    with open(score_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([score])

def pause_message():
    message("Game Paused. Press Space to Resume", yellow)
    pygame.display.update()

def get_top_scores():
    if not os.path.exists(score_file):
        return []
    with open(score_file, mode='r') as file:
        reader = csv.reader(file)
        scores = sorted([int(row[0]) for row in reader], reverse=True)
        return scores[:3]

def our_snake(snake_block, snake_List, direction):
    for index, x in enumerate(snake_List):
        if index == len(snake_List) - 1:
            # Draw the half-circle part of the head based on direction
            if direction == 'UP':
                pygame.draw.circle(dis, blue, (x[0] + snake_block // 2, x[1]), snake_block // 2)
                pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block // 2])
            elif direction == 'DOWN':
                pygame.draw.circle(dis, blue, (x[0] + snake_block // 2, x[1] + snake_block), snake_block // 2)
                pygame.draw.rect(dis, blue, [x[0], x[1] + snake_block // 2, snake_block, snake_block // 2])
            elif direction == 'LEFT':
                pygame.draw.circle(dis, blue, (x[0], x[1] + snake_block // 2), snake_block // 2)
                pygame.draw.rect(dis, blue, [x[0], x[1], snake_block // 2, snake_block])
            elif direction == 'RIGHT':
                pygame.draw.circle(dis, blue, (x[0] + snake_block, x[1] + snake_block // 2), snake_block // 2)
                pygame.draw.rect(dis, blue, [x[0] + snake_block // 2, x[1], snake_block // 2, snake_block])
        else:
            pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])


def message(msg, color, score=None):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(dis_width / 2, dis_height / 3))
    dis.blit(mesg, mesg_rect)
    if score is not None:
        score_msg = score_font.render("Your Score: " + str(score), True, yellow)
        score_rect = score_msg.get_rect(center=(dis_width / 2, dis_height / 3 + 50))
        dis.blit(score_msg, score_rect)
        
        top_scores = get_top_scores()
        for i, top_score in enumerate(top_scores):
            top_score_msg = score_font.render(f"Top {i+1} Score: {top_score}", True, yellow)
            top_score_rect = top_score_msg.get_rect(center=(dis_width / 2, dis_height / 3 + 100 + i * 30))
            dis.blit(top_score_msg, top_score_rect)

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def generate_food(food_count):
    while True:
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        # Ensure food does not spawn in the top area where the score and messages are displayed
        if foody > dis_height / 3 + 150:
            food_type = green if (food_count % 4) != 3 else red
            print(f"Generated food at ({foodx}, {foody}) with type {'red' if food_type == red else 'green'}")
            return foodx, foody, food_type
        
def display_start_message():
    dis.fill(black)
    font_style = pygame.font.SysFont(None, 50)
    message = font_style.render("Press any arrow key to start the game", True, white)
    dis.blit(message, [dis_width / 6, dis_height / 3])
    pygame.display.update()

def gameLoop():
    game_over = False
    game_close = False
    paused = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx, foody, food_type = generate_food(0)
    food_count = 0

    direction = 'RIGHT'  # Initial direction

    # Display start message and wait for arrow key press
    display_start_message()
    waiting_for_start = True
    while waiting_for_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    waiting_for_start = False

    while not game_over:

        while game_close:
            dis.fill(black)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            dis.blit(message, [dis_width / 6, dis_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                    direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                    direction = 'DOWN'

        if not paused:
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(black)
            pygame.draw.circle(dis, food_type, (int(foodx + snake_block / 2), int(foody + snake_block / 2)), snake_block // 2)
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List, direction)
            your_score(Length_of_snake - 1)
            pygame.display.update()
            if x1 == foodx and y1 == foody:
                current_food_type = food_type  # Store the current food type
                food_count += 1
                foodx, foody, food_type = generate_food(food_count)
                if current_food_type == red:
                    Length_of_snake += 2
                else:
                    Length_of_snake += 1

            clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()