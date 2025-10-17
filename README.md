# DYNAMIC PROFILE API
A simple Django-based REST API that serves a dynamic user profile with a timestamp and a random cat fact.

## Features
- JSON Response: Returns user details (email, name, tech stack), current UTC timestamp in ISO 8601 format, and a random cat fact fetched from the Cat Facts API.
- Error Handling: Gracefully handles failures when fetching cat facts (e.g., network issues), logs errors to cat_errors.log, and provides a fallback message.
- Lightweight: No external dependencies beyond Django and requests for the cat fact API.

## Installation & Setup
1. Clone the Repository
- git clone <repo-url>
- cd dynamic_profile_api

2. Create a Virtual Environment
- python -m venv venv
- source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
- pip install -r requirements.txt

4. Start the Development Server
- python manage.py runserver

# Usage
## API Endpoint
- URL: http://127.0.0.1:8000/me/ (adjust for your URLconf)
- Method: GET
- Response (Success - 200)