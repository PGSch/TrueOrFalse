# server.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import base64
import json
import random

# Define a simple handler class to respond to /login and /game requests
class RequestHandler(BaseHTTPRequestHandler):
    # Set username and password for login
    USERNAME = "admin"
    PASSWORD = "123"
    SESSION_ID = "12345"

    # Load questions and answers from a JSON file
    with open("questions.json", "r") as f:
        QUESTIONS = json.load(f)

    # Define the response to a GET request
    def do_GET(self):
        # Handle the /login request
        if self.path == "/login":
            # Extract the Authorization header from the request
            auth_header = self.headers.get("Authorization")

            if auth_header:
                # Decode the base64-encoded credentials
                auth_type, encoded_credentials = auth_header.split(" ")
                decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
                username, password = decoded_credentials.split(":")

                # Check if the username and password match
                if username == self.USERNAME and password == self.PASSWORD:
                    # Send a 200 OK response
                    self.send_response(200)
                    # Set the session cookie in the header
                    self.send_header("Set-Cookie", f"sessionid={self.SESSION_ID}; Path=/; HttpOnly")
                    self.send_header("Content-Type", "text/plain")
                    self.end_headers()
                    # Send a successful login message with a newline at the end
                    self.wfile.write(b"Login successful!\n")
                else:
                    # Send a 401 Unauthorized response
                    self.send_response(401)
                    self.send_header("Content-Type", "text/plain")
                    self.end_headers()
                    self.wfile.write(b"Unauthorized: Invalid credentials\n")
            else:
                # Send a 401 Unauthorized response if no credentials are provided
                self.send_response(401)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Unauthorized: Missing credentials\n")

        # Handle the /game request
        elif self.path == "/game":
            # Check if the session cookie is present
            cookie_header = self.headers.get("Cookie")

            if cookie_header and f"sessionid={self.SESSION_ID}" in cookie_header:
                # Randomly select a question and answer from the loaded JSON data
                selected_question = random.choice(self.QUESTIONS)

                # Prepare the response as a JSON object
                response = {
                    "question": selected_question["question"],
                    "answer": selected_question["answer"]
                }

                # Send the selected question and answer as JSON
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write((json.dumps(response) + "\n").encode("utf-8"))
            else:
                # Send a 403 Forbidden response if the session is invalid
                self.send_response(403)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Forbidden: Invalid session or no session cookie provided\n")

        else:
            # Send a 404 Not Found response for any other path
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found\n")

    def log_message(self, format, *args):
        # Suppress log messages to keep the output clean
        return

# Define the server address and handler
server_address = ("127.0.0.1", 8000)
httpd = HTTPServer(server_address, RequestHandler)

print("Server running on http://127.0.0.1:8000")
httpd.serve_forever()
# server.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import base64
import json

# Define a simple handler class to respond to /login and /game requests
class RequestHandler(BaseHTTPRequestHandler):
    # Set username and password for login
    USERNAME = "admin"
    PASSWORD = "123"
    SESSION_ID = "12345"

    # Define the response to a GET request
    def do_GET(self):
        # Handle the /login request
        if self.path == "/login":
            # Extract the Authorization header from the request
            auth_header = self.headers.get("Authorization")

            if auth_header:
                # Decode the base64-encoded credentials
                auth_type, encoded_credentials = auth_header.split(" ")
                decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
                username, password = decoded_credentials.split(":")

                # Check if the username and password match
                if username == self.USERNAME and password == self.PASSWORD:
                    # Send a 200 OK response
                    self.send_response(200)
                    # Set the session cookie in the header
                    self.send_header("Set-Cookie", f"sessionid={self.SESSION_ID}; Path=/; HttpOnly")
                    self.send_header("Content-Type", "text/plain")
                    self.end_headers()
                    # Send a successful login message with a newline at the end
                    self.wfile.write(b"Login successful!\n")
                else:
                    # Send a 401 Unauthorized response
                    self.send_response(401)
                    self.send_header("Content-Type", "text/plain")
                    self.end_headers()
                    self.wfile.write(b"Unauthorized: Invalid credentials\n")
            else:
                # Send a 401 Unauthorized response if no credentials are provided
                self.send_response(401)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Unauthorized: Missing credentials\n")

        # Handle the /game request
        elif self.path == "/game":
            # Check if the session cookie is present
            cookie_header = self.headers.get("Cookie")

            if cookie_header and f"sessionid={self.SESSION_ID}" in cookie_header:
                # Send a 200 OK response
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                
                # Prepare a question and answer response
                response = {
                    "question": "What is the capital of France?",
                    "answer": "Paris"
                }
                # Send the question and answer as JSON
                self.wfile.write((json.dumps(response) + "\n").encode("utf-8"))
            else:
                # Send a 403 Forbidden response if the session is invalid
                self.send_response(403)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Forbidden: Invalid session or no session cookie provided\n")

        else:
            # Send a 404 Not Found response for any other path
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found\n")

    def log_message(self, format, *args):
        # Suppress log messages to keep the output clean
        return

# Define the server address and handler
server_address = ("127.0.0.1", 8000)
httpd = HTTPServer(server_address, RequestHandler)

print("Server running on http://127.0.0.1:8000")
httpd.serve_forever()

