# app.py

from flask import Flask, render_template, request, redirect, flash, url_for
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


appointments_data = []

@app.route('/')
def index():
    return render_template('index.html', appointments=appointments_data)

# Add appointment
@app.route('/add_appointment_page/')
def add_appointment_page():
    return render_template('add_appointment.html')
    
@app.route('/add_appointment', methods=['POST'])
def add_appointment():
    if request.method == 'POST':
        print('Received a POST request for adding an appointment.')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        location = request.form.get('location')
        appointment_time = request.form.get('appointment_time')

        print(f'Form data: {first_name}, {last_name}, {location}, {appointment_time}')

        new_appointment = {
            'id': len(appointments_data) + 1,
            'first_name': first_name,
            'last_name': last_name,
            'location': location,
            'appointments': [appointment_time],
        }

        appointments_data.append(new_appointment)

        flash('Appointment added successfully!', 'success')
        return redirect(url_for('add_appointment_page'))
    else:
        flash('Invalid request method for adding appointment', 'danger')
        return redirect(url_for('add_appointment_page'))


# View appointment

@app.route('/view_appointment')
def view_appointments():
    return render_template('view_appointment.html', appointments=appointments_data)


# Edit appointment

@app.route('/edit_appointments')
def edit_appointments():
    return render_template('edit_appointment.html', appointments=appointments_data)

@app.route('/edit_appointment', methods=['GET','POST'])
def edit_appointment():
    if request.method == 'POST':
        edited_appointment_id = request.form.get('edited_appointment_id')
        edited_first_name = request.form.get('edited_first_name_' + str(edited_appointment_id))
        edited_last_name = request.form.get('edited_last_name_' + str(edited_appointment_id))
        edited_location = request.form.get('edited_location_' + str(edited_appointment_id))
        edited_appointment_time = request.form.get('edited_appointment_time_' + str(edited_appointment_id))

        for appointment in appointments_data:
            if str(appointment['id']) == edited_appointment_id:
                appointment['first_name'] = edited_first_name
                appointment['last_name'] = edited_last_name
                appointment['location'] = edited_location
                appointment['appointments'][0] = edited_appointment_time

        flash('Appointment edited successfully!', 'success')

    return redirect(url_for('edit_appointments'))

# Delete appointment

@app.route('/delete_appointments', methods=['GET', 'POST'])
def delete_appointments():
    if request.method == 'POST':
        appointment_id = request.form.get('appointment_id')
        delete_appointment(appointment_id)
        flash('Appointment deleted successfully!', 'success')

    return render_template('delete_appointment.html', appointments=appointments_data)

# Function to delete an appointment
def delete_appointment(appointment_id):
    appointment_to_delete = next((a for a in appointments_data if a['id'] == int(appointment_id)), None)
    if appointment_to_delete:
        appointments_data.remove(appointment_to_delete)

if __name__ == '__main__':
    app.run(debug=True)
