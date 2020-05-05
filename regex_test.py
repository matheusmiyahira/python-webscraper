import re

content = '''
Alarm Name: EvtCucSlrInProgress
Severity: INFORMATIONAL_ALARM
Description: License Reservation in progress.
Route To: Event Log
Explanation: >License Reservation in progress.
Recommended Action: License Reservation process must be completed by executing the 'license smart reservation install' CLI command.
Alarm Name: EvtCucSlrCancel
Severity: INFORMATIONAL_ALARM
Description: This will cancel the reservation request and put the Product Instance back in the unregistered state.
Route To: Event Log
Explanation: This will cancel the reservation request and put the Product Instance back in the unregistered state.
Recommended Action: No Action is required.
'''
# pattern = re.compile(r'(Alarm Name)', flags=re.MULTILINE)
# content = re.split(r'\n(Alarme Name)', content)
pattern = re.compile(r'(Alarm Name.*/b)')
# content = pattern.sub(r'\n\1\2', content)
content = pattern.findall(content)
print(content)

# for line in content:
#     content = [k for k in content.split('\n') if len(k) > 1]
#     content_dict = {k.split(':')[0]: k.split(':')[1].strip() for k in content}
#     print(content_dict)


# pattern = re.compile(r'\n.*', flags=re.MULTILINE)
# content = pattern.findall(content)
# print(content)


# for line in content:
#     print(content)
