from mycroft import MycroftSkill, intent_file_handler
from elasticsearch import Elasticsearch

client = Elasticsearch(self.settings.elastichost

class RecipeFinder(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('recipe.finder.intent')
    def handle_recipe_finder(self, message):
        recipe = message.data.get('type')
        if recipe is not None:
            result = search(message.data.get('recipe'))
            self.speaking_dialog('')
        else
            self.speak_dialog("A recipe was not found.")
        #self.speak_dialog('finder.recipe')

    def search(self, name, index="recipes", size=1):
        response = client.search(
            index=index,
            body={
                "size": size,
                "query": {
                    "match": {
                        "name": name
                    }
                }
            }
        )

        return response

    def stop(self):
        pass


def create_skill():
    return RecipeFinder()




