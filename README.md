# FileSharing
## Send file anywhere in the world.

<p>
This webapp is for sending a file, anywhere in the World. Sender sends a file through this webapp which can be downloaded by the receiver with a PIN that will be generated by the server from anywhere in the World.</p>

---

[My App URL](https://filesharingbd.pythonanywhere.com/)


---

# Environment Setup (Windows)
## Create Virtual Environment
`python -m venv env`

## Activate Virtual Environment
`env\Scripts\activate`

## Deactivate Virtual Environment
`env\Scripts\deactivate.bat`

---
# Install Project Dependency

`pip install -r requirements.txt`

# Collect Static Files
`(env) FileSharing> python manage.py collectstatic`

# Run Project
`(env) FileSharing> python manage.py runserver`


