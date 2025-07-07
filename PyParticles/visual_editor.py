# The Visual editor for PyParticles
import tkinter as tk
from particle_sys_core import Particle, ParticleSystem
import random

def attraction_force(p1, p2, strength=1000):
    dx = p2.position[0] - p1.position[0]
    dy = p2.position[1] - p1.position[1]
    dist_sq = dx * dx + dy * dy

    if dist_sq == 0:
        return  # Avoid division by zero

    force_magnitude = strength / dist_sq
    dist = dist_sq ** 0.5
    fx = force_magnitude * dx / dist
    fy = force_magnitude * dy / dist

    p1.apply_force((fx, fy))

class ParticleEditor:
    def __init__(self, master, particle_system):
        self.master = master
        self.particle_system = particle_system
        self.canvas = tk.Canvas(master, width=800, height=600, bg="black")
        self.canvas.pack()

        self.particle_radius = 3
        self.preview_particles = []
        self.edit_mode = True

        self.setup_ui()

    def setup_ui(self):
        btn_preview = tk.Button(self.master, text="Preview", command=self.preview)
        btn_preview.pack(side=tk.LEFT)

        btn_add_particle = tk.Button(self.master, text="Add Particle", command=self.add_particle)
        btn_add_particle.pack(side=tk.LEFT)

        btn_clear = tk.Button(self.master, text="Clear", command=self.clear_particles)
        btn_clear.pack(side=tk.LEFT)

    def add_particle(self):
        p = Particle((400, 300), (0, 0))
        self.particle_system.add_particle(p)
        self.preview_particles.append(p)
        self.draw_particles()

    def clear_particles(self):
        self.particle_system.particles.clear()
        self.preview_particles.clear()
        self.canvas.delete("all")

    def preview(self):
        self.edit_mode = False
        self.animate()

    def animate(self):
        if self.edit_mode:
            return
        dt = 0.1
        self.particle_system.step(dt)
        self.draw_particles()
        self.master.after(33, self.animate)

    def draw_particles(self):
        self.canvas.delete("all")
        for p in self.particle_system.particles:
            x, y = p.position
            self.canvas.create_oval(
                x - self.particle_radius,
                y - self.particle_radius,
                x + self.particle_radius,
                y + self.particle_radius,
                fill="white"   
            )

if __name__ == "__main__":
    root = tk.Tk()
    ps = ParticleSystem()
    ps.add_interaction(attraction_force)
    editor = ParticleEditor(root, ps)
    root.mainloop()
