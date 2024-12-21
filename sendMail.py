import smtplib
from datetime import datetime
import requests

s = smtplib.SMTP('smtp.gmail.com', 587)

def get_ip_and_location():
    ip_response = requests.get('https://api64.ipify.org?format=json')
    ip_data = ip_response.json()
    ip_address = ip_data['ip']
    
    # Get geolocation data
    geo_response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    geo_data = geo_response.json()
    latitude, longitude = geo_data['loc'].split(',')
    
    return ip_address, latitude, longitude

ip_address, latitude, longitude = get_ip_and_location()

s.starttls()
s.login("sahil456q@gmail.com", "dkdx dcoh ozku fdik")
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
subject = "Server Restart Notification"
body = f"This server has restarted at {formatted_time} with IP-Address: {ip_address} and Latitude:{latitude}, Longitude:{longitude}"
message = f"Subject: {subject}\n\n{body}"

print(message)
s.sendmail("sahil456q@gmail.com", "sahil456q@gmail.com", message)

s.quit()
