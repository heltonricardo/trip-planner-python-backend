# Trip Planner Python Backend 🌍

This is a backend API built with Python and Flask for managing trips. It allows users to create trips, add important links, activities, and participants. This repository is designed for educational purposes. The frontend will be developed in a separate repository (TODO).

## 🌟 Core Features

- **Trip Management**: Create and manage trips with details like destination and dates.
- **Links**: Attach important links related to each trip.
- **Activities**: Add and view planned activities for a trip.
- **Participants**: Add participants to trips and manage their details.

## 🔧 Complementary Utilities

- **Email Notifications**: Automatically send confirmation emails to the trip owner and participants.
- **Swagger API Documentation**: Available at `/docs`.

## 📡 Endpoints

- `POST /trips`: Create a new trip.
- `GET /trips/{trip_id}`: Retrieve details of a specific trip.
- `GET /trips/{trip_id}/confirm`: Confirm a trip.
- `POST /trips/{trip_id}/links`: Add a new link to a trip.
- `GET /trips/{trip_id}/links`: List all links for a trip.
- `POST /trips/{trip_id}/participants`: Add a participant to a trip.
- `GET /trips/{trip_id}/participants`: List all participants for a trip.
- `POST /trips/{trip_id}/activities`: Add a new activity to a trip.
- `GET /trips/{trip_id}/activities`: List all activities for a trip.
- `GET /participants/{participant_id}/confirm`: Confirm participation of a specific participant.

## 🛠️ Installation and Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/heltonricardo/trip-planner-python-backend.git
   cd trip-planner-python-backend
   ```

2. **Create and activate the virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create the SQLite database**:

   - Initialize the database with the schema by creating the file `init/schema.sql` in the root of the project. Make sure to also create a `storage.db` file.

5. **Generate email credentials for Nodemailer**:

   - Run the following script to generate email credentials:
     ```bash
     python utils/create_email.py
     ```
   - This will generate credentials using [Nodemailer](https://api.nodemailer.com/user).
   - Replace the generated credentials in `src/driver/email_sender.py`.

6. **Run the application**:

   ```bash
   python run.py
   ```

7. **Access Swagger Documentation**:
   - Visit [http://localhost:3000/docs](http://localhost:3000/docs) for the API documentation.
