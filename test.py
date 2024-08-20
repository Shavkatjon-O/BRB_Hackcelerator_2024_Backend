import requests

signup_data = {
    "email": "shavkatjon@gmail.com",
    "password": "Shovkatbek_1",
}

# Perform the POST request with CSRF token included
response = requests.post("https://admin.brb-titans.uz/api/v1/signup/", data=signup_data)

# Print status code and response content
print(response.status_code)
print(response.text)
print(response.headers)
