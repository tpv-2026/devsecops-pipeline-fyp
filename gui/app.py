from __future__ import annotations

import json
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "summary.json"

def load_summary() -> dict:
    """Loads dashboard data from the JSON file """
    if not DATA_FILE.exists():
        return {
            "pipeline_status": "Unknown",
            "last_run": "N/A",
            "vulnerabilities": {
                "critical": 0,
                "high": 0,
                "medium": 0,
                "low": 0,
            },
            "compliance_score": 0,
            "failed_checks": [],
        }
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/")
def dashboard():
    """Renders the main dashboard page"""
    summary = load_summary()
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)