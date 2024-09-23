"""
This file creates a table and draws a cake on the table based on user input.
"""

from turtle import Screen, Turtle


def draw_rect(height, width, color, turta):
    """
    This function draws a rectangle.
    height: integer
    width: integer
    color: string
    turta: Turtle
    """
    turta.begin_fill()
    turta.fillcolor(color)
    turta.pencolor(color)

    turta.fd(width / 2)
    turta.left(90)
    turta.fd(height)
    turta.left(90)
    turta.fd(width)
    turta.left(90)
    turta.fd(height)
    turta.left(90)
    turta.fd(width / 2)

    turta.end_fill()


def draw_plate(plate_length, plate_width, plate_color, turta):
    """
    This function draws a plate.
    table_width: integer
    turta: Turtle
    """
    turta.up()
    turta.goto(0, 1)
    turta.down()

    # Draw a plate
    draw_rect(plate_width, plate_length, "gray", turta)


def draw_candle(turta):
    """
    This function draws a blue candle.
    turta: Turtle
    """
    # Store coords to go back later
    before_candle_x = turta.xcor()
    before_candle_y = turta.ycor()

    draw_rect(10, 2.5, "blue", turta)

    turta.up()
    turta.goto(before_candle_x, before_candle_y + 12)
    turta.down()

    # Flame
    turta.begin_fill()
    turta.pencolor("yellow")
    turta.fillcolor("yellow")
    turta.circle(3)
    turta.end_fill()

    # Go back to before drawing the candle
    turta.up()
    turta.goto(before_candle_x, before_candle_y)
    turta.down()


def draw_cherry(turta):
    """
    This function draws a small red cherry.
    turta: Turtle
    """
    turta.pencolor("red")
    turta.begin_fill()
    turta.fillcolor("red")
    turta.circle(10)
    turta.end_fill()


def draw_icing(layer_width, turta):
    """
    This function draws white icing on the cake.
    layer_width: integer
    turta: Turtle
    """
    turta.pencolor("white")
    turta.begin_fill()
    turta.fillcolor("white")
    turta.bk(layer_width / 2)
    turta.right(90)
    turta.down()
    turta.circle(layer_width / 10, 180)
    turta.right(180)
    turta.circle(layer_width / 10, 180)
    turta.right(180)
    turta.circle(layer_width / 10, 180)
    turta.right(180)
    turta.circle(layer_width / 10, 180)
    turta.right(180)
    turta.circle(layer_width / 10, 180)
    turta.right(90)
    turta.end_fill()


def draw_cake(cake_length, cake_color1, cake_color2, cake_color3, turta):
    """
    This function draws a cake.
    cake_length: integer
    cake_color1: string
    cake_color2: string
    cake_color3: string
    turta: Turtle
    """
    # Plate properties
    plate_length = cake_length * 2
    plate_width = 5
    plate_color = "gray"

    # draw plate first
    draw_plate(plate_length, plate_width, plate_color, turta)

    turta.up()
    turta.goto(0, 7)
    turta.down()

    layerheight = cake_length / 3          # 3 layers 
    layer1width = 0.9 * (cake_length * 2)  # 90% of the cake width
    layer2width = 0.8 * (cake_length * 2)  # 80% of the cake width
    layer3width = 0.7 * (cake_length * 2)  # 70% of the cake width

    # Draw first layer of cake
    draw_rect(layerheight, layer1width, cake_color1, turta)

    # Move up
    turta.up()
    turta.goto(0, 7 + layerheight)
    turta.down()

    # Draw second layer of cake
    draw_rect(layerheight, layer2width, cake_color2, turta)

    # Move up
    turta.up()
    turta.goto(0, 7 + layerheight * 2)
    turta.down()

    # Draw third layer of cake
    draw_rect(layerheight, layer3width, cake_color3, turta)

    # Move up
    turta.up()
    turta.goto(0, 7 + layerheight * 3)

    # Icing
    draw_icing(layer3width, turta)

    # Move up
    turta.up()
    turta.goto(0, 7 + layerheight * 3)
    turta.down()

    turta.fd(0.1 * cake_length + 10)  # Move a bit to the right to draw the candle

    # Draw the candle
    draw_candle(turta)

    turta.up()
    turta.bk(
        0.1 * cake_length + 10
    )  # Move back to the left once the candle is done to draw the cherry
    turta.down()

    # Draw red cherry on top
    draw_cherry(turta)


def table_leg(table_size, turta):
    """
    This function draws a leg of the table.
    table_size: integer
    turta: Turtle
    """
    turta.left(90)
    turta.fd(table_size / 2)
    turta.right(86)
    turta.fd(table_size / 25)  # Width of the leg
    turta.right(60)
    turta.fd(table_size / 7)  # Going to the back right leg
    turta.right(34)
    turta.fd(table_size / 2.6)  # Going up to the table to draw next leg
    turta.right(90)
    turta.fd(table_size / 25)
    turta.right(90)
    turta.fd(table_size / 2.6)
    turta.left(35)
    turta.fd(table_size / 13)
    turta.left(145)
    turta.fd(table_size / 2.23)
    turta.left(90)


def table_right_side(table_size, turta):
    """
    This function the right side of the table.
    table_size: integer
    turta: Turtle
    """
    turta.fd(table_size / 2)
    turta.right(45)
    turta.fd(table_size / 13)
    turta.right(135)
    turta.fd(table_size / 13)


def table_left_side(table_size, turta):
    """
    This function draws the left size of the table.
    table_size: integer
    turta: Turtle
    """
    turta.right(135)
    turta.fd(table_size / 13)
    turta.right(45)
    turta.fd(table_size / 13)
    turta.goto(0, 0)


def draw_table(table_size, table_color, turta):
    """
    This def function is supposed to make a table with 4 legs
    table_size and table_color are manually entered by the user.
    table_size: integer
    table_color: string
    turta: Turtle
    """
    table_size = table_size * 2

    turta.begin_fill()
    turta.fillcolor(table_color)
    turta.pencolor(table_color)
    table_right_side(table_size, turta)
    table_leg(table_size, turta)
    turta.fd(table_size * 0.4)
    turta.fd(table_size * 0.4)
    table_leg(table_size, turta)
    turta.fd(table_size / 6.5)
    table_left_side(table_size, turta)
    turta.end_fill()


def main():
    user_name = input("Hello! What is your name?: ")
    table_length = int(
        input("Please enter the length of one side of a table (30 - 150): ")
    )

    # If table length is lesser than 30
    # Or greater than 150
    # Print and exit
    if table_length < 30 or table_length > 150:
        print("Invalid table size.")
    else:
        # Else continue with the program
        table_color = input("Please enter the color of the table: ")
        cake_length = int(
            input(
                "Please enter the size of the cake (should be smaller than the table): "
            )
        )
        cake_color1 = input("Enter color for layer 1 of the cake: ")
        cake_color2 = input("Enter color for layer 2 of the cake: ")
        cake_color3 = input("Enter color for layer 3 of the cake: ")

        # If cake is bigger than the table,
        # Make it the same size
        if cake_length > table_length:
            cake_length = table_length

        sc = Screen()
        turta = Turtle()
        sc.bgcolor("light blue")

        print(f"\nYour cake is loading! Happy birthday, {user_name}\n")
        print("\nClose the canvas window in order to quit...")

        draw_table(table_length, table_color, turta)
        draw_cake(cake_length, cake_color1, cake_color2, cake_color3, turta)

        # Return to where it started
        turta.up()
        turta.goto(0, 0)

        sc.exitonclick()


if __name__ == "__main__":
    main()
