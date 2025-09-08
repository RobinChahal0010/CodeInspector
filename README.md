# 🕵️ CodeInspector – Multi-language Code Analysis Tool

**Analyze, inspect, and understand your code like never before!**  
CodeInspector is a Flask-based web application that helps developers assess Python, JavaScript, and HTML code quality by checking syntax, measuring complexity, calculating metrics, and generating detailed PDF reports.

---

## 🚀 Features

✅ **Python Code Analysis**
- Syntax validation using `ast`
- Cyclomatic complexity with `radon`
- Halstead metrics to understand code structure
- Lines of code and comment count

✅ **JavaScript Code Analysis**
- ESLint integration to highlight style and syntax issues

✅ **HTML Code Analysis**
- Counts tags, inline styles, and scripts using `BeautifulSoup`

✅ **PDF Reports**
- Generate downloadable reports summarizing analysis results

✅ **Session Management**
- Keeps track of the last analysis for quick access and report generation

✅ **Simple and Intuitive UI**
- Upload code files easily and view results in a structured format

---

## 📂 Supported File Types

- `.py` → Python scripts  
- `.js` → JavaScript files  
- `.html` / `.htm` → HTML documents  

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
Install ESLint globally for JavaScript analysis

bash
Copy code
npm install -g eslint
Run the app

bash
Copy code
python app.py
Open http://127.0.0.1:5000 in your browser.

📖 How to Use
Upload a .py, .js, or .html file from the homepage.

Get detailed metrics and analysis for the uploaded file.

Download the report as a PDF for sharing or record keeping.

🛠 Technologies Used
Backend: Flask

Python Libraries: radon, ast, BeautifulSoup, FPDF

JavaScript Analysis: ESLint via subprocess

File Handling: Uploads and downloads supported with session tracking

Frontend: HTML templates, CSS styling

⚙ Possible Improvements
✔ Support for more languages (CSS, Java, etc.)
✔ Real-time linting and analysis
✔ Visualizations for complexity metrics
✔ User authentication for personal analysis history
✔ Cloud deployment and scalability enhancements

📂 Project Structure
csharp
Copy code
CodeInspector/
├── app.py
├── requirements.txt
├── uploads/             # Temporary uploads
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
└── README.md
📢 Contribution
Feel free to fork this project and submit pull requests! Suggestions and improvements are always welcome.

📞 Contact
Developed by Robinpreet Chahal
Check out more projects at https://github.com/RobinChahal0010

Empower developers by making code more understandable, maintainable, and efficient. Try CodeInspector today!

yaml
Copy code

---

Let me know if you want:
✔ A `.gitignore` template for this project  
✔ A sample `requirements.txt`  
✔ Instructions on deploying it or adding badges like Python version, license, etc.







Ask ChatGPT





ChatGPT can make mistakes. Check importa
