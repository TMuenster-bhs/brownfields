# Source:
# https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900


# Simple Snake Game in Python 3 for Beginners
# By @TokyoEdTech

import time
import random
from snake.segment import new_segment
from snake.food import food
from snake.head import head
import snake
from snake.pen import pen
from snake.head import move

delay = 0.1

# Score
score = 0
high_score = 0

gui = snake.Gui()

segments = []
# Main game loop
while True:
    gui.screen.update()

    # Check for a collision with the border
    def check_border_collision() -> bool:
        return (
            head.xcor() > 290
            or head.xcor() < -290
            or head.ycor() > 290
            or head.ycor() < -290
        )

    if check_border_collision():
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write(
            "Score: {}  High Score: {}".format(score, high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

        # Check for a collision with the food

    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment

        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(
            "Score: {}  High Score: {}".format(score, high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )

        # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write(
                "Score: {}  High Score: {}".format(score, high_score),
                align="center",
                font=("Courier", 24, "normal"),
            )

    time.sleep(delay)

gui.screen.mainloop()
