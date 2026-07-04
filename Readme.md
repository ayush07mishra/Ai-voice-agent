# 📞 AI-Powered Loan Collection Calling Agent

An AI-powered outbound loan collection calling agent that simulates a real collection executive. The application follows a predefined collection workflow, interacts with customers, manages different conversation stages, and generates voice responses for a call-like experience.

---

## 🚀 Features

- Customer Verification
- Permission to Continue Call
- Outstanding Amount Reminder
- Waiver Offer
- One-Time Settlement Offer
- EMI Option
- Token Payment Request
- Call Closing
- Voice Response using Text-to-Speech
- State-Based Conversation Flow
- Customer Data Management
- Modular Python Architecture

---

## 📂 Project Structure

```
KreditBee-AI-Agent/
│
├── ai/
│   ├── intent.py
│   └── ollama_client.py
│
├── customer/
│   ├── customer.json
│   └── loader.py
│
├── flow/
│   ├── manager.py
│   ├── rules.py
│   ├── scripts.py
│   ├── states.py
│   └── prompt_builder.py
│
├── voice/
│   ├── tts.py
│   └── stt.py
│
├── app.py
├── config.py
├── prompts.py
├── requirements.txt
└── README.md
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Ollama | Local LLM |
| Piper TTS | Text-to-Speech |
| Streamlit | User Interface |
| JSON | Customer Data Storage |

---

# ⚙️ Working Flow

```
Application Starts

        │

        ▼

Load Customer Information

        │

        ▼

Verification Stage

        │

        ▼

Permission Stage

        │

        ▼

Outstanding Amount

        │

        ▼

Waiver Offer

        │

        ▼

Settlement Offer

        │

        ▼

EMI Offer

        │

        ▼

Token Payment

        │

        ▼

Closing
```

---

# 📋 Conversation Flow

### 1. Verification

- Verify customer identity.

Example:

> Hello, am I speaking with Rahul Sharma?

---

### 2. Permission

Introduce the collection executive.

Example:

> My name is Alex and I'm calling from KreditBee regarding your loan account.

---

### 3. Outstanding Amount

Inform customer about outstanding payment.

Example:

> Your outstanding amount is ₹25,000.

---

### 4. Waiver

Offer waiver if customer refuses.

---

### 5. Settlement

Offer One-Time Settlement.

---

### 6. EMI

Offer EMI if settlement is rejected.

---

### 7. Token Payment

Request minimum token payment.

---

### 8. Closing

End the conversation politely.

---

# 🧠 State Machine

The application follows a predefined state machine.

```
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

CLOSING
```

The conversation cannot skip stages.

---

# 📁 Folder Description

## ai/

Contains AI-related modules.

- Intent Detection
- Ollama Communication

---

## customer/

Contains customer records.

- Customer JSON
- Customer Loader

---

## flow/

Contains business logic.

- Conversation Manager
- Rules Engine
- Scripts
- States

---

## voice/

Voice processing.

- Text-to-Speech
- Speech-to-Text

---

# 🔄 Application Flow

```
Customer

↓

Application

↓

Load Customer

↓

Current State

↓

Business Rules

↓

Generate Response

↓

Convert Text to Speech

↓

Customer Hears Voice

↓

Customer Reply

↓

Next State

↓

Repeat
```

---

# 🎤 Voice Support

The project supports voice interaction using:

- Piper Text-to-Speech

The generated dialogue is automatically converted into speech to simulate a real phone conversation.

---

# 📊 Customer Data

Customer details are stored in JSON format.

Example:

```json
{
  "name": "Rahul Sharma",
  "phone": "9876543210",
  "outstanding": 25000,
  "waiver": 22000,
  "settlement": 18000,
  "emi": 5000
}
```

---

# ▶️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

Run the application

```bash
python app.py
```

Or launch the Streamlit interface

```bash
streamlit run ui.py
```

---

# 📌 Advantages

- Modular Architecture
- Easy to Maintain
- Offline Execution
- Simple State Management
- Reusable Components
- Clear Separation of Business Logic
- Easy Future Enhancements

---

# 🔮 Future Enhancements

- Real Phone Call Integration (Twilio / Exotel)
- Whisper Speech Recognition
- SQL Database Support
- Payment Gateway Integration
- Call Recording
- Analytics Dashboard
- Multi-language Support
- Customer Authentication
- Admin Dashboard

---

# 📈 Use Cases

- Loan Collection
- Payment Reminder Calls
- Banking Support
- EMI Reminder
- Debt Recovery Automation
- Customer Follow-up

---

# 👨‍💻 Author

Developed as an AI-powered collection calling agent demonstrating:

- Conversation State Management
- AI Integration
- Voice-Based Interaction
- Modular Python Development
- Business Rule Automation
