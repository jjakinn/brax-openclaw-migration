# CS50 Flask Web Programming - Overview

## Lecture Structure

### Part 1: Introduction to Web Programming (00:00 - 15:00)
- Review of HTTP concepts from previous week
- Transition from static HTML to dynamic web applications
- Introduction to Flask framework
- MVC (Model-View-Controller) paradigm

### Part 2: Flask Basics (15:00 - 30:00)
- Installing Flask: `pip install flask`
- Minimal Flask application structure
- Creating routes with `@app.route()`
- Request/response cycle
- Running Flask: `flask run`

### Part 3: Templates (30:00 - 45:00)
- Separating logic from presentation
- Jinja templating engine
- Template inheritance with `extends`
- Dynamic content with `{{ variable }}`
- Control structures: `{% if %}`, `{% for %}`

### Part 4: Forms (45:00 - 75:00)
- HTML form elements
- GET vs POST methods
- Handling form data with `request.form`
- Input validation
- Preventing SQL injection with parameterized queries

### Part 5: Databases (75:00 - 105:00)
- SQLite integration
- CRUD operations (Create, Read, Update, Delete)
- Displaying database content in templates
- Registration and listing examples

### Part 6: Sessions (105:00 - 120:00)
- HTTP as stateless protocol
- Cookies for session management
- Flask session object
- Login/logout functionality
- Shopping cart example

### Part 7: APIs (120:00 - 144:00)
- RESTful API concepts
- JSON data format
- Creating API endpoints
- Frontend JavaScript integration
- Autocomplete example

## Key Code Patterns

### Basic Flask App
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
```

### Form Handling
```python
@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    # Process registration
```

### Database Operations
```python
db.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", name, sport)
registrants = db.execute("SELECT * FROM registrants")
```

## Security Considerations

- Always validate user input
- Use POST for data modification
- Never trust client-side data
- Use parameterized queries to prevent SQL injection
- Store sessions server-side, not in cookies
