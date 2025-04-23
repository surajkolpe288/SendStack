# SendStack
SendStack is a simple and efficient Python-based bulk email automation tool that helps you send personalized job application emails to multiple HRs or recruiters in one go. Just feed in your email template, contact list, and resume — SendStack handles the rest!

# 🚀 Features

- 🔁 Bulk email sending (10–20+ recipients at a time)
- 🧠 Auto-personalization using a flexible email template
- 📎 Resume attachment included with each mail
- 🛡️ Secure login using SMTP over SSL
- 🧾 Logging of all sent emails with timestamp
- 🧹 Skips incomplete or malformed contact rows automatically

# 🛠 Setup & Installation

1. Clone the Repository
2. Install Python (if not installed)
3. Add Your Email Credentials(Create a file named config.py in the root directory)
   🔐 Important: Use an App Password if you are using Gmail.
   You can enable 2FA and generate an app password from Google Account Settings.
4. Prepare contacts.csv
5. Write email_template.txt
6. Add attachements (If needed)

Example Directory Structure:
sendstack/
│
├── main.py
├── config.py
├── resume.pdf
├── email_template.txt
├── contacts.csv
├── sent_log.csv  ← Generated after running the script

License
This project is open-source and available under the MIT License.
