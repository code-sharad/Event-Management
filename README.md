# Event Management System

A web-based event management system built with Django Ninja and SQLLITE.

OpenAPI
https://event-management-456128109301.asia-south1.run.app/api/docs

## Features

- User Authentication and Authorization
- Event Creation and Management
- Participant Registration
- Venue Management


## Tech Stack

- Python 3.8+
- Django 4.x
- Django Ninja (Fast Django REST Framework)


## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- PostgreSQL 12+
- Git

## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/yourusername/event-management.git
cd event-management
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```



6. Apply migrations and create superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

7. Run development server
```bash
python manage.py runserver
```

8. Access the application
- API documentation: `http://localhost:8000/api/docs`
- Admin interface: `http://localhost:8000/admin`
- Default admin credentials (after creating superuser):
  - Use the credentials you created in step 6

## Troubleshooting

- Ensure PostgreSQL service is running
- Check the virtual environment is activated
- For permission issues, verify PostgreSQL user privileges
- Check logs in development server output

## Database Schema

- Users
- Events
- Participants
- Venues
- Categories

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License.
