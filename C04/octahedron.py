import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from matplotlib import colormaps
from vectors import *
from math import *
import itertools

def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

blues = colormaps.get_cmap('Greens')

def shade(face, color_map=blues, light=(1,2,3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))

light = (1,2,3)
faces = [
    [vec_x, vec_y, vec_z]
    # Combinations of ±1 and zeros for the first vector (x-axis)
    for vec_x in [(x, 0, 0) for x in [-1, 1]]
    # Perpendicular unit y and z vectors
    for vec_y, vec_z in itertools.permutations([(0, y, z) for y, z in itertools.product([-1, 0, 1], repeat=2)
                        if abs(y) + abs(z) == 1], 2)
    # Right-hand rule: cross product of y and z in x direction
    if (
        vec_y[1] * vec_z[2] - vec_y[2] * vec_z[1],
        vec_y[2] * vec_z[0] - vec_y[0] * vec_z[2],
        vec_y[0] * vec_z[1] - vec_y[1] * vec_z[0]
    ) == vec_x
]

pygame.init()
display = (400,400)
window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, 1, 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)
glEnable(GL_CULL_FACE)
glEnable(GL_DEPTH_TEST)
glCullFace(GL_BACK)

degrees_per_second = 360./5
degrees_per_millisecond = degrees_per_second / 1000

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    milliseconds = clock.tick()
    glRotate(milliseconds * degrees_per_millisecond, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    for face in faces:
        color = shade(face, blues, light)

        for vertex in face:
            glColor3fv((color[0],
                        color[1],
                        color[2]))
            glVertex3fv(vertex)
    glEnd()
    pygame.display.flip()
