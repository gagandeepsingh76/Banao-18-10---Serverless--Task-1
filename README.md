# Healthcare System - Django Application

A Django web application that provides user authentication for two types of users: **Patients** and **Doctors**. Users can sign up, login, and access their respective dashboards with all their profile information displayed.

## Features

### User Authentication
- **Two User Types**: Patient and Doctor
- **Secure Registration**: Password hashing using Django's built-in authentication
- **Profile Management**: Complete user profile with image upload and address information
- **Role-based Access**: Separate dashboards for patients and doctors

### Signup Form Fields
- First Name
- Last Name  
- User Type (Patient/Doctor)
- Username
- Email ID
- Password & Confirm Password (with validation)
- Profile Picture (Image upload)
- Address Information:
  - Address Line 1
  - City
  - State
  - Pincode

### Security Features
- Password confirmation validation (client and server-side)
- Secure password storage using Django's built-in hashing
- CSRF protection
- Form validation and error handling

## Project Structure

```
healthcare_system/
├── healthcare_system/          # Main project directory
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── accounts/                   # User authentication app
│   ├── models.py              # Custom User model
│   ├── forms.py               # Signup and login forms
│   ├── views.py               # Class-based views
│   ├── urls.py                # App URL configuration
│   ├── admin.py               # Admin configuration
│   └── templates/accounts/    # HTML templates
│       ├── base.html
│       ├── signup.html
│       ├── login.html
│       ├── patient_dashboard.html
│       └── doctor_dashboard.html
├── media/                     # User uploaded files
├── manage.py
└── README.md
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download the project**
   ```bash
   # If you have the project files, navigate to the project directory
   cd healthcare_system
   ```

2. **Install required packages**
   ```bash
   pip install django Pillow
   ```

3. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### User Registration
1. Navigate to the signup page
2. Fill in all required fields
3. Choose user type (Patient or Doctor)
4. Upload a profile picture (optional)
5. Enter address information
6. Submit the form

### User Login
1. Go to the login page
2. Enter username and password
3. Upon successful login:
   - **Patients** are redirected to the Patient Dashboard
   - **Doctors** are redirected to the Doctor Dashboard

### Dashboards
- **Patient Dashboard**: Displays all user information including profile picture and address
- **Doctor Dashboard**: Displays all user information with doctor-specific styling

## Technical Details

### Database
- Uses SQLite by default (can be configured for other databases)
- Custom User model extends Django's AbstractUser
- All user data including images and addresses are stored in the database

### Media Files
- Profile pictures are stored in the `media/profile_pictures/` directory
- Media files are served during development
- For production, configure proper media file serving

### Security
- Passwords are hashed using Django's built-in authentication
- CSRF protection enabled
- Form validation on both client and server side
- Role-based access control for dashboards

## Configuration

### Required Settings
The following settings are already configured in `settings.py`:

```python
# Custom User Model
AUTH_USER_MODEL = 'accounts.User'

# Media files (for user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Database Configuration
The project uses SQLite by default. To use a different database, update the `DATABASES` setting in `settings.py`.

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
```

### Applying Migrations
```bash
python manage.py migrate
```

## Production Deployment

For production deployment, consider the following:

1. **Security Settings**:
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Use environment variables for `SECRET_KEY`

2. **Database**:
   - Use PostgreSQL or MySQL for production
   - Configure proper database settings

3. **Media Files**:
   - Use cloud storage (AWS S3, etc.) for media files
   - Configure proper media file serving

4. **Static Files**:
   - Run `python manage.py collectstatic`
   - Configure static file serving

## Troubleshooting

### Common Issues

1. **Pillow Installation Error**:
   - Make sure Pillow is installed: `pip install Pillow`

2. **Migration Errors**:
   - Delete migration files and recreate: `python manage.py makemigrations --empty accounts`

3. **Media Files Not Loading**:
   - Ensure `MEDIA_URL` and `MEDIA_ROOT` are properly configured
   - Check that media files are in the correct directory

## Support

For issues or questions, please check the Django documentation or create an issue in the project repository.

## License

This project is open source and available under the MIT License.


<img width="1365" height="632" alt="Screenshot 2025-12-02 163108" src="https://github.com/user-attachments/assets/1dc5a75b-9e1d-4644-8f3c-71219729163b" />

<img width="1365" height="636" alt="Screenshot 2025-12-02 163124" src="https://github.com/user-attachments/assets/a4993fd6-6cdd-44e0-812a-f3537df1c323" />

<img width="1365" height="631" alt="Screenshot 2025-12-02 163232" src="https://github.com/user-attachments/assets/7b39a184-8735-4ff3-9f9e-5e5705ea4e53" />




