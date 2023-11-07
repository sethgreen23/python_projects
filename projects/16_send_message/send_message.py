import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': "0021693345420",
        'message': "Good Morning",
        'key': 'textbelt',
    })
    
    if resp.status_code == 200:
        try:
            data = resp.json()
            print(data)
        except Exception as e:
            print(f"Failed to parse JSON response: {e}")
    else:
        print(f"Request failed with status code {resp.status_code}")
        print(resp.text)

# Schedule the job to run every 10 seconds
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
