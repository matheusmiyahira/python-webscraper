# This script aims to parse missing alarms from cisco.com due to HTML element misconfiguration
import re


def get_content():
    with open('missing_alarms.txt', 'r') as f:
        content = f.read()
    return content


def parse_content(content):
    parsed_content = {}
    content = content.replace(':\xa0', ":")
    # new_content = [line.split(':') for line in content]

    pattern = re.compile(r'(.*:)(:.*)', flags=re.MULTILINE)
    matches = pattern.findall(content)
    new_content = matches.replace()

    # pattern = re.compile(r':\xa0', flags=re.M)
    # matches = pattern.findall(content)

    # matches = matches.replace(r"\1\'\:\'\3", pattern)

    # alarm_pattern = re.compile(r'^Alarm Name.*', flags=re.M)
    # matches = alarm_pattern.findall(content)
    parsed_content = new_content
    return parsed_content

# d={}
# for match in matches:
#     key_ = match.split(': ')[0]
#     value = match.split(': ')[1]
#     d[key]=value


def main():
    content = get_content()
    parsed_content = parse_content(content)
    print(parsed_content)


if __name__ == "__main__":
    main()
