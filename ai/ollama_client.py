from ollama import chat

from config import MODEL_NAME
from prompts import SYSTEM_PROMPT


def ask_ai(instruction):

    response = chat(

        model=MODEL_NAME,

        messages=[

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": instruction
            }

        ]

    )

    return response["message"]["content"]