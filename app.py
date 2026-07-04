from ai.ollama_client import ask_ai
from customer.loader import load_customer
from flow.manager import ConversationManager
from flow.prompt_builder import build_prompt
from flow.rules import get_next_state
from flow.scripts import get_script
from flow.states import END, PAYMENT_INSTRUCTIONS, SAVE_COMMITMENT, CLOSING

from flow.scripts import get_script


customer = load_customer()
manager = ConversationManager()


print("=" * 60)
print("KreditBee AI Collection Agent")
print("=" * 60)


while True:

    state = manager.get_state()

    if state == END:

        print("\nConversation Finished.")
        break

    promise_date = manager.get_promise_date()
    # prompt = build_prompt(state, customer, last_reply=promise_date)

    # reply = ask_ai(prompt)
    script = get_script(state, customer)
    reply = get_script(state, customer)
    print(f"\nAgent:\n{reply}")
    from voice.tts import speak
    speak(reply)

    if state in [PAYMENT_INSTRUCTIONS, SAVE_COMMITMENT, CLOSING]:
        manager.set_state(END)
        print("\nConversation Finished.")
        break

    from voice.stt import listen
    customer_reply = listen()
    if not customer_reply:
        customer_reply = input("\nCustomer (Type reply): ")

    next_state, promise_date = get_next_state(state, customer_reply)

    manager.set_state(next_state)
    if promise_date:
        manager.set_promise_date(promise_date)

