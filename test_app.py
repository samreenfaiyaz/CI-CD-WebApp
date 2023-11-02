import requests
import json  # Add this import to work with JSON responses

def test_hello_world():
    response = requests.get('http://127.0.0.1:8000')
    assert response.status_code == 200

    # Decode the JSON response
    data = json.loads(response.text)
    
    # Check for the presence of "Hello World!" in the "message" key
    assert 'Hello, World!' in data['message']
