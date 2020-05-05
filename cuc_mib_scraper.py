from requests_html import HTMLSession

PAGE_URL = 'http://www.ciscounitytools.com/Applications/CxN/RSK/Help/CISCO-UNITY-MIBContents.html'

session = HTMLSession()
request = session.get(PAGE_URL)

mib = request.html.find('#FHScroll p span')

with open('mib.txt', 'w') as mib_txt:
    for line in mib:
        mib_txt.write(line.text)
        mib_txt.write("\n")


# for line in mib:
#     print(line.text)
