# There is a youtube video showing how this works on my channel right here
# https://www.youtube.com/watch?v=KMeT2k1ytYs&lc=z13ne1urvyvhzbqf523jzl0ovtupxbzlw


import pygame


class GAS_class:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.params = GAS_class
        self.params.min_bots = 2
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
        return vector
