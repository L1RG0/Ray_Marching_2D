import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time
import Shapes
import Logic
import math

polygons = [[(450, 200), (600, 300), (650, 200), (600,  50)]]

boxes = [(300, 350, 550, 500)]
circles = [(150, 200, 100)]
points = []
camPoint = (150, 400)
pressed = False

def draw(cam_pos, checkedPixel):
    closest_distance = []
    for polygon in polygons:
        Shapes.Polygon(polygon, False)
        closest_distance.append(Logic.DistanceToPolygon(cam_pos, polygon))

    for box in boxes:
        Shapes.Polygon([(box[0], box[1]), (box[0], box[3]), (box[2], box[3]), (box[2], box[1])], False)
        closest_distance.append(Logic.DistanceToBox(cam_pos, box))

    # for point in points:
    #     Shapes.Point(point)

    for circle in circles:
        Shapes.Circle(circle, 32, False)
        closest_distance.append(Logic.DistanceToCircle(cam_pos, circle))

    Shapes.Point(cam_pos)
    Shapes.Circle((cam_pos[0], cam_pos[1], min(closest_distance)), 32, False)
    newPoint = Shapes.Ray(cam_pos, checkedPixel, min(closest_distance))
    if min(closest_distance) > 500 or 0 > newPoint[0] or 800 < newPoint[0] or 0 > newPoint[1] or 600 < newPoint[1]:
        return
    elif min(closest_distance) < 2:
        return
    else:
        draw(newPoint, checkedPixel)

def main():
    global pressed
    global camPoint
    checked_pixel = 0
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glFrustum(0, display[0], 0, display[1], 100, 101)
    glTranslate(0, 0, -100)
    Shapes.BackgroundColor = (0.1, 0.1, 0.1)
    Shapes.BrushColor = (1, .2, 1)
    while True:
        Shapes.Background(display)
        if pygame.mouse.get_pressed(3)[0]:
            camPoint = (pygame.mouse.get_pos()[0], display[1] - pygame.mouse.get_pos()[1])
        elif pygame.mouse.get_pressed(3)[2] and not pressed:
            pressed = True
            checked_pixel += 0.125
        elif not pygame.mouse.get_pressed(3)[2]:
            pressed = False
        draw(camPoint, checked_pixel)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


if __name__ == "__main__":
    main()
