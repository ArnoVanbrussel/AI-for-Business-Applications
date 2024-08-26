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