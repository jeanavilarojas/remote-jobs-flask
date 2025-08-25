# Remote Jobs Finder

A simple **Flask web application** that allows users to browse and filter remote job opportunities using the [Remotive API](https://remotive.com/api/remote-jobs).

---

## Features

* **Category Filtering**: View jobs by category or show all available listings.
* **Search Functionality**: Find jobs by title or company name.
* **Pagination**: Results are paginated for better readability.
* **Dark/Light Mode Toggle**: Users can customize their viewing experience.
* **Live Data**: All job postings are fetched in real-time from the Remotive API.

---

## Tech Stack

* **Backend**: [Flask](https://flask.palletsprojects.com/)
* **Frontend**: HTML, Jinja2 templates, Bootstrap 5
* **API**: [Remotive Jobs API](https://remotive.com/api/remote-jobs)
* **Version Control**: Git + GitHub

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/remote-jobs-finder.git
   cd remote-jobs-finder
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # On macOS/Linux
   .venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   flask run
   ```

5. Open your browser and go to `http://127.0.0.1:5000/`

---

## Project Structure

```
remote-jobs-finder/
│
├── app.py              # Main Flask app
├── requirements.txt    # Project dependencies
├── templates/          # HTML templates (Jinja2)
│   ├── base.html
│   ├── index.html
│
└── static/             # Static assets (CSS, JS, images)
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).
