from typing import Tuple, List
from collections import namedtuple
import gemini

generator = gemini.PromptGenerator()

generator.set_text("Hello, this is a test prompt.")
generator.set_topic_current(gemini.TopicWithSubject("motorcycles", "positive", [gemini.Subject("oil leak", "negative")]))
generator.set_topic_history([
    gemini.TopicWithSubject("climbing", "positive", 
        [
            gemini.Subject("lace climbing shoes", "neutral"),
            gemini.Subject("hook-and-loop climbing shoes", "positive"),
            gemini.Subject("belaying", "positive")
        ],
    ),
    gemini.TopicWithSubject("studying mathematics", "positive", 
        [
            gemini.Subject("abstract algebra", "neutral"),
            gemini.Subject("calculus", "positive"),
        ]
    )
])

# print(generator.prompt["text"])
print(generator.get_prompt_json())
