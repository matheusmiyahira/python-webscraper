import re

oid_pattern = re.compile(r'1\.3\.6\.1\.4\.1\.9\.9\.385.*\b')
desc_pattern = re.compile(r'DESCRIPTION\n".*"')

with open('mib.txt', 'r') as f:
    mib_txt = f.read()
    matches = re.findall(
        r'1\.3\.6\.1\.4\.1\.9\.9\.385.*\b' | 'DESCRIPTION\n', mib_txt)
    print(matches)

    # for match in matches:
    #     print(match)


# for line in mib:
#     mib_str += line.text + "\n"
# print(mib_str)

# desc_pattern = re.compile(r'DESCRIPTION\n".*(\n.*)*"', mib_str)

# parsed_mib = []

# for line in mib:
#     if re.search(r'1\.3\.6\.1\.4\.1\.9\.9\.385.*\b', line.text):
#         parsed_mib.append(line.text)
# print(parsed_mib)


# oids = request.html.find('#FHScroll p span.RVTS2')
# desc = request.html.find('#FHScroll p span.RVTS5')
# # mib = [(oid.text, desc.text) for oid in oids for desc in oids]
# # print(mib)

# for oid in oids:
#     print(oid.text)
#     for desc in oids:
#         print(desc.text)


# oids = request.html.search('1.3.6.1.4.1.9.9.385')
# print(type(oids))
# print(oids.html)

# oids = request.html.find('.RVTS2')
# print(type(oids))
# print(len(oids))
# for item in oids:
#     print(item.text)
