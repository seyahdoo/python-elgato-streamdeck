import layout


class Folder:


    def __init__(self):
        
        # List of Actions
        self.actions = []

        self.previous_folder = None

        return

    def set_action(self, space_index, action):
        self.actions[space_index] = action


    def open(self):

        # for each action in actions, draw action
        for i in range(0,len(self.actions)):
            self.actions[i].draw(i)

        # hook layout as current folder
        self.previous_folder = layout.current_folder
        layout.current_folder = self
        return


    def close(self):

        if self.previous_folder:
            self.previous_folder.open()

        return


    def button_pressed(self, space_index):
        
        actions[space_index].on_pressed()


    def button_released(self, space_index):
        
        actions[space_index].on_released()
