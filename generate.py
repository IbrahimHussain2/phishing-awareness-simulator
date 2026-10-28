import csv

# The base URL of our local tracking server (started later)
BASE_URL = "http://localhost:8000/click"

# Load the email template
with open("templates/it_password_notice.txt") as f:
    template = f.read()

# Read recipients and build a personalised email for each one
with open("recipients.csv") as f:
    reader = csv.DictReader(f)
    for person in reader:
        link = f"{BASE_URL}?id={person['tracking_id']}"
        email = template.replace("{{name}}", person["name"]).replace("{{link}}", link)

        filename = f"outbox/{person['tracking_id']}.txt"
        with open(filename, "w") as out:
            out.write(email)
        print(f"Generated email for {person['name']} -> {filename}")
