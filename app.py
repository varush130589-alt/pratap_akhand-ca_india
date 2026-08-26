from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# Used for Flask flash messages
app.secret_key = "ca-india-website-secret-key"


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# ABOUT
# ============================================================

@app.route("/about")
def about():
    return render_template("about.html")


# ============================================================
# SERVICES
# ============================================================

@app.route("/services")
def services():
    return render_template("services.html")


# ============================================================
# INDIVIDUAL SERVICE PAGES
# ============================================================

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


# ============================================================
# CONTACT
# ============================================================

@app.route("/contact")
def contact():
    return render_template("contact.html")


# ============================================================
# ENQUIRY FORM
# ============================================================

@app.route("/submit-enquiry", methods=["POST"])
def submit_enquiry():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    service = request.form.get("service", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not service or not message:
        flash(
            "Please complete all required fields before submitting.",
            "error"
        )

        return redirect(
            request.referrer or url_for("home")
        )

    # --------------------------------------------------------
    # TEMPORARY HANDLING
    # --------------------------------------------------------
    # The form is currently connected to Flask and validates
    # submitted information.
    #
    # Permanent database/email integration can be connected
    # separately when the enquiry database is implemented.
    # --------------------------------------------------------

    flash(
        "Thank you. Your enquiry has been received.",
        "success"
    )

    return redirect(
        request.referrer or url_for("home")
    )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)