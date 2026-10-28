from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime
import csv

# Load tracking_id -> name so the log is readable
recipients = {}
with open("recipients.csv") as f:
    for person in csv.DictReader(f):
        recipients[person["tracking_id"]] = person["name"]


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        tracking_id = query.get("id", ["unknown"])[0]
        name = recipients.get(tracking_id, "Unknown recipient")

        # Log the click
        with open("clicks.log", "a") as log:
            log.write(f"{datetime.now().isoformat()},{tracking_id},{name}\n")

        # Show the awareness page (no password is ever requested)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        page = f"""
        <html><body style="font-family: sans-serif; max-width: 600px; margin: 40px auto;">
        <h1>This was a phishing awareness test</h1>
        <p>Hi {name}, this was a simulated phishing email sent as part of security training.
        No harm has been done, and nothing you do here is stored beyond recording the click.</p>
        <h2>What gave it away:</h2>
        <ul>
          <li>It created urgency ("expire today", "access may be suspended")</li>
          <li>It asked you to "confirm details" through a link</li>
          <li>The sender was a generic "IT Support" with no real contact</li>
        </ul>
        <p>In future, check the sender and hover over links before clicking.</p>
        </body></html>
        """
        self.wfile.write(page.encode())

    def log_message(self, format, *args):
        pass  # keep the terminal quiet


print("Awareness server running at http://localhost:8000")
print("Press Ctrl+C to stop.")
HTTPServer(("localhost", 8000), Handler).serve_forever()
