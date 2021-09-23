import sys
import threading
from time import sleep

import pygame
import time
import random
import math
import numpy
from PyQt5 import QtWidgets
from pygame import gfxdraw
from GAS import GAS_class
from Mattias import GUI_setup


class create_bot:

    def __init__(self, g1, x, y, dna=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.g1 = g1

        self.position = numpy.array([x, y], dtype='float64')
        self.velocity = numpy.array([random.uniform(-g1.params.max_vel, g1.params.max_vel),
                                     random.uniform(-g1.params.max_vel, g1.params.max_vel)],
                                    dtype='float64')
        self.acceleration = numpy.array([0, 0], dtype='float64')
        self.health = g1.params.health

        dna = False
        self.max_vel = 2
        self.max_force = 0.5
        self.size = 5
        self.age = 1

        if dna:
            print("AAAAAAAAAAA")
            self.dna = []
            for i in range(len(dna)):
                if random.random() < g1.params.mutation_rate:
                    if i < 2:
                        self.dna.append(
                            dna[i] + random.uniform(-g1.params.steering_weights, g1.params.steering_weights))
                    else:
                        self.dna.append(dna[i] + random.uniform(-g1.params.perception_radius_mutation_range,
                                                                g1.params.perception_radius_mutation_range))

                else:
                    self.dna.append(dna[i])
        else:
            self.dna = [random.uniform(-g1.params.initial_max_force, g1.params.initial_max_force),
                        random.uniform(-g1.params.initial_max_force, g1.params.initial_max_force),
                        random.uniform(0, g1.params.initial_perception_radius),
                        random.uniform(0, g1.params.initial_perception_radius)]
        # print(self.dna)

    def lerp(self):
        percent_health = self.health / self.g1.params.health
        lerped_colour = (max(min((1 - percent_health) * 255, 255), 0), max(min(percent_health * 255, 255), 0), 0)
        return (lerped_colour)

    def update(self):
        self.velocity += self.acceleration

        self.velocity = self.g1.params.normalise(self.g1, self.velocity) * self.max_vel

        self.position += self.velocity
        self.acceleration *= 0
        self.health -= 0.2
        self.colour = self.lerp()
        self.health = min(self.g1.params.health, self.health)
        self.age += 1

    def reproduce(self):
        if random.random() < self.g1.params.reproduction_rate:
            self.g1.params.bots.append(create_bot(self.g1, self.position[0], self.position[1], self.dna))

    def dead(self):
        if self.health > 0:
            return False
        else:
            if self.g1.params.game_width - self.g1.params.boundary_size > self.position[
                0] > self.g1.params.boundary_size and self.g1.params.game_height - self.g1.params.boundary_size > \
                    self.position[1] > self.g1.params.boundary_size:
                self.g1.params.food.append(self.position)
            return True

    def apply_force(self, force):
        self.acceleration += force

    def seek(self, target):
        desired_vel = numpy.add(target, -self.position)
        desired_vel = self.g1.params.normalise(self.g1, desired_vel) * self.max_vel
        steering_force = numpy.add(desired_vel, -self.velocity)
        steering_force = self.g1.params.normalise(self.g1, steering_force) * self.max_force
        return steering_force

    # self.apply_force(steering_force)

    def eat(self, list_of_stuff, index):
        closest = None
        closest_distance = max(self.g1.params.game_width, self.g1.params.game_height)
        bot_x = self.position[0]
        bot_y = self.position[1]
        item_number = len(list_of_stuff) - 1
        for i in list_of_stuff[::-1]:
            item_x = i[0]
            item_y = i[1]
            distance = math.hypot(bot_x - item_x, bot_y - item_y)
            if distance < 5:
                list_of_stuff.pop(item_number)
                self.health += self.g1.params.nutrition[index]
            if distance < closest_distance:
                closest_distance = distance
                closest = i
            item_number -= 1
        if closest_distance < self.dna[2 + index]:
            seek = self.seek(closest)  # index)
            seek *= self.dna[index]
            seek = self.g1.params.normalise(self.g1, seek) * self.max_force
            self.apply_force(seek)

    def boundaries(self):
        desired = None
        x_pos = self.position[0]
        y_pos = self.position[1]
        if x_pos < self.g1.params.boundary_size:
            desired = numpy.array([self.max_vel, self.velocity[1]])
        elif x_pos > self.g1.params.game_width - self.g1.params.boundary_size:
            desired = numpy.array([-self.max_vel, self.velocity[1]])
        if y_pos < self.g1.params.boundary_size:
            desired = numpy.array([self.velocity[0], self.max_vel])
        elif y_pos > self.g1.params.game_height - self.g1.params.boundary_size:
            desired = numpy.array([self.velocity[0], -self.max_vel])
        if desired is not None:
            steer = desired - self.velocity
            steer = self.g1.params.normalise(self.g1, steer) * self.max_force
            self.apply_force(steer)

    def draw_bot(self):
        pygame.gfxdraw.aacircle(self.g1.params.gameDisplay, int(self.position[0]), int(self.position[1]), 10,
                                self.colour)
        pygame.gfxdraw.filled_circle(self.g1.params.gameDisplay, int(self.position[0]), int(self.position[1]), 10,
                                     self.colour)
        pygame.draw.circle(self.g1.params.gameDisplay, self.g1.params.green,
                           (int(self.position[0]), int(self.position[1])),
                           abs(int(self.dna[2])), abs(int(min(2, self.dna[2]))))
        pygame.draw.circle(self.g1.params.gameDisplay, self.g1.params.red,
                           (int(self.position[0]), int(self.position[1])), abs(int(self.dna[3])),
                           abs(int(min(2, self.dna[3]))))
        pygame.draw.line(self.g1.params.gameDisplay, self.g1.params.green,
                         (int(self.position[0]), int(self.position[1])), (
                             int(self.position[0] + (self.velocity[0] * self.dna[0] * 25)),
                             int(self.position[1] + (self.velocity[1] * self.dna[0] * 25))), 3)
        pygame.draw.line(self.g1.params.gameDisplay, self.g1.params.red, (int(self.position[0]), int(self.position[1])),
                         (
                             int(self.position[0] + (self.velocity[0] * self.dna[1] * 25)),
                             int(self.position[1] + (self.velocity[1] * self.dna[1] * 25))), 2)


class sim(threading.Thread):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        g1 = GAS_class()
        self.g1 = g1
        app = QtWidgets.QApplication(sys.argv)
        w = GUI_setup(g1)
        w.showUI()
        self.w = w
        self.simulation()
        sys.exit(app.exec_())

    def simulation(self):
        pygame.init()
        create_bot(self.g1, random.uniform(0, 800), random.uniform(0, 600), self.g1)

        for i in range(10):
            self.g1.params.bots.append(
                create_bot(self.g1, random.uniform(0, self.g1.params.game_width),
                           random.uniform(0, self.g1.params.game_height)))

        running = True
        oldest_ever_arr = []
        time_arr = []

        while (running):
            print(self.g1.params.oldest_ever)
            self.g1.params.gameDisplay.fill(self.g1.params.black)
            if len(self.g1.params.bots) < self.g1.params.min_bots or random.random() < 0.0001:
                self.g1.params.bots.append(
                    create_bot(self.g1, random.uniform(0, self.g1.params.game_width),
                               random.uniform(0, self.g1.params.game_height)))
            if random.random() < 0.1:
                self.g1.params.food.append(numpy.array(
                    [random.uniform(self.g1.params.boundary_size,
                                    self.g1.params.game_width - self.g1.params.boundary_size),
                     random.uniform(self.g1.params.boundary_size,
                                    self.g1.params.game_height - self.g1.params.boundary_size)],
                    dtype='float64'))
            if random.random() < 0.01:
                self.g1.params.poison.append(numpy.array(
                    [random.uniform(self.g1.params.boundary_size,
                                    self.g1.params.game_width - self.g1.params.boundary_size),
                     random.uniform(self.g1.params.boundary_size,
                                    self.g1.params.game_height - self.g1.params.boundary_size)],
                    dtype='float64'))
            if len(self.g1.params.poison) > self.g1.params.max_poison:
                self.g1.params.poison.pop(0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # print(event)

            # print(bots[0].position)
            # print((bots[0].position),(bots[0].position+(-size,0)),(bots[0].position+(-size/2,size)))
            for bot in self.g1.params.bots[::-1]:
                bot.eat(self.g1.params.food, 0)
                bot.eat(self.g1.params.poison, 1)
                bot.boundaries()
                # bot.seek(pygame.mouse.get_pos())
                bot.update()
                if bot.age > self.g1.params.oldest_ever:
                    self.g1.params.oldest_ever = bot.age / 10
                    if len(oldest_ever_arr) < 100:
                        oldest_ever_arr.append(self.g1.params.oldest_ever)
                    else:

                    self.g1.params.oldest_ever_dna = bot.dna
                    # print(oldest_ever, oldest_ever_dna)
                bot.draw_bot()
                # pygame.draw.polygon(gameDisplay, bot.colour, ((bot.position),tuple(map(operator.add,bot.position,(-size,0))),tuple(map(operator.add,bot.position,(-size/2,size)))))
                if bot.dead():
                    self.g1.params.bots.remove(bot)
                else:
                    bot.reproduce()

            # if random.random()<0.02:
            # bots.append(create_bot(random.uniform(0,game_width),random.uniform(0,game_height)))

            for i in self.g1.params.food:
                pygame.draw.circle(self.g1.params.gameDisplay, (0, 255, 0), (int(i[0]), int(i[1])), 3)
            # pygame.draw.circle(gameDisplay, bot.colour, (int(self.position[0]), int(self.position[1])), 10)
            for i in self.g1.params.poison:
                pygame.draw.circle(self.g1.params.gameDisplay, (255, 0, 0), (int(i[0]), int(i[1])), 3)
            pygame.display.update()
            self.g1.params.clock.tick(self.g1.params.fps)

        pygame.quit()
        quit()


if __name__ == "__main__":
    sim()
