import csv
import smtplib
from email.message import EmailMessage
from datetime import datetime
from config import EMAIL_ADDRESS, EMAIL_PASSWORD


def load_template():
    with open("email_template.txt", "r", encoding="utf-8") as file:
        return file.read()


def send_email(to_email, subject, body, resume_path):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg.set_content(body)

    with open(resume_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="Resume.pdf")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


def log_sent_email(name, email, company):
    with open("sent_log.csv", "a", newline='', encoding="utf-8") as log_file:
        writer = csv.writer(log_file)
        writer.writerow([datetime.now(), name, email, company])


def main():
    template = load_template()
    resume_path = "resume.pdf"

    # 🧾 Initialize log file
    with open("sent_log.csv", "w", newline='', encoding="utf-8") as log_file:
        writer = csv.writer(log_file)
        writer.writerow(["Timestamp", "Name", "Email", "Company"])

    with open("hr_contacts.csv", newline='', encoding="utf-8") as file:
        # Explicitly set delimiter to comma (',')
        reader = csv.DictReader(file, delimiter=',')  # Using ',' as delimiter for standard CSV

        # ✅ Fix 1: Clean header names
        if reader.fieldnames:
            reader.fieldnames = [field.strip().replace('\ufeff', '').replace('"', '') for field in reader.fieldnames]

        print("Cleaned Headers:", reader.fieldnames)  # Optional debug

        for row in reader:
            # ✅ Fix 2: Clean up the row values (strip spaces, tabs, etc.)
            row = {key: value.strip() if value else None for key, value in row.items()}

            # ✅ Skip rows with missing essential fields
            if not all([row.get("name"), row.get("email"), row.get("company"), row.get("job_role")]):
                print(f"⚠️ Skipping row due to missing data: {row}")
                continue

            try:
                email_body = template.format(
                    name=row["name"],
                    company=row["company"],
                    job_role=row["job_role"],
                    custom_note=row.get("custom_note", "")
                )

                send_email(
                    to_email=row["email"],
                    subject=f"Application for {row['job_role']} at {row['company']}",
                    body=email_body,
                    resume_path=resume_path
                )

                log_sent_email(row["name"], row["email"], row["company"])
                print(f"✅ Email sent to {row['name']} at {row['company']}")

            except Exception as e:
                print(f"❌ Failed to send email to {row.get('name', 'Unknown')}: {e}")


if __name__ == "__main__":
    main()
