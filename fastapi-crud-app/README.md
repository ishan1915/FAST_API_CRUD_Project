## File: README.md
# FastAPI CRUD App

A simple CRUD (Create, Read, Update, Delete) application built with FastAPI.

## Features
- Create an item
- Read all items or a single item
- Update an item
- Delete an item

## Project Structure
```
fastapi-crud-app/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── routes/
│       └── items.py
├── requirements.txt
└── README.md
```

## Running the App
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

## License
MIT
