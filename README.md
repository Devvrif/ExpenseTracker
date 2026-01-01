🧾 Expense Tracker (Python)
====================================================================

A simple, modular Expense Tracker built in Python to practice 
real-world application structure, file handling, and clean separation of concerns.

📂 Project Structure
====================================================================
ExpenseTracker/
│
├── main.py               # Entry point, menu loop, user interaction
├── expenses.py           # Business logic (add, validate, process expenses)
├── file_manager.py       # File I/O layer (read/write JSON)
├── data/
│   └── expenses.json     # Persistent storage (ignored by git)
├── .gitignore
└── README.md

⚙️ How It Works (Flow)
====================================================================
User
 ↓
main.py            → gets input, shows menu
 ↓
expenses.py        → validates & processes data
 ↓
file_manager.py    → reads/writes JSON
 ↓
expenses.json      → persistent storage

✨ Features
====================================================================
Add expenses with:
Amount
Category
Description
Auto-generated ID
Auto-assigned date
Input validation (rejects invalid data)
Persistent storage using JSON
Clean separation of concerns
Easily extensible (tags, filters, totals, etc.)

▶️ How to Run
===================================================================
python main.py

🛡️ Validation Rules
===================================================================
Amount must be greater than 0
Category and description cannot be empty
Invalid inputs are rejected with clear error messages

🧠 Learning Goals
====================================================================
This project focuses on:
Modular Python design
File handling with JSON
Exception handling
Clean architecture (main → logic → I/O)
Real-world debugging practices

🚀 Future Enhancements
=====================================================================
Show all expenses
Filter by category/date
Category totals
Tags & notes
Export to CSV

📝 Notes 
=====================================================================
data/expenses.json is ignored in .gitignore
Each user starts with a clean dataset
Built as a learning-focused, professional-grade starter project

About me:
======================================================================
Part of my journey from zero to **AI/ML developer**.
Follow along:**@itsrizmohammad** | **linkedin.com/in/mohammedriz**
