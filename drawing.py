"""
This file imports modules from pixart and draws shapes from file input
"""

from turtle import Screen, Turtle
from pixart import initialization, draw_shape_from_string, draw_grid, draw_from_file

def main():
    turta = Turtle()

    initialization(turta)

    # sc = Screen()
    # draw_grid(turta)
    # draw_shape_from_string(turta)
    # sc.exitonclick()

    draw_from_file(turta, Screen)

if __name__ == "__main__":
  main()
