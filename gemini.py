from typing import List, Optional
from pydantic import BaseModel, Field
import json

from dotenv import load_dotenv

load_dotenv()

# client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
# response = client.models.generate_content(
#     model="gemini-2.0-flash-lite-preview-02-05", contents="Explain how AI works"
# )
# print(response.text)


class Subject(BaseModel):
    """
    Represents a subtopic within a single conversation topic.
    
    This model captures both the name of a subject and the user's sentiment
    towards that subject.
    """
    
    name: str = Field(
        ...,
        description="The name of the subject (sub-topic)",
        example="oil leak"
    )
    feel: str = Field(
        ...,
        description="The user's feeling about the subject (negative, neutral, positive)",
        example="negative"
    )

class TopicWithSubject(BaseModel):
    """
    Represents a main conversation topic with associated subjects.
    
    This model captures the primary topic of conversation, the user's overall
    sentiment toward it, and optionally contains a list of more specific subjects
    related to the main topic, each with its own sentiment.
    """
    
    name: str = Field(
        ..., 
        description="The name of the main topic",
        example="motorcycles"
    )
    feel: str = Field(
        ..., 
        description="The user's overall feeling about the topic (negative, neutral, positive)",
        example="positive"
    )
    subjects: Optional[List[Subject]] = Field(
        None,
        description="List of specific subjects related to this topic"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "motorcycles",
                "feel": "positive",
                "subjects": [
                    {"name": "oil leak", "feel": "negative"},
                    {"name": "speed", "feel": "positive"}
                ]
            }
        }

class PromptGenerator:
    def __init__(self):

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