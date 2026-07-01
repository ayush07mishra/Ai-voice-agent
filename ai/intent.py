# ai/intent.py

import json
import re
from ai.ollama_client import ask_ai


def classify_intent(state, customer_reply):
    prompt = f"""
You are an intent classifier for a debt collection bot.
Analyze the customer's reply in the context of the current conversation stage.

Current Stage: {state}
Customer Reply: "{customer_reply}"

Determine the customer's intent:
1. For stages VERIFICATION, PERMISSION, OUTSTANDING, WAIVER, SETTLEMENT, EMI:
   - "yes": If the customer agrees, says yes, confirms, is willing, says "haan", "theek hai", "ji", "kar dunga", "kar dungi", "ok", "sure", etc.
   - "no": If the customer disagrees, says no, refuses, is busy, wrong number, says "nahi", "no", "busy", "baad mein", "nahi ho payega", etc.
2. For stage TOKEN:
   - "date": If the customer promises to pay and provides a specific date or time frame (e.g., "5 तारीख", "monday", "next week", "10th July", "kal", "parso", "10 tarikh").
   - "no": If the customer refuses to pay, says they have no money, or does not give any date.

Return ONLY a JSON object with the following format:
{{
  "intent": "yes" or "no" or "date",
  "extracted_date": "the date/day mentioned by the customer (in English or Hindi) if intent is date, otherwise null"
}}

Do not return any other text, code blocks, or explanations. Only the raw JSON.
"""

    response = ask_ai(prompt)

    try:
        # Robustly extract JSON object using regex to ignore any surrounding text from the LLM
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            clean_response = json_match.group(0)
            data = json.loads(clean_response)
            intent = data.get("intent", "no")
            extracted_date = data.get("extracted_date", None)
            return intent, extracted_date
        raise ValueError("No JSON found")

    except Exception:
        # Fallback to simple keyword/regex pattern matching
        reply_lower = customer_reply.lower()

        # Check for date keywords if in TOKEN state
        if state == "TOKEN":
            # Simple check for numbers or common date terms
            date_match = re.search(r'\d+|tarikh|tareekh|taarikh|date|monday|tuesday|wednesday|thursday|friday|saturday|sunday|kal|parso|week|month|july', reply_lower)
            if date_match:
                return "date", customer_reply
            return "no", None

        # Check for yes/no keywords
        yes_keywords = ["yes", "haan", "ji", "ok", "yep", "sure", "हाँ", "जी", "कर दू", "कर दूंगा", "कर दूंगी", "agree", "theek"]
        no_keywords = ["no", "nahi", "busy", "wrong", "baad", "na", "गलत", "नहीं", "नहीं होगा"]

        for w in yes_keywords:
            if w in reply_lower:
                return "yes", None
        for w in no_keywords:
            if w in reply_lower:
                return "no", None

        return "no", None
