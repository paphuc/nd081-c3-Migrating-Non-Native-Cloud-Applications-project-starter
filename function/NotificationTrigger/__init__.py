import logging
import azure.functions as func
import psycopg2
from datetime import datetime
import time
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

def main(msg: func.ServiceBusMessage):
    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s',notification_id)

    # Get connection to database
    POSTGRES_URL = "pr3db.postgres.database.azure.com"
    POSTGRES_USER = "phucpa1@pr3db"
    POSTGRES_PW = "12345678abC"
    POSTGRES_DB = "techconfdb"
    connection = psycopg2.connect(host = POSTGRES_URL, dbname = POSTGRES_DB, user = POSTGRES_USER, password = POSTGRES_PW)
    
    try:
        curr = connection.cursor()

        # Get notification message and subject from database using the notification_id
        curr.execute("SELECT message, subject FROM notification WHERE id = %s;",(notification_id,))
        message, subject = curr.fetchone()
        
        # Get attendees email and name
        curr.execute("SELECT email, first_name, last_name FROM attendee;")
        attendees = curr.fetchall()
        
        # Loop through each attendee and send an email with a personalized subject
        success = 0
        for (first_name, last_name, email) in attendees:
            try:
                time.sleep(15)
                success += 1
            except Exception as e:
                logging.error("Error when sendding a notification to email %s", attendees[0])
        
        # Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        notification_date = datetime.utcnow()
        notification_info = 'Notified {} attendees'.format(success)
        
        # Update the notification table by setting the completed date and updating the status with the total number of attendees notified
        curr.execute("UPDATE notification SET status = %s, completed_date = %s WHERE id = %s;",(notification_info, notification_date, notification_id))
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        if connection:
            curr.close()
            connection.close()
