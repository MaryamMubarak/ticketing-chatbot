import requests

# Function to simulate chatbot ticket creation
def create_ticket(issue_description):
    # Example API endpoint for a ticketing system (replace with your system's endpoint)
    ticketing_system_url = "https://yourticketingsystem.com/api/create_ticket"
    
    # Data to send in POST request
    data = {
        "issue": issue_description,
        "priority": "high",
        "status": "open",
        "assigned_to": "support_team",
    }
    
    # Make the request to create a ticket
    response = requests.post(ticketing_system_url, json=data)
    
    if response.status_code == 200:
        print(f"Ticket created successfully: {response.json()}")
    else:
        print(f"Failed to create ticket: {response.status_code}")

# Simulate receiving an issue
