

import pygame
import time
import random
import math
import numpy
from pygame import gfxdraw
from GAS import GAS_class

#g2 = GAS()
g1 = GAS_class()


class create_bot(GAS_class):  # How to input dna????
    def __init__(self, x, y, g1, dna=False):
        # super().__init__(GAS)

        # g1 = GAS
        self.max_vel = g1.params.max_vel
        self.mutation_rate = g1.params.mutation_rate
        self.green = g1.params.green
        self.game_width = g1.params.game_width
        self.boundary_size = g1.params.boundary_size
        self.game_height = g1.params.game_height
        self.bots = g1.params.bots

        self.steering_weights = g1.params.steering_weights
        self.perception_radius_mutation_range = g1.params.perception_radius_mutation_range
        self.initial_max_force = g1.params.initial_max_force
        self.initial_perception_radius = g1.params.initial_perception_radius

        self.reproduction_rate = g1.params.reproduction_rate
        self.normalise = g1.normalise()
        self.lerp = g1.lerp()
        self.health = g1.params.health


        self.position = numpy.array([x, y], dtype='float64')
        self.velocity = numpy.array([random.uniform(-self.max_vel, self.max_vel), random.uniform(-self.max_vel, self.max_vel)],
                                    dtype='float64')
        self.acceleration = numpy.array([0, 0], dtype='float64')
        self.colour = self.green

        self.max_vel = 2
        self.max_force = 0.5
        self.size = 5
        self.age = 1

        if dna:
            self.dna = []
            for i in range(len(dna)):
                if random.random() < self.mutation_rate:
                    if i < 2:
                        self.dna.append(dna[i] + random.uniform(-self.steering_weights, self.steering_weights))
                    else:
                        self.dna.append(dna[i] + random.uniform(-self.perception_radius_mutation_range,
                                                                self.perception_radius_mutation_range))

                else:
                    self.dna.append(dna[i])
        else:
            self.dna = [random.uniform(-self.initial_max_force, self.initial_max_force),
                        random.uniform(-self.initial_max_force, self.initial_max_force),
                        random.uniform(0, self.initial_perception_radius), random.uniform(0, self.initial_perception_radius)]
        print(self.dna)

    def update(self):
        self.velocity += self.acceleration

        self.velocity = self.normalise(self.velocity) * self.max_vel

        self.position += self.velocity
        self.acceleration *= 0
        self.health -= 0.2
        self.colour = self.lerp()
        self.health = min(g1.params.health, self.health)
        if self.age % 1000 == 0:
            print(self.age, self.dna)
        self.age += 1

    def reproduce(self):
        if random.random() < self.reproduction_rate:
            self.bots.append(create_bot(self.position[0], self.position[1], self.dna))

    def dead(self):
        if self.health > 0:
            return False
        else:
            if self.position[0] < self.game_width - self.boundary_size and self.position[0] > self.boundary_size and self.position[1] < self.game_height - self.boundary_size and self.position[1] > self.boundary_size:
                self.food.append(self.position)
            return True

    def apply_force(self, force):
        self.acceleration += force

    def seek(self, target):
        desired_vel = numpy.add(target, -self.position)
        desired_vel = self.normalise(desired_vel) * self.max_vel
        steering_force = numpy.add(desired_vel, -self.velocity)
        steering_force = self.normalise(steering_force) * self.max_force
        return steering_force

    # self.apply_force(steering_force)

    def eat(self, list_of_stuff, index):
        closest = None
        closest_distance = max(self.game_width, self.game_height)
        bot_x = self.position[0]
        bot_y = self.position[1]
        item_number = len(list_of_stuff) - 1
        for i in list_of_stuff[::-1]:
            item_x = i[0]
            item_y = i[1]
            distance = math.hypot(bot_x - item_x, bot_y - item_y)
            if distance < 5:
                list_of_stuff.pop(item_number)
                self.health += self.nutrition[index]
            if distance < closest_distance:
                closest_distance = distance
                closest = i
            item_number -= 1
        if closest_distance < self.dna[2 + index]:
            seek = self.seek(closest)  # index)
            seek *= self.dna[index]
            seek = self.normalise(seek) * self.max_force
            self.apply_force(seek)

    def boundaries(self):
        desired = None
        x_pos = self.position[0]
        y_pos = self.position[1]
        if x_pos < self.boundary_size:
            desired = numpy.array([self.max_vel, self.velocity[1]])
        elif x_pos > self.game_width - self.boundary_size:
            desired = numpy.array([-self.max_vel, self.velocity[1]])
        if y_pos < self.boundary_size:
            desired = numpy.array([self.velocity[0], self.max_vel])
        elif y_pos > self.game_height - self.boundary_size:
            desired = numpy.array([self.velocity[0], -self.max_vel])
        if desired is not None:
            steer = desired - self.velocity
            steer = self.normalise(steer) * self.max_force
            self.apply_force(steer)

    def draw_bot(self):
        pygame.gfxdraw.aacircle(self.gameDisplay, int(self.position[0]), int(self.position[1]), 10, self.colour)
        pygame.gfxdraw.filled_circle(self.gameDisplay, int(self.position[0]), int(self.position[1]), 10, self.colour)
        pygame.draw.circle(self.gameDisplay, self.green, (int(self.position[0]), int(self.position[1])),
                           abs(int(self.dna[2])), abs(int(min(2, self.dna[2]))))
        pygame.draw.circle(self.gameDisplay, self.red, (int(self.position[0]), int(self.position[1])), abs(int(self.dna[3])),
                           abs(int(min(2, self.dna[3]))))
        pygame.draw.line(self.gameDisplay, self.green, (int(self.position[0]), int(self.position[1])), (
        int(self.position[0] + (self.velocity[0] * self.dna[0] * 25)),
        int(self.position[1] + (self.velocity[1] * self.dna[0] * 25))), 3)
        pygame.draw.line(self.gameDisplay, self.red, (int(self.position[0]), int(self.position[1])), (
        int(self.position[0] + (self.velocity[0] * self.dna[1] * 25)),
        int(self.position[1] + (self.velocity[1] * self.dna[1] * 25))), 2)

    # for i in range(10):
    #     bots.append(create_bot(random.uniform(0, game_width), random.uniform(0, game_height)))
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
    # quit()

if __name__ == "__main__":
    create_bot(random.uniform(0,800),random.uniform(0,600),g1)