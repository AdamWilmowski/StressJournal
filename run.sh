#!/bin/bash

# Stress Diary Startup Script

echo "Starting Stress Diary Web Application..."
echo "========================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if any users exist
echo "Checking for existing users..."
if ! python -c "from app import app, db, User; app.app_context().push(); print('Users found:', User.query.count())" 2>/dev/null | grep -q "Users found: [1-9]"; then
    echo ""
    echo "⚠️  No users found in the database!"
    echo "You need to create a user account first."
    echo "Run: python create_user.py"
    echo ""
    read -p "Do you want to create a user now? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        python create_user.py
    else
        echo "Please create a user account before starting the application."
        exit 1
    fi
fi

# Start the application
echo "Starting Flask application..."
echo "The app will be available at:"
echo "  - Local: http://localhost:5000"
echo "  - Network: http://$(hostname -I | awk '{print $1}'):5000"
echo ""
echo "Press Ctrl+C to stop the application"
echo "========================================"

python app.py
