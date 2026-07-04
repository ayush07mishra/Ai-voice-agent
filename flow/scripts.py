# def get_script(state, customer):

#     if state == "INTRO":

#         return f"""
# Hello, am I speaking with {customer['name']}?
# """

#     elif state == "OUTSTANDING":

#         return f"""
# My name is AI Agent, and I am calling from KreditBee regarding your loan account.

# Is this a convenient time to talk for about 2 minutes?

# Your total outstanding amount is ₹{customer['outstanding']}.

# We request you to make the full payment today to avoid further collection activity and any negative impact on your credit profile.

# Will you be able to make the full payment today?
# """

#     elif state == "WAIVER":

#         return f"""
# I understand your situation.

# We may be able to offer a waiver on late fees and penalties.

# Your revised payable amount will be ₹{customer['waiver']}.

# Would you be able to close your account today with this payment?
# """

#     elif state == "SETTLEMENT":

#         return f"""
# We can also offer you a One-Time Settlement.

# You can close your loan account by paying ₹{customer['settlement']}.

# Would you like to proceed with this settlement today?
# """

#     elif state == "EMI":

#         return f"""
# If paying the settlement amount today is difficult,

# we can also arrange an EMI or partial payment.

# You can start with ₹{customer['emi']}.

# Would that work for you?
# """

#     elif state == "TOKEN":

#         return """
# I understand your situation.

# Can you make a small token payment today to show your payment intention?

# The remaining amount can be paid later.
# """

#     return "Thank you."
# flow/scripts.py

SCRIPTS = {

    "VERIFICATION": """
Hello, am I speaking with {name}?
""",

    "PERMISSION": """
My name is Alex, and I am calling from KreditBee regarding your loan account.

Is this a convenient time to talk for about 2 minutes?
""",

    "OUTSTANDING": """
Your total outstanding amount is ₹{outstanding}.

We request you to make the full payment today to avoid further collection activity and any negative impact on your credit profile.

Will you be able to make the full payment today?
""",

    "WAIVER": """
I completely understand your situation.

We may be able to offer a waiver on the late fees and penalties.

Your revised payable amount will be ₹{waiver}.

Would you be able to pay this amount today and close your account?
""",

    "SETTLEMENT": """
We can also offer you a One-Time Settlement option.

You can close your account by paying ₹{settlement}.

Would you like to proceed with the settlement today?
""",

    "EMI": """
If paying the settlement amount today is difficult, we can also arrange an EMI or partial payment.

You can start with ₹{emi}.

Would that be convenient for you?
""",

    "TOKEN": """
I understand your situation.

Would you be able to make a small token payment today to show your payment intention?

If not, could you please let me know a suitable date when you will be able to make the payment?
""",

    "PAYMENT_DONE": """
Thank you for confirming.

A payment link has been sent to your registered mobile number.

Kindly complete the payment and share the confirmation once it is done.
""",

    "SAVE_COMMITMENT": """
Thank you for your commitment.

I have noted your promised payment date as {last_reply}.

Please make sure the payment is completed on or before the committed date.

Have a great day.
""",

    "CLOSING": """
Thank you for your time.

Have a wonderful day.
"""
}


def get_script(stage, customer, last_reply=""):

    return SCRIPTS[stage].format(
        name=customer["name"],
        outstanding=customer["outstanding"],
        waiver=customer["waiver"],
        settlement=customer["settlement"],
        emi=customer["emi"],
        last_reply=last_reply
    )