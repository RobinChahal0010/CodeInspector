# 🕵️ CodeInspector – Python Code Analysis Tool

**Analyze, inspect, and improve your Python code effortlessly!**  
CodeInspector is a Flask-based web application designed to help Python developers assess code quality by checking syntax, measuring complexity, calculating metrics, and generating detailed PDF reports — all in one place.

---

## 🚀 Features

✅ **Python Code Analysis**
- Syntax validation using `ast`
- Cyclomatic complexity with `radon`
- Halstead metrics to understand code structure
- Lines of code and comment count

✅ **PDF Reports**
- Downloadable reports summarizing analysis results with professional formatting

✅ **Session Management**
- Keeps track of the last analysis for easy access and reporting

✅ **User-Friendly Interface**
- Upload Python files easily and view results with structured, readable metrics

---

## 📂 Supported File Types

- `.py` → Python scripts

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/RobinChahal0010/CodeInspector.git
   cd CodeInspector
Create and activate a virtual environment (optional but recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the app

bash
Copy code
python app.py
Open the app in your browser
Visit http://127.0.0.1:5000

📖 How to Use
Upload a .py file from the homepage.

Get instant insights about syntax errors, complexity, effort, and more.

Download the results as a PDF for sharing or documentation.

🛠 Technologies Used
Backend: Flask

Python Libraries: radon, ast, FPDF

File Handling: Upload and download support with session tracking

Frontend: HTML templates with Bootstrap-based styling


📂 Project Structure
csharp
Copy code
CodeInspector/
├── app.py
├── requirements.txt
├── uploads/             
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
└── README.md
📢 Contribution
Contributions are welcome!
Feel free to fork this project, submit pull requests, or open issues with suggestions or improvements.

📞 Contact
Developed by Robinpreet Chahal
Check out more projects at https://github.com/RobinChahal0010

Let’s empower developers to write smarter, cleaner, and more efficient Python code!

📌 License
This project is open-source and available for modification, improvement, and learning.

