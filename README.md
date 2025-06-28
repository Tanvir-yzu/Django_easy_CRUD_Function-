
# Company Management System

A modern Django web application for managing company information with full CRUD (Create, Read, Update, Delete) functionality.

## 🚀 Features

- **Company Management**: Complete CRUD operations for company records
- **Modern UI**: Responsive design with Tailwind CSS and Alpine.js
- **File Upload**: Company logo upload and management
- **Form Validation**: Client and server-side validation
- **Interactive Modals**: View details and confirm deletions
- **Professional Design**: Modern glassmorphism effects and animations

## 📋 Company Information Fields

- Company Name (Required)
- Email Address (Required)
- Phone Number
- Street Address
- City & Country
- Website URL
- Industry
- Employee Count
- Company Description
- Company Logo

## 🛠️ Technology Stack

- **Backend**: Django 4.x
- **Frontend**: HTML5, Tailwind CSS, Alpine.js
- **Database**: SQLite (default)
- **File Storage**: Django's default file handling
- **Icons**: Heroicons (SVG)

## 📁 Project Structure

```
Test/
├── Home/                          # Main Django app
│   ├── templates/                 # HTML templates
│   │   ├── company_list.html      # Company listing page
│   │   ├── company_form.html      # Add/Edit company form
│   │   └── company_confirm_delete.html  # Delete confirmation
│   ├── models.py                  # Company model
│   ├── views.py                   # Class-based views
│   ├── urls.py                    # URL patterns
│   └── admin.py                   # Admin configuration
├── Test/                          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/                         # Uploaded files
├── db.sqlite3                     # Database file
├── manage.py                      # Django management script
└── README.md                      # This file
```

## 🚦 Getting Started

### Prerequisites

- Python 3.8+
- Django 4.x
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd d:\Programming\Softwer_Project\Django_test\Test
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Django** (if not already installed):
   ```bash
   pip install django
   ```

4. **Run database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📖 Usage

### Company Management

1. **View Companies**: Navigate to the home page to see all companies
2. **Add Company**: Click the "Add Company" button and fill in the form
3. **Edit Company**: Click the "Edit" button on any company card
4. **View Details**: Click "View Details" to see complete company information
5. **Delete Company**: Click "Delete" and confirm the action

### Features Overview

- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **File Upload**: Upload company logos with preview functionality
- **Form Validation**: Real-time validation with error messages
- **Confirmation Modals**: Safe deletion with confirmation dialogs
- **Modern Animations**: Smooth transitions and hover effects

## 🎨 UI Components

### Company List Page
- Grid layout of company cards
- Search and filter capabilities
- Action buttons (Add, Edit, View, Delete)
- Responsive design for all screen sizes

### Company Form
- Modern glassmorphism design
- Icon-enhanced form fields
- File upload with preview
- Comprehensive validation
- Responsive grid layout

### Confirmation Dialogs
- Modal-based confirmations
- Clear action buttons
- Company information display

## 🔧 Configuration

### Media Files
The application handles file uploads for company logos. Make sure your `settings.py` includes:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### URL Configuration
The main URLs are configured in `Test/urls.py` and include the Home app URLs.

## 📝 Models

### Company Model
The main model includes fields for:
- Basic information (name, email, phone)
- Location (address, city, country)
- Business details (website, industry, employee count)
- Description and logo

## 🎯 Views

The application uses Django's class-based views:
- `CompanyList`: Display all companies
- `CompanyDetail`: Show individual company details
- `CompanyCreate`: Add new companies
- `CompanyUpdate`: Edit existing companies
- `CompanyDelete`: Remove companies

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure a production database (PostgreSQL recommended)
3. Set up static file serving
4. Configure media file handling
5. Use a production WSGI server (Gunicorn, uWSGI)

## 🤝 Contributing

1. Fork the project
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:
1. Check the Django documentation
2. Review the code comments
3. Test with sample data
4. Ensure all dependencies are installed

## 🔄 Version History

- **v1.0.0**: Initial release with full CRUD functionality
- Modern UI with Tailwind CSS
- File upload capabilities
- Responsive design
- Form validation

---

**Built with ❤️ using Django and modern web technologies**
```

This comprehensive README provides:

✅ **Project Overview**: Clear description of what the application does
✅ **Features List**: All the functionality you've implemented
✅ **Technology Stack**: Technologies used in the project
✅ **Installation Guide**: Step-by-step setup instructions
✅ **Usage Instructions**: How to use each feature
✅ **Project Structure**: File organization explanation
✅ **Configuration Details**: Important settings and setup
✅ **Deployment Notes**: Production considerations
✅ **Professional Formatting**: Clean, readable structure with emojis and code blocks

The README is tailored specifically to your Django company management system and includes all the features we've implemented together!
        