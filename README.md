# 🚀 Project Name

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
This project is an attempt to implement the use case "Gen AI Orchestrator for Email and Document Triage/Routing" given as part of Hackathon-2025.


## 🎥 Demo

### Please refer to [/artifacts/demo](https://github.com/ewfx/gaied-ai-enthus/tree/main/artifacts/demo)

🔗[Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
What inspired you to create this project? Describe the problem you're solving.

## ⚙️ What It Does
Extract contents from email and trains the list of sample emails using LLM and uses trained model to classify the new emails to request type and sub request type combination.

## 🛠️ How We Built It
Used python as backend. 
A base open LLM from Hugging Face has been choosen and has been trained on sample supervised set of emails.
Trained and inferred on laptop.

## 🚧 Challenges We Faced
Time constraints :)
Generation of sample email content
Identifying the right model that is apt for classification task as well as runs local.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/gaied-ai-enthus.git
   ```
2. Install dependencies  
   ```sh
   pip install -r requirements.txt (for Python)
   ```
3. Run the project  
   ```sh
   Change directory to code/src and
   Run:
   python preprocessing.py
   python train_classification.py
   python evaluate_email.py
   in the order.

   Or, run
   python app.py which runs all of them in the order. 
   ```

## 🏗️ Tech Stack
- 🔹 Backend: Python
- 🔹 Other: Access to Hugging Face to download model

## 👥 Team
- **Your Name** - [GitHub](#) | [LinkedIn](#)
- **Teammate 2** - [GitHub](#) | [LinkedIn](#)
