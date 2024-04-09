Getting Started
Prerequisites
Before setting up DataForge, ensure you have the following installed:

Python 3.x
Node.js and npm
These are essential for running the backend and frontend parts of the project.

Installation
1. Clone the Repository
Start by cloning the DataForge repository to your local machine:

bash
Copy code
git clone https://github.com/HardtoHave/DataForge.git
cd DataForge
2. Set Up the Backend
Navigate to the backend directory and install the required Python dependencies:

bash
Copy code
cd Backend
pip install -r requirements.txt
Initialize the database and start the backend server (assuming a Django backend for demonstration purposes):

bash
Copy code
python manage.py migrate
python manage.py runserver
3. Set Up the Frontend
In a new terminal, navigate to the frontend directory from the project root:

bash
Copy code
cd Frontend
npm install
Start the frontend development server:

bash
Copy code
npm start
The frontend should now be accessible at http://localhost:8000.

Usage
With both the backend and frontend running, navigate to http://localhost:8000 in your web browser to view and interact with the DataForge application.
