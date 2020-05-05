from requests_html import HTMLSession

PAGE_URL = 'https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/alarm_messages/12cucalrmmsgdef.html'


session = HTMLSession()
request = session.get(PAGE_URL)
# print(request)
scraped_alarms = request.html.find('#eot-doc-wrapper p')
# print(scrape_alarms.text)

# with open('scraped_alarms.txt', 'w') as f:
#     for alarm in scraped_alarms:
#         if alarm.text.startswith('Alarm'):
#             f.write(alarm.text + "\n")

print(scraped_alarms[-1].text)
