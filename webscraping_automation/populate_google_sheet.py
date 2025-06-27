import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials for Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("Prospect Companies").sheet1

# List of URLs
urls = [
    "https://www.nestle.com",
    "https://www.drreddys.com",
    "https://www.colacompany.com",
    "https://www.pfizer.com",
    "https://www.pepsico.com",
    "https://www.jnj.com",
    "https://www.danone.com",
    "https://www.bayer.com",
    "https://www.generalmills.com",
    "https://www.gsk.com",
    "https://www.kelloggs.com",
    "https://www.merck.com",
    "https://www.unilever.com",
    "https://www.roche.com",
    "https://www.nestlewaters.com",
    "https://www.sanofi.com",
    "https://www.mondelezinternational.com",
    "https://www.novartis.com",
    "https://www.kraftheinzcompany.com",
     "www.lilly.com",
    "www.tysonfoods.com",
    "www.tevapharm.com",
    "www.mars.com",
    "www.abbvie.com",
    "www.campbellsoupcompany.com",
    "www.amgen.com",
    "www.conagrabrands.com",
    "www.astrazeneca.com",
    "www.molsoncoors.com",
    "www.boehringeringelheim.com",
    "www.abinbev.com",
    "www.basf.com",
   " www.diageo.com",
    "www.pg.com",
    "www.theheinekencompany.com",
    "www.medtronic.com",
    "www.mckesson.com",
    "www.amerisourcebergen.com",
    "www.cardinalhealth.com",
    "www.medline.com"
]

# Function to fetch company data
def fetch_company_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract relevant details (this is an example, adjust as needed)
    company_name = soup.title.string if soup.title else "N/A"
    relevant_category = "N/A"  # Logic to determine category
    health_segments = "N/A"  # Logic to determine health segments
    probiotics_involvement = "N/A"  # Logic to determine probiotics involvement
    fortification_mentioned = "N/A"  # Logic to determine fortification
    potential_contact_person = "N/A"  # Logic to determine contact person
    
    return [
        company_name,
        url,
        relevant_category,
        health_segments,
        probiotics_involvement,
        fortification_mentioned,
        potential_contact_person
    ]

# Populate Google Sheet
for url in urls:
    company_data = fetch_company_data(url)
    sheet.append_row(company_data)

print("Google Sheet has been updated with company data.")