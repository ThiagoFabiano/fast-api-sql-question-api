# FastAPI SQL Question API

This project is a FastAPI application that allows users to ask questions related to SQL queries. The application connects to a PostgreSQL database and utilizes a custom class to generate and execute SQL queries based on user input.

## Project Structure

```
fastapi-sql-question-api
├── src
│   ├── app.py                # Entry point of the FastAPI application
│   ├── database
│   │   ├── __init__.py       # Empty initializer for the database module
│   │   └── vanna_client.py    # Logic to connect to PostgreSQL and run SQL queries
│   ├── api
│   │   ├── __init__.py       # Empty initializer for the api module
│   │   └── routes.py         # API routes for handling questions and SQL execution
│   ├── models
│   │   ├── __init__.py       # Empty initializer for the models module
│   │   └── query.py          # Data models or schemas for API requests and responses
│   └── config.py             # Configuration settings for the application
├── requirements.txt           # List of dependencies for the project
├── .env                       # Environment variables for configuration
├── .env.example               # Example of the environment variables needed
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fastapi-sql-question-api
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in the required database credentials.

5. **Run the application:**
   ```
   uvicorn src.app:app --reload
   ```

## Usage

Once the application is running, you can send a POST request to the `/ask` endpoint with a JSON body containing your question. For example:

```json
{
  "question": "Me liste os produtos e suas quantidades em estoque"
}
```

The application will return the result of the SQL query generated based on your question.

## License

This project is licensed under the MIT License.