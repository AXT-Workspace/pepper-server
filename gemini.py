from typing import Tuple, List, Optional
from dataclasses import dataclass
import json
from google import genai
import os

# client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
# response = client.models.generate_content(
#     model="gemini-2.0-flash-lite-preview-02-05", contents="Explain how AI works"
# )
# print(response.text)

@dataclass
class Subject:
    name: str  # The name of the subject (sub-topic)
    feel: str  # The user's feeling about the subject (negative, neutral, positive)

@dataclass
class TopicWithSubject:
    name: str
    feel: str
    subjects: Optional[List[Subject]] = None

class PromptGenerator:
    def __init__(self):
        """
        Prompt dictionary is the main JSON object on the sent request.
        TopicWithSubject object contains a list of Subjects that have parent-children relationship based on index.
        
        "prompt": {
            "text": "REQUIRED. Raw prompt text taken from the STT.",
            "history": "OPTIONAL. List of TopicWithSubject objects with recent previous conversations topics.",
            "current": "OPTIONAL. TopicWithSubject object of current topic and subjects.
        }
        """
        self.prompt = {}
        
    def set_text(self, text: str):
        self.prompt["text"] = text

    def set_topic_current(self, topic: TopicWithSubject):
        processed_dict = {}
        if topic.subjects is not None:
            subject_strings = [f"{subject.name}, {subject.feel}" for subject in topic.subjects]
            
            processed_dict[f"{topic.name},{topic.feel}"] = subject_strings
        else:
            processed_dict[f"{topic.name},{topic.feel}"] = ""
            
        self.prompt["topic"] = processed_dict
    
    def set_topic_history(self, topic_list: List[TopicWithSubject]):
        processed_dict = {}
        for topic in topic_list:
            if topic.subjects is not None:
                subject_strings = [f"{subject.name}, {subject.feel}" for subject in topic.subjects]
                
                processed_dict[f"{topic.name},{topic.feel}"] = subject_strings
            else:
                processed_dict[f"{topic.name},{topic.feel}"] = ""

        self.prompt["history"] = processed_dict
        
    def get_prompt_json(self):
        return json.dumps(self.prompt, indent=4)