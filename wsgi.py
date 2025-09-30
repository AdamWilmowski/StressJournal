"""
WSGI entry point for production deployment.
This file is used by WSGI servers like Gunicorn, uWSGI, etc.
"""

from app import create_app

# Create the Flask application instance
application = create_app()

if __name__ == "__main__":
    application.run()
