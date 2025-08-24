from flask import Flask, render_template, request
import requests
import math

app = Flask(__name__)

API_URL = "https://remotive.com/api/remote-jobs"


@app.route("/", methods=["GET"])
def index():
    category = request.args.get("category", "")
    query = request.args.get("q", "").lower()
    page = int(request.args.get("page", 1))
    per_page = 10  # Jobs per page

    response = requests.get(API_URL)
    data = response.json()

    jobs = data.get("jobs", [])

    # Filter by category if selected
    if category:
        jobs = [job for job in jobs if job["category"] == category]

    # Filter by search query if provided
    if query:
        jobs = [
            job for job in jobs
            if query in job["title"].lower() or query in job["company_name"].lower()
        ]

    # Extract unique categories
    categories = sorted(set(job["category"] for job in data["jobs"]))

    # Pagination logic
    total_jobs = len(jobs)
    total_pages = math.ceil(total_jobs / per_page)

    start = (page - 1) * per_page
    end = start + per_page
    jobs = jobs[start:end]

    return render_template(
        "index.html",
        jobs=jobs,
        categories=categories,
        selected_category=category,
        query=query,
        page=page,
        total_pages=total_pages
    )


if __name__ == "__main__":
    app.run(debug=True)
