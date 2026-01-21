## Overview
This project is a test assignment demonstrating automated testing using
Pytest and Playwright. It includes simple UI and API tests showcasing
basic test structure, assertions, and reporting.

## Tech Stack
- Python 3.10+
- Pytest
- Playwright (sync)
- Requests (for API tests)

## Project Structure
tests/
├── ui/
│   └── test_login.py
├── api/
│   ├── test_get.py
│   ├── test_post.py
│   ├── test_put.py
│   └── test_delete.py
pages/
├── login_page.py
└── welcome_page.py

## Installation

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd project

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

playwright install

Run Tests using the following commands:
pytest test_login.py
pytest test_get.py
pytest test_post.py
pytest test_put.py
pytest test_delete.py
pytest --headed
