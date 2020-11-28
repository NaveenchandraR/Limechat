# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from datetime import datetime

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_relative"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        curr_time = datetime.now()

        hours = (int(curr_time.strftime("%H"))+5)%24

        delay = int(tracker.get_slot("number_of_hours"))
        final_time = (hours + delay)%24

        if(final_time < 12):
            p = "am"
        else:
            p = "pm"

        time = str(final_time) + " " + p

        print("Sure, I have scheduled a cleaning for " + time + "today")
        dispatcher.utter_message(text="Sure, I have scheduled a cleaning for " + time + "today")

        return []
