import numpy as np
from particle import Particle

class Molecule:
    """A class which tracks the attributes of a simple diatomic molecule."""
    
    def __init__(self, pos1, pos2, m1, m2, k, L0):
        self.p1 = Particle(pos1, m1)
        self.p2 = Particle(pos2, m2)
        self.k = k
        self.L0 = L0

    def get_displ(self):
        return self.p2.pos - self.p1.pos

    def get_force(self):
        """Returns the spring force on p1 by p2."""
        return self.k*(1 - self.L0/np.linalg.norm(self.get_displ()))*self.get_displ()