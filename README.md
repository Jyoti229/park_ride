# Park & Ride Management System

A comprehensive web application built with **Django** and **Django REST Framework (DRF)** to manage parking slots, ride reservations, and pricing. This project provides a clean API, user authentication, and a responsive dashboard for easy management of parking and ride services.

---

## Project Structure

```
park_ride/
│
├── parking/              # Parking slots and reservations app
├── rides/                # Ride booking and management app
├── pricing/              # Pricing plans and rules
├── park_ride/            # Project configuration (settings, urls)
├── templates/            # HTML templates for the web app
├── static/               # Static files (CSS, JS, images)
├── manage.py             # Django project manager
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## API Endpoints

- **Parking Slots:** `/api/parking-slots/`
- **Reservations:** `/api/parking-reservations/`
- **Rides:** `/api/rides/`
- **Pricing:** `/api/pricing/`

---

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/park_ride.git
   ```

2. **Navigate into the project directory:**
   ```bash
   cd park_ride
   ```

3. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the project in the browser:**
   ```
   http://127.0.0.1:8000/
   ```

---

## Features

- Manage parking slots and availability.
- Create and track parking reservations.
- Book rides and manage ride schedules.
- Dynamic pricing system with easy updates.
- RESTful API endpoints for integration.
- User authentication (login/logout, profiles).
- Admin dashboard for full control.

---

## Future Enhancements

- Add payment gateway integration (e.g., Stripe, Razorpay).
- Real-time parking slot availability using WebSockets.
- Mobile-friendly UI and PWA support.
- Vehicle tracking with GPS integration.
- Role-based access control (Admin, User).
- Email & SMS notifications for bookings.

---

## Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Database:** SQLite (can switch to PostgreSQL/MySQL)
- **Frontend:** HTML, CSS, Bootstrap
- **Authentication:** Django Auth
- **Tools:** Git, VS Code

---

##  Contribution

Contributions are welcome! Please open an issue or submit a pull request.

---

##  License

This project is licensed under the MIT License.

---

## 👤 Author

**Your Name**  
- GitHub: [Jyoti229](https://github.com/Jyoti229)
- LinkedIn: [jyoti-ai-maestro](https://linkedin.com/in/jyoti-ai-maestro/)
