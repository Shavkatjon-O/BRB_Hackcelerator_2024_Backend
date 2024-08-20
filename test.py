import requests

# Create a session to handle cookies and CSRF token
session = requests.Session()

# First, get the CSRF token
response = session.get("https://admin.brb-titans.uz/login/")
csrf_token = response.cookies["csrftoken"]

# Data for signup
signup_data = {
    "email": "shavkatjon@gmail.com",
    "password": "Shovkatbek_1",
    "csrfmiddlewaretoken": csrf_token,
}

# Perform the POST request with CSRF token included
response = session.post("https://admin.brb-titans.uz/api/signup/", data=signup_data)

# Print status code and response content
print(response.status_code)
print(response.text)
print(response.headers)
