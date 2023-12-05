This is a simple web application for for Fitness Trainers for managing appointments. Users can add new appointments, view a list of appointments, edit existing appointments, and delete appointments.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [URL Usage](#url-usage)
- [Adding Appointments](#adding-appointments)
- [Viewing Appointments](#viewing-appointments)
- [Editing Appointments](#editing-appointments)
- [Deleting Appointments](#deleting-appointments)
- [Screenshots](#screenshots)
- [Acknowledgements](#acknowledgements)

## Features

- Add new appointments with details such as first name, last name, location, and date & time.
- View a list of all appointments with the ability to edit or delete each appointment.
- Edit existing appointments to update details.
- Delete appointments to remove them from the system.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Flask 3.0.0
- VS Code or any other editor

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ADITYONALDO/Fitness-Trainer-Appointment-Scheduling.git


2. Navigate to the project directory:

    cd Fitness-Trainer-Appointment-Scheduling

3. Install dependencies:

    pip install -r requirements.txt




## Usage

1. Run the Flask application:

    python app.py

2. Open your browser and navigate to http://127.0.0.1:5000. or (ctrl+click) on the link shown in the terminal.



## URL Usage

For ease of navigation throught the app, edit the URL's as given below:


http://127.0.0.1:5000/#   (To return to home page)

http://127.0.0.1:5000/add_appointment_page  (To move to Add Appointment Page)

http://127.0.0.1:5000/view_appointment      (To move to View Appointment Page)

http://127.0.0.1:5000/edit_appointments     (To move to Edit Appointment Page)

http://127.0.0.1:5000/delete_appointments   (To move to Delete Appointment Page)



## Adding Appointments

To add an appointment:

    1. Fill the fields designated to given columns
    2. Click on button "Add Appointment" to add the appointment.


## Viewing Appointments

To view the appointsments:

    1. Navigate to home page i.e. http://127.0.0.1:5000/#
    2. Click on the View Appointment section on top right side of the page to view the appointments.


## Editing Appointments

To edit an existing appointment:

    1. Navigate to Edit Appointment page.
    2. Click on the "Edit" button next to the appointment you want to edit.
    3. Modify the details as needed.
    4. Click the "Save Changes" button to apply the changes.


    Developers Note - edit one appointment at a time and press 'Save Changes' button to save the data. 
                      (Example - Edit appointment 1 and press Save Changes button to save, then edit appointment 2 and so on)
             


## Deleting Appointments

To delete an appointment:

    1. Click on the "Delete" button next to the appointment you want to delete.
    2. Confirm the deletion when prompted.




## Screenshots

Home Page - 
![image](https://github.com/ADITYONALDO/Fitness-Trainer-Appointment-Scheduling/assets/91738311/356c61a5-380f-4d45-b357-d610e465f791)


Add Appointment Page - 
![image](https://github.com/ADITYONALDO/Fitness-Trainer-Appointment-Scheduling/assets/91738311/f9570d63-8187-44fb-ab60-36b392877add)

![image](https://github.com/ADITYONALDO/Fitness-Trainer-Appointment-Scheduling/assets/91738311/3d09867b-48be-4366-a895-3f5ca5a95e2c)  (Displaying message after appointment is added)


View Appointment Page - 
![image](https://github.com/ADITYONALDO/Fitness-Trainer-Appointment-Scheduling/assets/91738311/840b5639-2d23-4f9e-b854-393fb6e0427b)


Edit Appointment Page - 
![image](https://github.com/ADITYONALDO/Fitness-Trainer-Appointment-Scheduling/assets/91738311/819c781a-6346-479d-9b67-b46966f5b944)

![image](https://github.com/ADITYONALDO/Fitness-Trainer-Appointment-Scheduling/assets/91738311/fc174c6a-0870-4b05-a42e-c3bd66206281)  (Editing appointment after pressing 'Edit' button)

![image](https://github.com/ADITYONALDO/Fitness-Trainer-Appointment-Scheduling/assets/91738311/e7f55b9e-19f7-45d4-a05e-7c8a5dd6c0c1)  (Showing message when edited appointment is edited)



Delete Appointment Page - 
![image](https://github.com/ADITYONALDO/Fitness-Trainer-Appointment-Scheduling/assets/91738311/06794453-fd86-442a-b62f-49f183b06b09)  (Showing new data after changes are made in edit appointment)

![image](https://github.com/ADITYONALDO/Fitness-Trainer-Appointment-Scheduling/assets/91738311/9f1e31ae-71bf-49c7-a00b-f3ea700fef62)  (Showing a confirmation step before deleting an appointment)

![image](https://github.com/ADITYONALDO/Fitness-Trainer-Appointment-Scheduling/assets/91738311/3cb5bf98-c3bb-4d90-98dd-cd1bb107ab61)  (Showing message when an appointment is deleted)




## Acknowledgements

Libraries used = Flask 3.0.0
