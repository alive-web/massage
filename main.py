import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name('Massage-bfc7a6e7a61f.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Perfectial').sheet1

result = sheet.get_all_records()
print len(result)
print result
