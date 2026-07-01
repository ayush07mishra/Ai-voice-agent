import os
import streamlit as st

from ai.ollama_client import ask_ai
from customer.loader import load_customer
from flow.manager import ConversationManager
from flow.prompt_builder import build_prompt
from flow.rules import get_next_state
from flow.states import END, PAYMENT_INSTRUCTIONS, SAVE_COMMITMENT, CLOSING


# -------------------------
# Initial Setup
# -------------------------

st.set_page_config(
    page_title="KreditBee AI Collection Agent",
    page_icon="💰",
    layout="centered"
)

st.title("💰 KreditBee AI Collection Agent")


customer = load_customer()

# Store conversation state
if "manager" not in st.session_state:
    st.session_state.manager = ConversationManager()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "finished" not in st.session_state:
    st.session_state.finished = False

if "play_audio" not in st.session_state:
    st.session_state.play_audio = False


# -------------------------
# Show Previous Messages
# -------------------------

for role, message in st.session_state.messages:

    if role == "agent":
        st.chat_message("assistant").write(message)

    else:
        st.chat_message("user").write(message)


# -------------------------
# Play Speech Audio
# -------------------------

audio_file = None
if os.path.exists("voice.wav"):
    audio_file = "voice.wav"
elif os.path.exists("voice.mp3"):
    audio_file = "voice.mp3"

if audio_file and st.session_state.play_audio:
    st.audio(audio_file, format=f"audio/{audio_file.split('.')[-1]}", autoplay=True)
    st.session_state.play_audio = False


# -------------------------
# Stop if finished
# -------------------------

if st.session_state.finished:

    st.success("Conversation Finished ✅")
    st.stop()


# -------------------------
# Generate Agent Message
# -------------------------

if len(st.session_state.messages) == 0 or st.session_state.messages[-1][0] == "user":

    state = st.session_state.manager.get_state()

    if state == END:

        st.session_state.finished = True
        st.rerun()

    promise_date = st.session_state.manager.get_promise_date()
    prompt = build_prompt(state, customer, last_reply=promise_date)

    reply = ask_ai(prompt)

    st.session_state.messages.append(("agent", reply))

    # Generate TTS audio for the reply
    from voice.tts import speak
    speak(reply)
    st.session_state.play_audio = True

    if state in [PAYMENT_INSTRUCTIONS, SAVE_COMMITMENT, CLOSING]:
        st.session_state.manager.set_state(END)
        st.session_state.finished = True

    st.rerun()


# -------------------------
# Voice Input Button
# -------------------------

if not st.session_state.finished:
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("🎤 Speak"):
            from voice.stt import listen
            with st.spinner("Listening... Speak into microphone..."):
                voice_reply = listen()
            if voice_reply:
                st.session_state.messages.append(("user", voice_reply))
                current_state = st.session_state.manager.get_state()
                next_state, promise_date = get_next_state(current_state, voice_reply)
                st.session_state.manager.set_state(next_state)
                if promise_date:
                    st.session_state.manager.set_promise_date(promise_date)
                st.rerun()
            else:
                st.warning("Could not capture speech. Click 'Speak' again or type below.")


# -------------------------
# Customer Input (Keyboard Fallback)
# -------------------------

customer_reply = st.chat_input("Type customer reply...")

if customer_reply:

    st.session_state.messages.append(("user", customer_reply))

    current_state = st.session_state.manager.get_state()

    next_state, promise_date = get_next_state(current_state, customer_reply)

    st.session_state.manager.set_state(next_state)
    if promise_date:
        st.session_state.manager.set_promise_date(promise_date)

    st.rerun()