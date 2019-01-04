

from action import Action
from folder import Folder

class OpenFolderAction(Action):

    def __init__(self, folder):
        super.__init__(self)

        self.folder: Folder = folder

        return


    def on_pressed(self):
        folder.open()

        return


