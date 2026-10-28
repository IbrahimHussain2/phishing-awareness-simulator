import csv

# Load all recipients
recipients = {}
with open("recipients.csv") as f:
    for person in csv.DictReader(f):
        recipients[person["tracking_id"]] = person["name"]

# Find unique recipients who clicked (ignore duplicates and unknown IDs)
clicked = set()
with open("clicks.log") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) >= 2:
            tracking_id = parts[1]
            if tracking_id in recipients:
                clicked.add(tracking_id)

total = len(recipients)
clicked_count = len(clicked)
rate = (clicked_count / total) * 100

# Print the report
print("=== Phishing Awareness Campaign Report ===")
print(f"Recipients: {total}")
print(f"Clicked the link: {clicked_count}")
print(f"Click rate: {rate:.0f}%")
print()

print("Who clicked:")
for tracking_id, name in recipients.items():
    status = "CLICKED" if tracking_id in clicked else "did not click"
    print(f"  - {name}: {status}")
print()

# Awareness suggestions based on the result
print("Recommendations:")
if rate >= 50:
    print("  - High click rate: run a mandatory awareness session for all staff.")
elif rate > 0:
    print("  - Some staff clicked: send targeted training to those who did.")
else:
    print("  - No clicks: good awareness. Keep testing periodically.")
