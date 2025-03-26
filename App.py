
import json
import os
from dotenv import load_dotenv
import requests

# Charger les variables d'environnement du fichier .env
load_dotenv()

# Récupérer les valeurs
glpi_url = os.getenv("GLPI_URL")
username = os.getenv("GLPI_USERNAME")
password = os.getenv("GLPI_PASSWORD")
app_token = os.getenv("GLPI_APP_TOKEN")



# Headers for the request
headers = {
    "Content-Type": "application/json",  # Ensures proper request format
    "App-Token": app_token,
}

# Function to get the Session-Token (and set session write mode)
def get_session_token():
    url = f"{glpi_url}/initSession?session_write=true"  # Passing session_write=true
    payload = {
        "login": username,
        "password": password,
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        session_token = response.json().get('session_token')
        if session_token:
            print(f"Session-Token: {session_token}")
            return session_token
        else:
            print("Error: No session token found in the response.")
            return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to create a user (requester)
def create_user(session_token, username, firstname, lastname, email):
    url = f"{glpi_url}/User"
    headers.update({"Session-Token": session_token})
    
    # User data wrapped in an array (as required by the GLPI API)
    user_data = {
        "input": {
            "name": username,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "authtoken": "unique-auth-token",  # Unique authentication token for the user
            "status": 1  # Active status
        }
    }

    response = requests.post(url, headers=headers, json=user_data)  # Use json instead of data to auto-encode to JSON

    if response.status_code == 201:  # Check for 201 status code (created)
        user_id = response.json().get("id")
        if user_id:
            print(f"User created successfully! ID: {user_id}")
            return user_id
        else:
            print("Error: User ID not returned.")
            return None
    else:
        print(f"Error creating user: {response.status_code} - {response.text}")
        return None

# Function to create a ticket
def create_ticket(session_token, user_id, title, description):
    url = f"{glpi_url}/Ticket"
    headers.update({"Session-Token": session_token})
    
    # Ticket data
    ticket_data = {
        "input": {
            "name": title,  # Subject of the ticket
            "content": description,  # Description of the ticket
            "status": 1,  # New ticket status
            "requester": user_id,  # User ID of the requester
            "urgency": 3,  # Urgency (1: low, 3: high)
        }
    }
    
    response = requests.post(url, headers=headers, json=ticket_data)  # Use json instead of data to auto-encode to JSON
    
    if response.status_code == 201:
        ticket_id = response.json().get("id")
        if ticket_id:
            print(f"Ticket created successfully! ID: {ticket_id}")
            return ticket_id
        else:
            print("Error: Ticket ID not returned.")
            return None
    else:
        print(f"Error creating ticket: {response.status_code} - {response.text}")
        return None

# Main function
def main():
    session_token = get_session_token()
    
    if session_token:
        print("Session token obtained successfully!")
        
        # Create a user
        username = "dadasdas"
        firstname = "dasdasd"
        lastname = "dasdasd"
        email = "dasdasd@example.com"
        
        user_id = create_user(session_token, username, firstname, lastname, email)
        
        if user_id:
            # Create a ticket for the user
            ticket_title = "Computer issue"
            ticket_description = "The computer won't start."
            create_ticket(session_token, user_id, ticket_title, ticket_description)
    else:
        print("Failed to obtain session token.")

if __name__ == "__main__":
    main()
