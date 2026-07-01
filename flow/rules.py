# flow/rules.py

from flow.states import *
from ai.intent import classify_intent


def get_next_state(current_state, customer_reply):

    # If already at a terminal state, stay at END
    if current_state in [PAYMENT_INSTRUCTIONS, SAVE_COMMITMENT, CLOSING, END]:
        return END, None

    # Classify the customer intent and extract any date
    intent, extracted_date = classify_intent(current_state, customer_reply)

    # ---------------- VERIFICATION ---------------- #
    if current_state == VERIFICATION:
        if intent == "yes":
            return PERMISSION, None
        else:
            return CLOSING, None

    # ---------------- PERMISSION ---------------- #
    elif current_state == PERMISSION:
        if intent == "yes":
            return OUTSTANDING, None
        else:
            return CLOSING, None

    # ---------------- OUTSTANDING ---------------- #
    elif current_state == OUTSTANDING:
        if intent == "yes":
            return PAYMENT_INSTRUCTIONS, None
        else:
            return WAIVER, None

    # ---------------- WAIVER ---------------- #
    elif current_state == WAIVER:
        if intent == "yes":
            return PAYMENT_INSTRUCTIONS, None
        else:
            return SETTLEMENT, None

    # ---------------- SETTLEMENT ---------------- #
    elif current_state == SETTLEMENT:
        if intent == "yes":
            return PAYMENT_INSTRUCTIONS, None
        else:
            return EMI, None

    # ---------------- EMI ---------------- #
    elif current_state == EMI:
        if intent == "yes":
            return PAYMENT_INSTRUCTIONS, None
        else:
            return TOKEN, None

    # ---------------- TOKEN ---------------- #
    elif current_state == TOKEN:
        if intent == "date" or extracted_date:
            return SAVE_COMMITMENT, extracted_date
        else:
            return CLOSING, None

    return END, None