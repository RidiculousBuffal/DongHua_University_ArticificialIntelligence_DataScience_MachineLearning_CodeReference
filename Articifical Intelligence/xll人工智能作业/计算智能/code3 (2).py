import random


class Particle:
    def __init__(self, bounds):
        self.position = random.uniform(bounds[0], bounds[1])  #随机生成点的坐标
        self.velocity = random.uniform(-1, 1)  # 速度
        self.best_position = self.position  # 最佳位置
        self.best_value = self.eval_position()  # 最佳值

    def eval_position(self):
        return self.position ** 2  # f(x) = x^2

    def update_velocity(self, global_best_position):
        c1 = 1
        c2 = 2
        r1 = random.random()
        r2 = random.random()
        self.velocity = (self.velocity +
                         c1 * r1 * (self.best_position - self.position) +
                         c2 * r2 * (global_best_position - self.position))

    def update_position(self, bounds):
        self.position += self.velocity
        if self.position < bounds[0]:
            self.position = bounds[0]
        if self.position > bounds[1]:
            self.position = bounds[1]

    def update(self, global_best_position, bounds):
        self.update_velocity(global_best_position)
        self.update_position(bounds)
        current_value = self.eval_position()
        if current_value > self.best_value:
            self.best_value = current_value
            self.best_position = self.position


def pso(num_particles, bounds, max_iter):
    particles = [Particle(bounds) for _ in range(num_particles)]
    global_best_value = float('-inf')
    global_best_position = None

    for _ in range(max_iter):
        for particle in particles:
            if particle.best_value > global_best_value:
                global_best_value = particle.best_value
                global_best_position = particle.best_position

        for particle in particles:
            particle.update(global_best_position, bounds)

    return global_best_position, global_best_value


# PSO 参数
num_particles = 30
bounds = (0, 31)  # Bounds for x
max_iter = 100

#  PSO
best_position, best_value = pso(num_particles, bounds, max_iter)
print(best_position, best_value)

