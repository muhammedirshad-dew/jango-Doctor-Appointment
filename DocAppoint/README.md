# 🩺 ClinicLink - Doctor Appointment System

**ClinicLink** is a web-based application that helps patients easily book appointments with doctors in a simple and efficient way.

---

## 🚀 Features

- 🏥 View departments and their details  
- 👨‍⚕️ View the list of available doctors  
- 📅 Book an appointment easily using the booking form  
- 📍 Contact page with an embedded location map  

---

## 🛠️ Technologies Used

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite3  

---

## ⚙️ Setup and Installation

Follow the steps below to run this project on your local machine:

### 1. Clone the Repository
`bash
git clone <your-repository-url>
cd DocAppoint
`

### 2. Create and Activate Virtual Environment (Windows)
`bash
python -m venv env
.\env\Scripts\activate
`

### 3. Install Dependencies
`bash
pip install -r requirements.txt
`

### 4. Apply Database Migrations
`bash
python manage.py migrate
`

### 5. Run the Development Server
`bash
python manage.py runserver
`
Now open your browser and go to 👉 `http://127.0.0.1:8000/` to view the application.

## 💡 Usage
Once you open the application:

- The **Home Page** displays departments and available doctors.
- You can visit the **Booking Page** to schedule an appointment with your preferred doctor.
- The **Contact Page** shows the hospital’s location on a map and contact details.