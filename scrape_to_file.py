from requests_html import HTMLSession

PAGE_URL = 'https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/alarm_messages/12cucalrmmsgdef.html'


session = HTMLSession()
request = session.get(PAGE_URL)
# print(request)
scraped_alarms = request.html.find('#eot-doc-wrapper p')
# print(scrape_alarms.text)

with open('scrape_to_file.txt', 'w') as f:
    for alarm in scrape_to_file:
        if alarm.text.startswith('Alarm'):
            f.write(alarm.text + "\n")


# alarms = [alarm.text +
#           "\n" for alarm in scraped_alarms if alarm.text.startswith('Alarm')]
# print(alarms)


# alarms = [alarm.split("\n") for alarm in alarms]
# # alarms = [alarm.split(":", maxsplit=1) for alarm in alarms.split("\n")]

# print(alarms)
# print(len(alarms))

# alarms = [(key.strip(), value.strip()) for key, value in alarms]
# for alarms in alarms:
#     print(alarms)


# for alarm in alarms_dict:
#     alarms_th = []
#     print(alarms_dict[0][0])

# alarms_th = [alarm[0][0] for alarm in alarms_dict]
# print(alarms_th)

# def main():
#     scraped_alarms = get_scrap_request()
#     parsed_alamrs = parse_scrape(scraped_alarms)
#     print(parsed_alamrs)


# if __name__ == "__main__":
#     main()
