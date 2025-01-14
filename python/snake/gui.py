import turtle
from snake.head import go_up, go_down, go_left, go_right, move


class Gui:
    def __init__(self):
        self.screen = self.create_screen()
        self.register_keyboard_bindings()

    def create_screen(self):
        screen = turtle.Screen()
        screen.title("Snake Game")
        screen.bgcolor("green")
        screen.setup(width=600, height=600)
        screen.tracer(0)
        return screen

    def register_keyboard_bindings(self):
        # Keyboard bindings
        self.screen.listen()
        self.screen.onkeypress(go_up, "w")
        self.screen.onkeypress(go_down, "s")
        self.screen.onkeypress(go_left, "a")
        self.screen.onkeypress(go_right, "d")
     