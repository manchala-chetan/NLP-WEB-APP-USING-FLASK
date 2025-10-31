# NLP Web Application

A Flask-based web application that provides various Natural Language Processing (NLP) features using the ParallelDots API.

## Features

- User registration and login system
- Named Entity Recognition (NER)
- Sentiment Analysis
- Abuse Detection

## Setup Instructions

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with the following content:
   ```
   # Flask configuration
   SECRET_KEY=your-secret-key-here
   
   # API keys
   PARALLELDOTS_API_KEY=your-api-key-here
   
   # Database configuration
   DB_FILENAME=users.json
   ```
4. Replace `your-secret-key-here` with a secure random string
5. Replace `your-api-key-here` with your ParallelDots API key

## Running the Application

```
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

- `app.py`: Main Flask application with routes
- `api.py`: Contains functions for interacting with the ParallelDots API
- `db.py`: Database class for user management
- `config.py`: Configuration settings
- `templates/`: HTML templates
- `static/`: Static files (CSS, JavaScript, etc.)

## Security Features

- Password hashing using SHA-256
- Environment variables for sensitive information
- Input validation
- Error handling

## Future Improvements

- Use a more robust database system (SQLite, PostgreSQL, etc.)
- Implement more advanced password hashing (bcrypt)
- Add user profile management
- Implement rate limiting for API calls
- Add more NLP features
