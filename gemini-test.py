from typing import Tuple, List
from collections import namedtuple
from gemini import PromptGenerator, TopicWithSubject, Subject

generator = PromptGenerator()

generator.set_text("Hello, this is a test prompt.")
generator.set_topic_current(TopicWithSubject(
  name = "motorcycles",
  feel = "positive",
  subjects = [Subject(name="oil leak", feel="negative")]
))
generator.set_topic_history([
  TopicWithSubject(
    name = "climbing",
    feel = "positive", 
    subjects = [
      Subject(name = "lace climbing shoes", feel = "neutral"),
      Subject(name = "hook-and-loop climbing shoes", feel = "positive"),
      Subject(name = "belaying", feel = "positive")
    ],
  ),
  TopicWithSubject(
    name = "studying mathematics",
    feel = "positive", 
    subjects = [
      Subject(name = "abstract algebra", feel = "neutral"),
      Subject(name = "calculus", feel = "positive"),
    ]
  )
])

# print(generator.prompt["text"])
print(generator.get_prompt_json())
