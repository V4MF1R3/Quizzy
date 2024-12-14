# Quizzy App
live✌️: 'https://quizzy-1-3rz6.onrender.com'

## Overview
Quizzy is a Django-based application designed to provide a platform for interactive quizzes. It features various functionalities like starting a quiz, answering questions, and viewing results.

## Features
* Quizzes: Start quizzes, answer questions, and view results.
* Static File Support: Integrated with WhiteNoise to serve static files efficiently.
* Clean URLs: URLs are designed to be user-friendly and SEO-friendly.

## Prerequisites
* Python 3.11+
* Django 5.1.4+
* A virtual environment (recommended)

## Installation
1. Clone the repository:

    ```bash
    Copy code
    git clone https://github.com/your-username/quizzy.git
    cd quizzy

2. Set up a virtual environment and install dependencies:

    ```bash
    Copy code
    python -m venv .venv
    source .venv/bin/activate  # On Windows use .venv\Scripts\activate
    pip install -r requirements.txt

3. Apply migrations:

    ```bash
    Copy code
    python manage.py migrate

4. Collect static files:

    ```bash
    python manage.py collectstatic

5. Start the development server:

    ```bash
    python manage.py runserver

## Configuration
* Environment Variables: Create a `.env` file with necessary environment variables (like database configurations, secret keys, etc.).

* Allowed Hosts: Ensure `ALLOWED_HOSTS` is set correctly in `settings.py`:

    ```bash
    ALLOWED_HOSTS = ['127.0.0.1', 'yourdomain.com']

* WhiteNoise Middleware: Ensure WhiteNoise middleware is added to your MIDDLEWARE setting:

    ```bash
    MIDDLEWARE = [
        ...
        'whitenoise.middleware.WhiteNoiseMiddleware',
        ...
    ]

## Usage
1. Visit the app at 'http://127.0.0.1:8000/'.
2. Navigate through quiz sessions, answer questions, and view results.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Submit a pull request.

## License
MIT © V4mF1R3