

class Action:

    def __init__(self):

        self.image = None
        self.is_visible = False
        self.current_space = 0
        self.is_pressed = False
        
        return

    def visible(self,space):
        self.is_visible = True
        self.current_space = space
        self.draw()

    def invisible(self):
        self.is_visible = False

    def draw(self):
        if self.is_visible:
            # TODO draw to current space
            pass

        return

    def on_pressed(self):
        self.is_pressed = True
        return

    def on_released(self):
        self.is_pressed = False
        return

    

    