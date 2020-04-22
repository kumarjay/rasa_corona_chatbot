# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

import corona_info as ci


class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")

        # overwrite the representation function of the hotel object
        # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object(
            "hotel", lambda obj: obj["name"] + " (" + obj["city"] + ")"
        )

        super().__init__(knowledge_base)


class ActionHelloWorld(FormAction):

    def name(self) -> Text:
        return "action_form"
    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        print('required_slots(tracker: Tracker)')
        return ["name", "email", "district", "country"]


    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:


        #text= tracker.latest_message['text']
        country= tracker.get_slot('country')
        district= tracker.get_slot('district')


        email_id = tracker.get_slot('email')

        information= ci.country_info(country)

        information= str(information)
        ci.send_email(email_id, information)

        dispatcher.utter_message(template="utter_submit", info= information)

        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "name": [self.from_entity(entity='name', intent='name_entity'), self.from_text()],
            "email": [self.from_entity(entity='email', intent='email_entity'), self.from_text()],
            "district": [self.from_entity(entity='district', intent='district_entity'), self.from_text()],
            "country": [self.from_entity(entity='country', intent='country_entity'), self.from_text()],
        }


class ActionMap(FormAction):

    def name(self) -> Text:
        return 'action_map'



    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:


        link= ''
        dispatcher.utter_message(template="utter_submit", info= link)

        return []


class ActionState(FormAction):

    def name(self) -> Text:
        return "action_state"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        print('required_slots(tracker: Tracker)')
        return ["state", "district"]

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        # text= tracker.latest_message['text']

        district = tracker.get_slot('district')
        state= tracker.get_slot('state')

        email_id = tracker.get_slot('email')

        information = ci.india_info(state, district)
        print('you are in district slot')

        information = str(information)
        print('information is....', information)
        ci.send_email(email_id, information)

        dispatcher.utter_message(template="utter_submit2", info=information)

        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "state": [self.from_entity(entity='state', intent='state_entity'), self.from_text()],
            "district": [self.from_entity(entity='district', intent='district_entity'), self.from_text()],

        }

class ActionLink(Action):

    def name(self) -> Text:
        return "action_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #link = "https://i.imgur.com/nGF1K8f.jpg"
        link= "https://cnet2.cbsistatic.com/img/7nPNsiTIf7fYTXFRthV7h8J4Kws=/2020/04/03/07c8bb49-4ec5-480b-a977-1614f2484881/john-hopkins-map-april-3-2020.png"
        dispatcher.utter_message(template="utter_cheer_up", abc= 'hello', link=link)

        return []




#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
#


#  iyzcwirxfximfype
