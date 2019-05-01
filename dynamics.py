# Physics 91SI
# Spring 2019
# Lab 9

# Modules you won't need
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Modules you will need
import numpy as np
import particle
from molecule import Molecule

# TODO: Implement this function
def init_molecule():
    x1 = 0.2
    y1 = 0.2
    m1 = 1
    x2 = 0.8
    y2 = 0.8
    m2 = 2
    k = 1
    L0 = 0.5
    pos1 = np.array([x1,y1])
    pos2 = np.array([x2,y2])
    return Molecule(pos1,pos2,m1,m2,k,L0)


# TODO: Implement this function
def time_step(dt, mol):
    """Sets new positions and velocities of the particles attached to mol"""
    mol.p1.vel += mol.get_force() * dt / mol.p1.m
    mol.p2.vel += -1 * mol.get_force() * dt / mol.p2.m
    mol.p1.pos += mol.p1.vel * dt
    mol.p2.pos += mol.p2.vel * dt


#############################################
# The rest of the file is already implemented
#############################################

def run_dynamics(n, dt, xlim=(0, 1), ylim=(0, 1)):
    """Calculate each successive time step and animate it"""
    mol = init_molecule()

    # Animation stuff
    fig, ax = plt.subplots()
    line, = ax.plot((mol.p1.pos[0], mol.p2.pos[0]), (mol.p1.pos[1], mol.p2.pos[1]), '-o')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title('Dynamics simulation')
    dynamic_ani = animation.FuncAnimation(fig, update_anim, n,
            fargs=(dt, mol,line), interval=50, blit=False)
    plt.show()

def update_anim(i,dt, mol,line):
    """Update and draw the molecule. Called by FuncAnimation"""
    time_step(dt, mol)
    line.set_data([(mol.p1.pos[0], mol.p2.pos[0]),
                   (mol.p1.pos[1], mol.p2.pos[1])])
    return line,

if __name__ == '__main__':
    # Set the number of iterations and time step size
    n = 10
    dt = .1
    run_dynamics(n, dt)
