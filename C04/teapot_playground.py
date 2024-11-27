from vectors import scale, add
from teapot import load_triangles
from draw_model import draw_model
from math import pi

def compose(*args):
    def new_function(input):
        state = input
        for f in reversed(args):
            state = f(state)
        return state
    return new_function

def scale_by(scalar):
    def new_function(v):
        return scale(scalar, v)
    return new_function

def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]

def translate_by(translation):
    def new_function(v):
        return add(translation,v)
    return new_function

def curry2(f):
    def g(x):
        def new_function(y):
            return f(x,y)
        return new_function
    return g

# scale_by = curry2(scale)
# print(scale_by(2)((1,2,3)))

# draw_model(polygon_map(compose(scale_by(2), translate_by((1,0,0))), load_triangles()))
# draw_model(polygon_map(compose(translate_by((1,0,0)),scale_by(2)), load_triangles()))
# draw_model(polygon_map(compose(translate_by((1,0,0)),scale_by(0.4),translate_by((0,.4,2)),scale_by(1.5)), load_triangles()))

# draw_model(polygon_map(translate_by((0,0,-20)), load_triangles()))
# draw_model(polygon_map(translate_by((-1,0,0)), load_triangles()))

# angle = pi /2
#
# v = (2,2,2)
#
# def stretch_x(scalar, vector):
#     x,y,z = vector
#     return (scalar*x, y, z)
#
# def stretch_x_by_scalar(scalar):
#     def new_function(vector):
#         return stretch_x(scalar, vector)
#     return new_function

# stretchx3 = curry2(stretch_x)
#
# print(stretchx3(3)(v))
# draw_model(polygon_map(compose(stretchx3(3)), load_triangles()))

Ae1 = (1, 1, 1)
Ae2 = (1, 0, -1)
Ae3 = (0, 1, 1)

def apply_A(v):
    return add(
        scale(v[0], Ae1),
        scale(v[1], Ae2),
        scale(v[2], Ae3)
    )

draw_model(polygon_map(apply_A, load_triangles()))