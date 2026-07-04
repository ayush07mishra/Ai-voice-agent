
Start
   │
   ▼
1. Introduction & Customer Verification
   │
   ▼
2. Ask Permission to Talk (2-minute confirmation)
   │
   ▼
3. Inform Outstanding Amount
   │
   ▼
4. Ask for Full Payment
   │
   ├── Yes → Payment Instructions → End
   │
   └── No
        │
        ▼
5. Offer Waiver
        │
        ├── Yes → Payment Instructions → End
        │
        └── No
             │
             ▼
6. Offer One-Time Settlement
             │
             ├── Yes → Settlement Process → End
             │
             └── No
                  │
                  ▼
7. Offer EMI / Partial Payment
                  │
                  ├── Yes → EMI Arrangement → End
                  │
                  └── No
                       │
                       ▼
8. Ask for Token Payment / Promise to Pay
                       │
                       ├── Customer Gives Date
                       │        │
                       │        ▼
                       │   Save Commitment
                       │
                       ▼
9. Closing



State machine - > to maintain the flow ( if else ) so that AI will not give accurate answer


ollama_client.py
Purpose: Communicates with the Ollama server.
If asked "What does it do?"
Answer: It acts as a bridge between the Python application and the local Ollama model.

intent.py
Purpose: Understand customer replies.
Example
Customer says
I don't have money.
Intent : NO_PAYMENT
Instead of checking hundreds of if-else conditions, AI understands the customer's intent.
loader.py- LOAD JSON 

flow/

states.py - Contains conversation states.
Example
VERIFICATION
↓
PERMISSION
↓
OUTSTANDING
↓
WAIVER
↓
SETTLEMENT
↓
EMI
↓
TOKEN
↓
END

Think of it as a roadmap.

manager.py
Stores
Current State
Example
Current
↓
VERIFICATION
Later
Current
↓
OUTSTANDING
It remembers where the conversation currently is.

rules.py
This file contains business logic.
Example
Customer says
YES
↓
END

Customer says
NO
↓
Move to

WAIVER
Python makes all decisions.
Not AI.
scripts.py
This is your SOP.
It contains
Verification Script
Outstanding Script
Waiver Script
Settlement Script
Each stage has its own predefined dialogue.
prompt_builder.py
Originally,

this generated prompts for Ollama.

If you moved to scripts,

say

This file was initially designed for dynamic prompt generation when using Ollama for dialogue generation. Later, I shifted to fixed business scripts to maintain compliance with the collection process.

That sounds very professional.

voice/
tts.py

Purpose

Convert text into speech.

Flow

Text

↓

Piper

↓

wav file

↓

Speaker
stt.py

Speech To Text

Microphone

↓

Text

Currently optional.

config.py

Contains

Model name

Voice model

Configuration

Keeping configuration separate avoids changing code everywhere.

prompts.py

If asked

"What is prompts.py?"

Say

It contains system prompts used to guide the AI model's behavior whenever Ollama is used.

app.py

This is the entry point.

Everything starts here.

Flow

Load Customer

↓

Initialize Conversation

↓

Current State

↓

Generate Script

↓

Voice Output

↓

Receive Customer Reply

↓

Update State

↓

Repeat
Complete Flow

This is the most important answer.

Application Starts

↓

Load Customer

↓

Current Stage

↓

Generate Script

↓

Text To Speech

↓

Customer Listens

↓

Customer Replies

↓

Business Rules

↓

Next State

↓

Repeat

↓

Call Ends
Why use a State Machine?

This is a favorite interview question.

Wrong approach

AI decides everything

Correct

Python

↓

Current State

↓

Allowed Next State

↓

AI only helps

State machines guarantee

correct order
no skipped steps
predictable behavior
Why Python instead of AI?

Because business rules should never depend on AI.

For example,

If customer refuses payment,

we must

Offer Waiver

Not

Offer EMI

Python guarantees this.

Why Ollama?

Because

Free
Offline
Local
No API cost
Fast
Why Piper?

Converts

Text

↓

Speech

Offline.

Difference between Ollama and Piper

Very important.

Ollama

Brain

Piper

Voice
Difference between STT and TTS

STT

Voice

↓

Text

TTS

Text

↓

Voice
If they ask "Why didn't you use ChatGPT API?"

Answer

I wanted a fully offline solution with no API cost, so I selected Ollama. It allows running open-source language models locally while maintaining user privacy and reducing operational cost.

If they ask "What is the biggest challenge?"

Answer

The biggest challenge was maintaining a strict collection workflow while using AI. Large language models tend to improvise responses, so I separated the business logic from the AI logic. Python controls the workflow through a state machine, while AI is only responsible for understanding customer responses and generating natural language when required.

If they ask "How can this project be improved?"

Say:

Connect with Twilio or Exotel for real phone calls.
Replace typed customer responses with Whisper for speech recognition.
Store customer data in a SQL database instead of JSON.
Add authentication for agents.
Integrate payment APIs.
Add call recording and analytics.
Build an admin dashboard to monitor calls and outcomes.
My last piece of advice for your presentation

Don't present it as a "chatbot".

Present it as:

"An AI-powered Collection Calling Agent that uses a state machine to enforce business rules, a local LLM (Ollama) for conversational intelligence, and a Text-to-Speech engine to simulate real outbound collection calls."

That framing immediately makes the project sound more like an enterprise application than a simple chatbot. It also accurately reflects the architecture you've built.