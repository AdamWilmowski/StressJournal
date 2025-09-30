# Stress Diary Web Application

A Flask-based web application for tracking stress events, analyzing patterns, and managing anxiety. This app allows you to record stress-inducing events from anywhere with internet access and identify connections between different stressors.

## Features

- **Private Access**: Secure login system for authorized users only
  - Pre-configured user accounts only
  - Password hashing for security
  - Session management
  - User-specific data isolation

- **Event Recording**: Track stress events with detailed information including:
  - Title and description
  - Date and time
  - Stress level (1-10 scale)
  - Category (work, relationships, health, etc.)
  - Location
  - Triggers and symptoms
  - Coping strategies used

- **Event Management**: 
  - View all recorded events
  - Edit existing events
  - Delete events
  - Search and filter events

- **Analysis & Insights**:
  - Overview statistics
  - Category breakdown
  - Recent trends
  - Pattern analysis
  - Personalized recommendations

- **Modern UI**: Clean, responsive design that works on desktop and mobile devices

## Installation

1. **Clone or download the project**:
   ```bash
   cd /home/wilma_pl/CursorProjects/StressDiary
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create your user account**:
   ```bash
   python create_user.py
   ```
   Follow the prompts to create your username, email, and password.

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   - Open your web browser
   - Navigate to `http://localhost:5000`
   - Login with your credentials
   - The app will be accessible from any device on your network at `http://YOUR_IP:5000`

## Usage

### Getting Started
1. **Login**: 
   - Use your pre-configured credentials to access your personal stress diary
   - Your session will be maintained until you logout
   - Only authorized users can access the application

### Adding Events
1. Click "Add Event" from the navigation or home page
2. Fill in the event details:
   - **Title**: Brief description of the stress event
   - **Stress Level**: Rate from 1 (low) to 10 (very high)
   - **Date/Time**: When the event occurred
   - **Category**: Type of stressor
   - **Location**: Where it happened
   - **Triggers**: What specifically caused the stress
   - **Symptoms**: Physical or emotional reactions
   - **Coping Strategies**: How you dealt with it

### Viewing and Managing Events
- **Home Page**: See recent events and quick stats
- **All Events**: Browse all recorded events with pagination
- **Event Details**: View complete information for any event
- **Edit/Delete**: Modify or remove events as needed

### Analysis
- **Overview**: Total events, average stress levels, recent trends
- **Category Breakdown**: See which types of events are most common
- **Insights**: Get personalized recommendations based on your data
- **Pattern Recognition**: Identify recurring triggers and effective coping strategies

## User Management

### Creating Users
To create additional users for the application:
```bash
python create_user.py
```

### Listing Users
To see all existing users:
```bash
python create_user.py list
```

### User Security
- Only pre-configured users can access the application
- No public registration is available
- Each user's data is completely isolated
- Passwords are securely hashed

## Database

The application uses SQLite for data storage. The database file (`stress_diary.db`) will be created automatically when you first run the app. All your data is stored locally on your machine.

## Security Note

This is a basic implementation for personal use. For production deployment:
- Change the `SECRET_KEY` in `app.py`
- Use a proper database (PostgreSQL, MySQL)
- Implement user authentication
- Use HTTPS
- Add input validation and sanitization

## Customization

### Adding New Categories
Edit the `category` field choices in `app.py`:
```python
category = SelectField('Category', 
                      choices=[('work', 'Work'), ('relationships', 'Relationships'), 
                             ('health', 'Health'), ('financial', 'Financial'),
                             ('family', 'Family'), ('social', 'Social'),
                             ('new_category', 'New Category'),  # Add here
                             ('other', 'Other')])
```

### Styling
Modify `static/css/style.css` to customize the appearance.

## Future Enhancements

Potential features to add:
- User authentication and multiple user support
- Data export (CSV, PDF reports)
- Advanced analytics and charts
- Mobile app version
- Reminder notifications
- Integration with health apps
- Machine learning for pattern detection
- Sharing and collaboration features

## Troubleshooting

**Port already in use**: If port 5000 is busy, modify the last line in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change port number
```

**Database issues**: Delete `stress_diary.db` to reset the database (this will lose all data).

**Dependencies**: Make sure you have Python 3.7+ installed and all requirements are installed.

## Support

This is a personal project for stress management. Feel free to modify and enhance it according to your needs!
