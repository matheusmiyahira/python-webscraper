from requests_html import HTMLSession
from pprint import pprint
import csv

PAGE_URL = 'https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/alarm_messages/12cucalrmmsgdef.html'


def get_request_alarms():
    session = HTMLSession()
    request = session.get(PAGE_URL)
    request_alarms = request.html.find('#eot-doc-wrapper p')
    return request_alarms


def get_alarms_from_div(alarms):
    parsed_alarms = []

    for alarm in alarms:
        if not alarm.text.startswith("Alarm Name:"):
            continue
        alarm_tuples = [tuple(alarm_line.split(":", maxsplit=1))
                        for alarm_line in alarm.text.split("\n")]
        # print(alarm_tuples)
        alarm_tuples = [(field.strip(), value.strip())
                        for field, value in alarm_tuples]
        alarm_dict = dict(alarm_tuples)
    # print(alarm_dict)
    # print(type(alarm_dict))
    # # return alarm_dict
    # # pprint(alarm_dict)
    # #print(f"{alarm_dict['Alarm Name']}:\t{alarm_dict['Severity']}")
        parsed_alarms.append(alarm_dict)
    print(parsed_alarms)
    return parsed_alarms


def main():
    request_alarms = get_request_alarms()
    all_alarms = get_alarms_from_div(request_alarms)
    # print(f"Found {len(all_alarms)} alarms")
    # for alarm in all_alarms:
    #     print(alarm)
    # print(type(all_alarms))
    with open('alarms.csv', 'w', newline='') as alarms_csv:
        fieldnames = ['Alarm Name', 'Severity', 'Description',
                      'Route To', 'Explanation', 'Recommended Action']
        writer = csv.DictWriter(alarms_csv, fieldnames=fieldnames)
        writer.writeheader()
        for alarm in all_alarms:
            writer.writerow(alarm)


if __name__ == "__main__":
    main()

    # for alarm_line in alarm.text.split("\n"):
    #     alarm_column, alarm_value = alarm_line.split(":")
    #     print("|" + alarm_column + "|" + alarm_value)
    #     print()

# for alarm in alarms:
#     print(alarm)
#     print()

# alarmSplit = alarms.split('\n')
# print(alarmSplit)

# alarm = []
# for a in alarmSplit:
#     result = a.split(':')
#     alarm.append(result)

# print(alarm)

# alarmName = r.html.find('div#eot-doc-wrapper > p > b', first=True)
# print(alarmName.text)
