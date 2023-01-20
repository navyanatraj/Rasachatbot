# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

# # from typing import Any, Text, Dict, List
# #
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# #
# #
# # class ActionHelloWorld(Action):
# #
# #     def name(self) -> Text:
# #         return "action_hello_world"
# #
# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #
# #         dispatcher.utter_message(text="Hello World!")
# #
# #         return []
# from typing import Any, Text, Dict, List
# from rasa_sdk.types import DomainDict
# from rasa_sdk import Action, Tracker, FormValidationAction
# from rasa_sdk.executor import CollectingDispatcher
# import requests
# from rasa_sdk.events import SlotSet
# from rasa_sdk.events import AllSlotsReset
# import re
# class ValidateBirthDeathForm(FormValidationAction):  
#     def name(self) -> Text:
#         return "validate_birth_death_form"

#     def validate_email_id(self, slot_value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
#         if slot_value is not None:
#             if re.match(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", slot_value.strip()):
#                 return {"email_id" : slot_value}
#         dispatcher.utter_message(text = "Please enter a valid email id ")    
#         return {"email_id" : None} 
    

#     def validate_date_of_event(self, slot_value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
#         if slot_value is not None:
#             if re.match(r"^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$", slot_value.strip()):
#                 return {"date_of_event" : slot_value}
#         dispatcher.utter_message(text = "Please enter a valid date ")    
#         return {"date_of_event" : None}  
    
# # class SubmitForm(FormValidationAction):  
#     # def name(self) -> Text:
#         # return "action_submit_bd"
#     # def run(self, dispatcher: CollectingDispatcher,
#         # tracker: Tracker,
#         # domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # dispatcher.utter_message(text="Hello World!")
#         # return []