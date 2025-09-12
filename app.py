import os
import subprocess
import ast
import io
from flask import Flask, render_template, request, redirect, url_for, session, send_file
from radon.complexity import cc_visit
from radon.metrics import h_visit
from bs4 import BeautifulSoup
from fpdf import FPDF

app = Flask(__name__)
app.secret_key = "supersecretkey123"  # session ke liye mandatory
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ----------------------------
# Python Code Analysis
# ----------------------------
def analyze_python(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    # Syntax check
    try:
        ast.parse(code)
        syntax_ok = True
        syntax_error = None
    except Exception as e:
        syntax_ok = False
        syntax_error = str(e)

    # Cyclomatic Complexity
    functions = cc_visit(code)
    total_complexity = sum(f.complexity for f in functions)

    # Halstead metrics
    halstead_obj = h_visit(code)
    halstead_result = halstead_obj._asdict() if halstead_obj else {}

    # LOC and comment lines
    loc = len(code.splitlines())
    comment_lines = sum(1 for line in code.splitlines() if line.strip().startswith("#"))

    return {
        "syntax_ok": syntax_ok,
        "syntax_error": syntax_error,
        "complexity": total_complexity,
        "halstead": halstead_result,
        "lines": loc,
        "comments": comment_lines
    }




@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["codefile"]
        if uploaded_file:
            file_name = uploaded_file.filename
            file_path = os.path.join(UPLOAD_FOLDER, file_name)
            uploaded_file.save(file_path)
            ext = file_name.split(".")[-1].lower()

            if ext == "py":
                result = analyze_python(file_path)
            
            else:
                result = {"error": "Unsupported file type!"}

            # Store result in session for PDF download
            session["last_analysis"] = result
            session["last_filename"] = file_name
            session["last_file_ext"] = ext

            return redirect(url_for("result_page"))
    return render_template("index.html")

@app.route("/result")
def result_page():
    result = session.get("last_analysis")
    filename = session.get("last_filename", "file")
    ext = session.get("last_file_ext", "py")

    # Simplify result for Python files
    simple_result = {}
    if ext == "py" and result and not result.get("error"):
        simple_result["syntax_ok"] = result.get("syntax_ok")
        simple_result["syntax_error"] = result.get("syntax_error")
        simple_result["complexity"] = result.get("complexity")
        simple_result["lines"] = result.get("lines")
        simple_result["comments"] = result.get("comments")

        halstead = result.get("halstead", {})
        total = halstead.get("total") if halstead else None
        if total:
            simple_result["effort"] = round(total[9], 2)
            simple_result["bugs"] = round(total[11], 4)
    else:
        simple_result = result  # For JS and HTML or error cases

    return render_template("result.html", result=simple_result, filename=filename, ext=ext)

@app.route("/download")
def download_report():
    result = session.get("last_analysis")
    filename = session.get("last_filename", "report")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Analysis Report for {filename}", ln=True)
    pdf.ln(5)

    if result:
        if isinstance(result, dict):
            for k, v in result.items():
                pdf.multi_cell(0, 10, f"{k}: {v}")
        else:
            pdf.multi_cell(0, 10, str(result))

    pdf_bytes = pdf.output(dest='S').encode('latin1')
    return send_file(
        io.BytesIO(pdf_bytes),
        download_name=f"{filename}_report.pdf",
        as_attachment=True,
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    app.run(debug=True)
