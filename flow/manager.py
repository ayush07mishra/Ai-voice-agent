# flow/manager.py

from flow.states import *


class ConversationManager:

    def __init__(self):

        self.state = VERIFICATION
        self.promise_date = None

    def get_state(self):

        return self.state

    def set_state(self, new_state):

        self.state = new_state

    def get_promise_date(self):

        return self.promise_date

    def set_promise_date(self, new_date):

        self.promise_date = new_date