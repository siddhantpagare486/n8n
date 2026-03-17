🚀 AI-Powered Document Orchestrator

An end-to-end AI-driven document processing and automation system that extracts insights from documents and triggers intelligent workflows using Streamlit, Gemini API, and n8n.

📌 Project Overview

The AI-Powered Document Orchestrator is designed to automate document analysis and business workflows. It allows users to upload documents, extract meaningful insights using AI, and trigger automated actions like sending emails based on extracted data.

This project demonstrates real-world applications of:

Dynamic AI Extraction

Business Process Automation (BPA)

Workflow Orchestration

🎯 Key Features

✅ Upload and process documents (PDF, TXT, DOCX)
✅ AI-powered data extraction using Gemini API
✅ Clean and interactive UI using Streamlit
✅ Conditional workflow automation using n8n
✅ Automated email notifications based on extracted insights
✅ Modular and scalable architecture

🛠️ Tech Stack

Frontend: Streamlit

Backend: Python

AI Model: Google Gemini API

Automation: n8n

Other Tools: Pandas, Requests, SMTP

🧠 How It Works

User uploads a document via Streamlit UI

Backend processes the document using Python

Gemini API extracts structured information

Extracted data is evaluated based on conditions

n8n workflow is triggered via webhook

Email is automatically sent based on conditions

🏗️ Project Structure
AI-Document-Orchestrator/
│
├── app.py                  # Streamlit frontend
├── backend/
│   ├── extractor.py        # Gemini API logic
│   ├── parser.py           # Document parsing
│   └── utils.py
│
├── workflows/
│   └── n8n_workflow.json   # n8n automation workflow
│
├── requirements.txt
└── README.md
⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/AI-Document-Orchestrator.git
cd AI-Document-Orchestrator
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Add API Keys

Create a .env file and add:

GEMINI_API_KEY=your_api_key_here
4️⃣ Run the Streamlit App
streamlit run app.py
5️⃣ Setup n8n Workflow

Open n8n

Import the workflow from /workflows/n8n_workflow.json

Configure:

Webhook URL

Email credentials (SMTP / Gmail)

🔗 API Integration (Gemini)

Example usage:

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Extract key info from this document")

print(response.text)
📧 Automation Logic (n8n)

Trigger: Webhook from Streamlit backend

Condition: Extracted data meets criteria (e.g., invoice > ₹50,000)

Action: Send email notification

📊 Use Cases

Invoice processing & alerts

Resume screening automation

Legal document summarization

Business report insights

Customer feedback analysis

🚀 Future Improvements

Add OCR for scanned documents

Multi-language support

Dashboard for analytics

Database integration (PostgreSQL)

Role-based access

🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

📜 License

This project is licensed under the MIT License.

👤 Author

Siddhant Pagare
📧 siddhantpagare913@gmail.com

⭐ If you like this project

Give it a ⭐ on GitHub and share it!
