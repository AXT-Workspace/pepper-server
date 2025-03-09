from typing import Tuple, List
from collections import namedtuple
from google import genai
import os

client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
response = client.models.generate_content(
    model="gemini-2.0-flash-lite-preview-02-05", contents="Explain how AI works"
)
print(response.text)



Subject = namedtuple("Subject", ["name", "feel"])
TopicSubject = Tuple[str, str, List[Subject]]

class PromptGenerator:
    def __init__(self):
        """
        Prompt dictionary is the main JSON object on the sent request.
        TopicSubject object contains a list of Subjects that have parent-children relationship based on index.
        
        "prompt": {
            "text": "REQUIRED. Raw prompt text taken from the STT.",
            "history": "OPTIONAL. List of TopicSubject objects with recent previous conversations topics.",
            "current": "OPTIONAL. TopicSubject object of current topic and subjects.
        }
        """
        self.final_prompt = ""
        self.topic_current
        self.topic_history = []


    def create_topic(name: str, feel: str, subjects: List[Subject]) -> TopicSubject:
        return (name, feel, subjects)


    def define_topic_current(topic_obj: TopicSubject) -> TopicSubject:
        if topic_obj[2] is not None:
            return (topic_obj[0], topic_obj[1], topic_obj[2])
        return (topic_obj[0], topic_obj[1])
    

    def define_topic_history(topic_list: List[TopicSubject]) -> List[TopicSubject]:
        processed_list: List[TopicSubject] = []
        for topic_obj in topic_list:
            if len(topic_obj) == 3: # Check if subjects are present
                processed_list.append(topic_obj)
            else:
                processed_list.append((topic_obj[0], topic_obj[1], [])) # Add empty list of subjects
        return processed_list
    
    def get_prompt():
        

# Prompt Example
# {
#   "prompt": {
#     "text": "User's input goes here.",
#       "history": "User's specific history, if available, goes here.",
#       "topic": ["Previous_Topic", "likes/dislikes"],
#       "subject": ["Previous_Subject", "likes/dislikes"]
#     },
#     "instruction": "Any specific instruction for Pepper to act on goes here."
#   }
# }