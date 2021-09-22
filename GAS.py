# There is a youtube video showing how this works on my channel right here
# https://www.youtube.com/watch?v=KMeT2k1ytYs&lc=z13ne1urvyvhzbqf523jzl0ovtupxbzlw


import pygame
import time
import random
import math
import numpy
from pygame import gfxdraw


class GAS_class:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        pygame.init()
        self.params = GAS_class
        self.params.game_width = 800
        self.params.game_height = 600
        self.params.white = (255, 255, 255)
        self.params.black = (0, 0, 0)
        self.params.red = (255, 0, 0)
        self.params.green = (0, 255, 0)
        self.params.blue = (0, 0, 255)
        self.params.fps = 60
        self.params.size = 5
        self.params.mutation_rate = 0.2
        self.params.steering_weights = 0.5
        self.params.perception_radius_mutation_range = 30
        self.params.reproduction_rate = 0.0005
        self.params.initial_perception_radius = 100
        self.params.boundary_size = 10
        self.params.max_vel = 10
        self.params.initial_max_force = 0.5
        self.params.health = 100
        self.params.max_poison = 50
        self.params.nutrition = [20, -80]
        self.params.bots = []
        self.params.food = []
        self.params.poison = []
        self.params.oldest_ever = 0
        self.params.oldest_ever_dna = []
        self.params.gameDisplay = pygame.display.set_mode((self.params.game_width, self.params.game_height))
        self.params.clock = pygame.time.Clock()

    def magnitude_calc(self, vector):
        x = 0
        for ii in vector:
            x += ii ** 2
        magnitude = x ** 0.5
        return (magnitude)

    def normalise(self, vector):
        magnitude = self.magnitude_calc(vector)
        if magnitude != 0:
            vector = vector / magnitude
        return (vector)


    # for i in range(10):
    #     self.params.bots.append(create_bot(random.uniform(0, game_width), random.uniform(0, game_height)))
    # running = True
    # while (running):
    #     gameDisplay.fill(black)
    #     if len(bots) < 5 or random.random() < 0.0001:
    #         bots.append(create_bot(random.uniform(0, game_width), random.uniform(0, game_height)))
    #     if random.random() < 0.1:
    #         food.append(numpy.array([random.uniform(boundary_size, game_width - boundary_size),
    #                                  random.uniform(boundary_size, game_height - boundary_size)], dtype='float64'))
    #     if random.random() < 0.01:
    #         poison.append(numpy.array([random.uniform(boundary_size, game_width - boundary_size),
    #                                    random.uniform(boundary_size, game_height - boundary_size)], dtype='float64'))
    #     if len(poison) > max_poison:
    #         poison.pop(0)

    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #     # print(event)

    #     # print(bots[0].position)
    #     # print((bots[0].position),(bots[0].position+(-size,0)),(bots[0].position+(-size/2,size)))
    #     for bot in bots[::-1]:
    #         bot.eat(food, 0)
    #         bot.eat(poison, 1)
    #         bot.boundaries()
    #         # bot.seek(pygame.mouse.get_pos())
    #         bot.update()
    #         if bot.age > oldest_ever:
    #             oldest_ever = bot.age
    #             oldest_ever_dna = bot.dna
    #             print(oldest_ever, oldest_ever_dna)
    #         bot.draw_bot()
    #         # pygame.draw.polygon(gameDisplay, bot.colour, ((bot.position),tuple(map(operator.add,bot.position,(-size,0))),tuple(map(operator.add,bot.position,(-size/2,size)))))
    #         if bot.dead():
    #             bots.remove(bot)
    #         else:
    #             bot.reproduce()

    #     # if random.random()<0.02:
    #     # bots.append(create_bot(random.uniform(0,game_width),random.uniform(0,game_height)))

    #     for i in food:
    #         pygame.draw.circle(gameDisplay, (0, 255, 0), (int(i[0]), int(i[1])), 3)
    #     # pygame.draw.circle(gameDisplay, bot.colour, (int(self.position[0]), int(self.position[1])), 10)
    #     for i in poison:
    #         pygame.draw.circle(gameDisplay, (255, 0, 0), (int(i[0]), int(i[1])), 3)
    #     pygame.display.update()
    #     clock.tick(fps)

    # pygame.quit()
    # #quit()


if __name__ == "__main__":
    g1 = GAS_class()
    
    for i in range(10):
        g1.params.bots.append(create_bot(random.uniform(0, g1.params.game_width), random.uniform(0, g1.params.game_height)))
    running = True
    while (running):
        g1.params.gameDisplay.fill(g1.params.black)
        if len(g1.params.bots) < 5 or random.random() < 0.0001:
            g1.params.bots.append(create_bot(random.uniform(0, g1.params.game_width), random.uniform(0, g1.params.game_height)))
        if random.random() < 0.1:
            g1.params.food.append(numpy.array([random.uniform(g1.params.boundary_size, g1.params.game_width - g1.params.boundary_size),
                                     random.uniform(g1.params.boundary_size, g1.params.game_height - g1.params.boundary_size)], dtype='float64'))
        if random.random() < 0.01:
            g1.params.poison.append(numpy.array([random.uniform(g1.params.boundary_size, g1.params.game_width - g1.params.boundary_size),
                                       random.uniform(g1.params.boundary_size, g1.params.game_height - g1.params.boundary_size)], dtype='float64'))
        if len(g1.params.poison) > g1.params.max_poison:
            g1.params.poison.pop(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # print(event)

        # print(bots[0].position)
        # print((bots[0].position),(bots[0].position+(-size,0)),(bots[0].position+(-size/2,size)))
        for bot in g1.params.bots[::-1]:
            bot.eat(g1.params.food, 0)
            bot.eat(g1.params.poison, 1)
            bot.boundaries()
            # bot.seek(pygame.mouse.get_pos())
            bot.update()
            if bot.age > oldest_ever:
                oldest_ever = bot.age
                oldest_ever_dna = bot.dna
                print(oldest_ever, oldest_ever_dna)
            bot.draw_bot()
            # pygame.draw.polygon(gameDisplay, bot.colour, ((bot.position),tuple(map(operator.add,bot.position,(-size,0))),tuple(map(operator.add,bot.position,(-size/2,size)))))
            if bot.dead():
                g1.params.bots.remove(bot)
            else:
                bot.reproduce()

        # if random.random()<0.02:
        # bots.append(create_bot(random.uniform(0,game_width),random.uniform(0,game_height)))

        for i in g1.params.food:
            pygame.draw.circle(g1.params.gameDisplay, (0, 255, 0), (int(i[0]), int(i[1])), 3)
        # pygame.draw.circle(gameDisplay, bot.colour, (int(self.position[0]), int(self.position[1])), 10)
        for i in g1.params.poison:
            pygame.draw.circle(g1.params.gameDisplay, (255, 0, 0), (int(i[0]), int(i[1])), 3)
        pygame.display.update()
        g1.params.clock.tick(g1.params.fps)

    pygame.quit()
    quit()
