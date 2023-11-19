This is a simple web application for managing appointments. Users can add new appointments, view a list of appointments, edit existing appointments, and delete appointments.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Editing Appointments](#editing-appointments)
- [Deleting Appointments](#deleting-appointments)
- [Acknowledgements](#acknowledgements)

## Features

- Add new appointments with details such as first name, last name, location, and date & time.
- View a list of all appointments with the ability to edit or delete each appointment.
- Edit existing appointments to update details.
- Delete appointments to remove them from the system.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- (Add any additional prerequisites)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/appointment-management.git


2. Navigate to the project directory:

cd appointment-management

3. Install dependencies:

pip install -r requirements.txt

## Usage

1. Run the Flask application:

    python app.py

2. Open your browser and navigate to http://127.0.0.1:5000. or (ctrl+click) on the terminal to access the link


## Adding Appointments

To add an appointment:

    1. Fill the fields designated to given columns
    2. Click on button "Add Appointment" to add the appointment.



## Editing Appointments

To edit an existing appointment:

    1. Click on the "Edit" button next to the appointment you want to edit.
    2. Modify the details as needed.
    3. Click the "Save Changes" button to apply the changes.

    Note - Editing Appointment only works for First Name, Last Name, Location. Due to some technical error Date and Time cannot be edited and Edit Appointment can't handel editing of multiple appointments. (Sorry for the inconvience. Tried my best to solve it but it didnt work)


## Deleting Appointments

To delete an appointment:

    1. Click on the "Delete" button next to the appointment you want to delete.
    2. Confirm the deletion when prompted.


## Acknowledgements

Libraries used = Flask 2.0.2