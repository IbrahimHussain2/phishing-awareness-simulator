# Phishing Awareness Simulator

A local tool that simulates a phishing awareness training campaign. It generates personalised training emails, tracks who clicks the link on a local server, shows them an educational "this was a test" page, and produces a report with the click rate and recommendations.

I built this to understand how security teams measure and improve staff awareness of phishing, which is one of the most common ways attackers get in.

## Responsible use
This tool is for **authorised security awareness training only**, for example your own test accounts or staff whose organisation has approved the training.

- It runs entirely **locally** and does not send real emails.
- The landing page **never asks for or stores passwords**. It only records that a link was clicked, then shows an educational message.
- Do not use it against anyone without their organisation's permission.

## How it works
1. `recipients.csv` lists the people in the campaign, each with a unique random tracking ID.
2. `generate.py` fills a template from `templates/` with each person's name and tracking link, saving the emails to `outbox/` (a simulated send).
3. `server.py` runs a local web server. When a tracking link is opened, it logs the click and returns an awareness page.
4. `report.py` reads the log and reports the click rate, who clicked, and recommendations. It counts unique recipients and ignores duplicate or invalid clicks.

## Running it
```
python3 generate.py          # build the training emails
python3 server.py            # start the tracking server (leave running)
# open a tracking link, e.g. http://localhost:8000/click?id=a1b2c3
python3 report.py            # view the results
```

## What I learned
- How phishing awareness campaigns are measured (click rate)
- Using a random tracking token so email addresses aren't exposed in URLs
- Cleaning messy log data: counting unique clickers, ignoring invalid entries
- Why runtime data and logs (which can contain personal data) are kept out of version control with .gitignore

## What I'd improve
- Add more templates and pick one per campaign
- Record *which* template each person received
- Export the report to CSV
