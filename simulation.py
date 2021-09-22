# There is a youtube video showing how this works on my channel right here
# https://www.youtube.com/watch?v=KMeT2k1ytYs&lc=z13ne1urvyvhzbqf523jzl0ovtupxbzlw


import pygame
import time
import random
import math
import numpy
from pygame import gfxdraw

class GAS:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.params = None
        pygame.init()
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
        self.params.gameDisplay = pygame.display.set_mode((self.game_width, self.game_height))
        self.params.clock = pygame.time.Clock()

<<<<<<< HEAD

    def lerp():
        percent_health = bot.health / health
        lerped_colour = (max(min((1 - percent_health) * 255, 255), 0), max(min(percent_health * 255, 255), 0), 0)
        return (lerped_colour)

    def magnitude_calc(vector):
        x = 0
        for i in vector:
            x += i ** 2
        magnitude = x ** 0.5
        return magnitude

    def normalise(vector):
        magnitude = self.magnitude_calc(vector)
        if magnitude != 0:
            vector = vector / magnitude
        return vector

    class create_bot:  # How to input dna????
        def __init__(self, x, y, dna=False):
            super().__init__(x, y, dna=False)
            self.position = numpy.array([x, y], dtype='float64')
            self.velocity = numpy.array([random.uniform(-self.max_vel, self.max_vel), random.uniform(-self.max_vel, self.max_vel)],
                                        dtype='float64')
            self.acceleration = numpy.array([0, 0], dtype='float64')
            self.colour = self.params.green
            self.health = self.health
            self.max_vel = 2
            self.max_force = 0.5
            self.size = 5
            self.age = 1

            if dna:
                self.dna = []
                for i in range(len(dna)):
                    if random.random() < self.params.mutation_rate:
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
            self.health = min(self.health, self.health)
            if self.age % 1000 == 0:
                print(self.age, self.dna)
            self.age += 1

        def reproduce(self):
            if random.random() < self.reproduction_rate:
                self.bots.append(self.create_bot(self.position[0], self.position[1], self.dna))

        def dead(self):
            if self.health > 0:
                return (False)
            else:
                if self.params.position[0] < self.params.game_width - self.params.boundary_size and self.params.position[0] > self.params.boundary_size and self.params.position[
                    1] < self.params.game_height - self.params.boundary_size and self.params.position[1] > self.params.boundary_size:
                    self.food.append(self.position)
                return (True)

        def apply_force(self, force):
            self.acceleration += force

        def seek(self, target):
            desired_vel = numpy.add(target, -self.position)
            desired_vel = self.params.normalise(desired_vel) * self.max_vel
            steering_force = numpy.add(desired_vel, -self.velocity)
            steering_force = self.params.normalise(steering_force) * self.max_force
            return (steering_force)

        # self.apply_force(steering_force)

        def eat(self, list_of_stuff, index):
            closest = None
            closest_distance = max(self.params.game_width, self.params.game_height)
            bot_x = self.position[0]
            bot_y = self.position[1]
            item_number = len(list_of_stuff) - 1
            for i in list_of_stuff[::-1]:
                item_x = i[0]
                item_y = i[1]
                distance = math.hypot(bot_x - item_x, bot_y - item_y)
                if distance < 5:
                    list_of_stuff.pop(item_number)
                    self.health += nutrition[index]
                if distance < closest_distance:
                    closest_distance = distance
                    closest = i
                item_number -= 1
            if closest_distance < self.dna[2 + index]:
                seek = self.seek(closest)  # index)
                seek *= self.dna[index]
                seek = self.params.normalise(seek) * self.max_force
                self.apply_force(seek)

        def boundaries(self):
            desired = None
            x_pos = self.position[0]
            y_pos = self.position[1]
            if x_pos < self.params.boundary_size:
                desired = numpy.array([self.max_vel, self.velocity[1]])
            elif x_pos > self.params.game_width - self.params.boundary_size:
                desired = numpy.array([-self.max_vel, self.velocity[1]])
            if y_pos < self.params.boundary_size:
                desired = numpy.array([self.velocity[0], self.max_vel])
            elif y_pos > self.params.game_height - self.params.boundary_size:
                desired = numpy.array([self.velocity[0], -self.max_vel])
            if desired is not None:
                steer = desired - self.velocity
                steer = self.params.normalise(steer) * self.max_force
                self.apply_force(steer)

        def draw_bot(self):
            pygame.gfxdraw.aacircle(self.params.gameDisplay, int(self.position[0]), int(self.position[1]), 10, self.colour)
            pygame.gfxdraw.filled_circle(self.params.gameDisplay, int(self.position[0]), int(self.position[1]), 10, self.colour)
            pygame.draw.circle(self.params.gameDisplay, self.params.green, (int(self.position[0]), int(self.position[1])),
                               abs(int(self.dna[2])), abs(int(min(2, self.dna[2]))))
            pygame.draw.circle(self.params.gameDisplay, self.params.red, (int(self.position[0]), int(self.position[1])), abs(int(self.dna[3])),
                               abs(int(min(2, self.dna[3]))))
            pygame.draw.line(self.params.gameDisplay, self.params.green, (int(self.position[0]), int(self.position[1])), (
            int(self.position[0] + (self.velocity[0] * self.dna[0] * 25)),
            int(self.position[1] + (self.velocity[1] * self.dna[0] * 25))), 3)
            pygame.draw.line(self.params.gameDisplay, self.params.red, (int(self.position[0]), int(self.position[1])), (
            int(self.position[0] + (self.velocity[0] * self.dna[1] * 25)),
            int(self.position[1] + (self.velocity[1] * self.dna[1] * 25))), 2)

    for i in range(10):
        self.params.bots.append(create_bot(random.uniform(0, self.params.game_width), random.uniform(0, self.params.game_height)))
    running = True
    while (running):
        self.params.gameDisplay.fill(self.params.black)
        if len(self.params.bots) < 5 or random.random() < 0.0001:
            self.params.bots.append(create_bot(random.uniform(0, self.params.game_width), random.uniform(0, self.params.game_height)))
        if random.random() < 0.1:
            self.params.food.append(numpy.array([random.uniform(self.params.boundary_size, self.params.game_width - self.params.boundary_size),
                                     random.uniform(self.params.boundary_size, self.params.game_height - self.params.boundary_size)], dtype='float64'))
        if random.random() < 0.01:
            poison.append(numpy.array([random.uniform(boundary_size, game_width - boundary_size),
                                       random.uniform(boundary_size, game_height - boundary_size)], dtype='float64'))
        if len(poison) > max_poison:
            poison.pop(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # print(event)

        # print(bots[0].position)
        # print((bots[0].position),(bots[0].position+(-size,0)),(bots[0].position+(-size/2,size)))
        for bot in bots[::-1]:
            bot.eat(food, 0)
            bot.eat(poison, 1)
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
                bots.remove(bot)
            else:
                bot.reproduce()

        # if random.random()<0.02:
        # bots.append(create_bot(random.uniform(0,game_width),random.uniform(0,game_height)))

        for i in food:
            pygame.draw.circle(gameDisplay, (0, 255, 0), (int(i[0]), int(i[1])), 3)
        # pygame.draw.circle(gameDisplay, bot.colour, (int(self.position[0]), int(self.position[1])), 10)
        for i in poison:
            pygame.draw.circle(gameDisplay, (255, 0, 0), (int(i[0]), int(i[1])), 3)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

if __name__ == "__main__":
    GAS()