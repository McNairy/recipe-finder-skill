from mycroft import MycroftSkill, intent_file_handler


class RecipeFinder(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('finder.recipe.intent')
    def handle_finder_recipe(self, message):
        self.speak_dialog('finder.recipe')


def create_skill():
    return RecipeFinder()

