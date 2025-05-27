from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

#connect to database
mydb = {
  'host': "172.28.110.89",
  'user': "data",
  'password': "Idrive",
  'database': "Hoytorptreffet"
}
def db_connection():
    try:
        connection = mysql.connector.connect(**mydb)
        return connection
    except Error as e:
        print(f"Error connecting to mariadb: {e}")
        return None

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/registrer.html')
def registrer():
    return render_template("registrer.html")

@app.route('/submit_reg', methods=['POST'])
def submit_reg():
    try:
        #tar input fra form. 
        first_name = request.form['fornavn']
        last_name = request.form['etternavn']
        email = request.form['email']
        phone_number = request.form['tlf']
        address = request.form['adresse']
        city = request.form['by']
        country = request.form['land']

        vehicle_type = request.form['kjoretoy']
        make = request.form['merke']
        model = request.form['modell']
        year = request.form['aar']
        registration_number = request.form['reg']
    
        event_year = request.form['eventYear'] 
        comments = request.form['comments'] 
    #validate reqired fields
        if not all([first_name, last_name, email, event_year]):
            return "fyll ut fornavn, etternavn, email og event år", 400
    
    
        connection = db_connection()
        cursor = connection.cursor()
        
        check_participant_query = "SELECT ParticipantID FROM Participants WHERE Email = %s"
        cursor.execute(check_participant_query, (email,))
        participant_result = cursor.fetchone()
        
        if participant_result:
            participant_id = participant_result[0]
        else:
        #insert deltaker data
            participant_query = """
        INSERT INTO Participants (FirstName, LastName, Email, PhoneNumber, Address, City, Country)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        
            participant_data = (first_name, last_name, email, phone_number, address, city, country)
            cursor.execute(participant_query, participant_data)
            participant_id = cursor.lastrowid
        
        
    # insert kjøretøy data
        vehicle_query = """
    INSERT INTO Vehicles (ParticipantID, VehicleType, Make, Model, Year, RegistrationNumber)
    VALUES (%s, %s, %s, %s, %s, %s)
        """
        vehicle_data = (participant_id, vehicle_type, make, model, year, registration_number)
        cursor.execute(vehicle_query, vehicle_data)
        
        # participation record
        participation_record_query = """
    INSERT INTO ParticipationRecords (ParticipantID, EventYear, Comments)
    VALUES (%s, %s, %s)
        """
        participation_record_data = (participant_id, event_year, comments)
        cursor.execute(participation_record_query, participation_record_data)
        
        # commits submit data to database
        connection.commit()
        
        # lukke cursor og connection
        cursor.close()
        connection.close()
        
        return redirect(url_for('registration_success'))
    
    except Error as e:
        if connection:
            connection.rollback()
        return f"An error occured: {str(e)}", 500
    
@app.route('/success')
def registration_success():
    return "Takk for at du blir med på Høytorptreffet!!"        
        
#if __name__ == '__main__':
    #app.run(debug=True)
