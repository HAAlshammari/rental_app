import gspread
from oauth2client.service_account import ServiceAccountCredentials

def submit_to_sheet(date, flats_a, flats_b, flats_c, total_cost, total_income, inv1, inv2, inv3):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("rental_service_account.json", scope)
    client = gspread.authorize(creds)

    # 👇 Replace with your actual sheet name
    sheet = client.open("RentalData").Sheet1

    sheet.append_row([
        date,
        flats_a,
        flats_b,
        flats_c,
        total_cost,
        total_income,
        inv1,
        inv2,
        inv3
    ])
