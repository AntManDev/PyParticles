# Create a class for a particle with it's properties
class Particle:
    def __init__(self, position, velocity, mass=1.0):
        self.position = position # e.g. (x, y)
        self.velocity = velocity # e.g. (vx, vy)
        self.mass = mass
        self.forces = [0.0, 0.0]

    def apply_force(self, force):
        self.forces[0] += force[0]
        self.forces[1] += force[1]

    def update(self, dt):
        ax = self.forces[0] / self.mass
        ay = self.forces[1] / self.mass
        self.velocity = (self.velocity[0] + ax * dt, self.velocity[1] + ay * dt)
        self.position = (self.position[0] + self.velocity[0] * dt, self.position[1] + self.velocity[1] * dt)
        self.forces = [0.0, 0.0]

class ParticleSystem:
    def __init__(self, max_particles=1000, mode='CPU'):
        self.particles = []
        self.max_particles = max_particles
        self.mode = mode
        self.interactions = []

    def add_particle(self, particle):
        if len(self.particle) < self.max_particles:
            self.particles.append(particle)

    def add_interaction(self, interacrtion_func):
        self.interactions.append(interaction_func)

    def step(self, dt):
        if self.mode == 'CPU':
            self._cpu_step(dt)
        elif self.mode == 'GPU':
            pass 
    
    def _cpu_step(self, dt):
        for i, p1 in enumerate(self.particles):
            for j, p2 in enumerate(self.particles):
                if i != j:
                    for interaction in self.interactions:
                        interaction(p1, p2)

        for p in self.particles:
            p.update(dt)