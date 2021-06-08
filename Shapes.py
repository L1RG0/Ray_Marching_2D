import OpenGL.GL as GL
import math

BackgroundColor = (0, 0, 0)
BrushColor = (1, 1, 1)

def Circle(position, accuracy, inside):
    posx, posy = position[0], position[1]
    radius = position[2]
    if inside:
        GL.glBegin(GL.GL_POLYGON)
        for i in range(accuracy):
            cosine = radius * math.cos(i * 2 * math.pi / accuracy) + posx
            sine   = radius * math.sin(i * 2 * math.pi / accuracy) + posy
            GL.glVertex2f(cosine, sine)
        GL.glEnd()
    else:
        for i in range(accuracy):
            GL.glBegin(GL.GL_LINES)
            cosine = radius * math.cos(i * 2 * math.pi / accuracy) + posx
            sine = radius * math.sin(i * 2 * math.pi / accuracy) + posy
            GL.glVertex2f(cosine, sine)
            cosine = radius * math.cos((i + 1) * 2 * math.pi / accuracy) + posx
            sine = radius * math.sin((i + 1) * 2 * math.pi / accuracy) + posy
            GL.glVertex2f(cosine, sine)
            GL.glEnd()

def Line(position1, position2):
    GL.glBegin(GL.GL_LINES)
    GL.glVertex2fv(position1)
    GL.glVertex2fv(position2)
    GL.glEnd()

def Polygon(vertices, inside):
    if inside:
        GL.glBegin(GL.GL_POLYGON)
        for vertex in vertices:
            GL.glVertex2fv(vertex)
        GL.glEnd()
    else:
        for i in range(len(vertices)):
            GL.glBegin(GL.GL_LINES)
            GL.glVertex2fv(vertices[i])
            if i < len(vertices) - 1:
                GL.glVertex2fv(vertices[i + 1])
            else:
                GL.glVertex2fv(vertices[0])
            GL.glEnd()

def Background(display):
    GL.glColor(BackgroundColor)
    Polygon([(0, 0), (0, display[1]), (display[0], display[1]), (display[0], 0)], True)
    GL.glColor(BrushColor)

def Ray(origin, i, radius):
    cosine = radius * math.cos(i * 2 * math.pi) + origin[1]
    sine   = radius * math.sin(i * 2 * math.pi) + origin[0]
    Line(origin, (sine, cosine))
    return sine, cosine

def Point(position):
    Circle((position[0], position[1], 3), 3, True)
