from flask import Flask, render_template

app = Flask(__name__)


# -----------------------------
# HOME PAGE
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# ABOUT PAGE
# -----------------------------
@app.route("/about")
def about():
    return render_template("about.html")


# -----------------------------
# SERVICES MAIN PAGE
# -----------------------------
@app.route("/services")
def services():
    return render_template("services.html")


# -----------------------------
# INDIVIDUAL SERVICE PAGES
# -----------------------------
@app.route("/services/income-tax")
def income_tax():
    return render_template("income_tax.html")


@app.route("/services/gst")
def gst():
    return render_template("gst.html")


@app.route("/services/accounting")
def accounting():
    return render_template("accounting.html")


@app.route("/services/audit")
def audit():
    return render_template("audit.html")


@app.route("/services/financial-advisory")
def financial_advisory():
    return render_template("financial_advisory.html")


# -----------------------------
# CONTACT PAGE
# -----------------------------
@app.route("/contact")
def contact():
    return render_template("contact.html")


# -----------------------------
# RUN APPLICATION
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)