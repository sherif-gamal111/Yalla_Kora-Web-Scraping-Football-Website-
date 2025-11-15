🏆 YallaKora Football Matches Web Scraper

A Python web scraping project that extracts detailed football match information from YallaKora Match Center based on a user-provided date, then saves the results into a structured CSV file with full UTF-8 support.

This tool is useful for football enthusiasts, data analysts, and developers who want to automate match data collection.

📌 Features

✔️ Scrapes match data for any date (MM/DD/YYYY)
✔️ Extracts the following information:

Championship name

Match date/status

Team A & Team B

Match time

Match score

Broadcasting channel

Match status / duration

✔️ Automatically saves results into a UTF-8 CSV file (supports Arabic text)
✔️ Error-tolerant — handles missing fields gracefully
✔️ Uses clean, reliable BeautifulSoup parsing logic

🛠️ Technologies Used
Component	Purpose
Python 3	Core programming language
Requests	Fetches HTML content
BeautifulSoup (bs4)	Parses and extracts HTML elements
lxml	High-performance HTML parser
CSV module	Exports structured data

Install dependencies:

pip install requests
pip install beautifulsoup4
pip install lxml

🚀 How It Works

The user inputs a date in the format:

MM/DD/YYYY


The script sends a GET request to:

https://www.yallakora.com/match-center?date=<date>


BeautifulSoup parses all match cards (matchCard divs).

For each match, the script extracts:

Teams

Result

Time

Channel

Status and duration

Championship title

All match data is saved into:

YallaKoraProject.csv


with UTF-8-SIG encoding to support Arabic characters.

📁 Project Structure
.
├── scraper.py             # Main scraping script
└── YallaKoraProject.csv   # Output file (created after running)

▶️ Usage

Run the script:

python scraper.py


Enter a date when prompted:

Please enter the date in the following formate MM/DD/YYY:


Once completed, you'll see:

File is created


Your CSV file will be generated in the configured output path.

📝 Sample Output (CSV)
Championship	Match Status	Team A	Team B	Time	Score	Channel	Duration
Egyptian Premier League	15 Nov 2025	Al Ahly	Zamalek	20:00	(1 - 1)	OnTime Sports	Finished
⚠️ Notes

If YallaKora changes its HTML layout, the CSS selectors may need to be updated.

The script handles missing fields and marks them as "غير محدد" to avoid crashes.

Ensure you update the CSV output path to a location that exists on your machine.

📄 License

This project is licensed under the MIT License.
