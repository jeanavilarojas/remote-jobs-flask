from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://remotive.com/api/remote-jobs"

@app.route("/", methods=["GET"])
def index():
    category = request.args.get("category", "")

    response = requests.get(API_URL)
    data = response.json()

    jobs = data.get("jobs", [])

    if category:
        jobs = [job for job in jobs if job["category"] == category]

    categories = sorted(set(job["category"] for job in data["jobs"]))

    return render_template("index.html", jobs=jobs, categories=categories, selected_category=category)


if __name__ == "__main__":
    app.run(debug=True)
