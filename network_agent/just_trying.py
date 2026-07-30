import requests
ip_address=requests.get('https://api.ipify.org').text
ip_ad2=requests.get('https://api.ipify.org')
# print(type(ip_ad2))
# print(ip_ad2)
# print(ip_address)
# page=requests.get('https://www.netflix.com/watch/81210705?trackId=264293154&tctx=1%2C0%2Cdbdd4cbd-fafa-486f-86d0-ede34549cdc0-315501236%2CeyJwYWdlSWQiOiJQU18xZWEwOGRlMi05OTQzLTQ0N2QtODU3ZS04ZTA3NTM0YzhhNTdfTDFfTjEyIiwic2VjdGlvbklkIjoiMmUwMzMxNDUtZWM0OC00MGNhLWFlNjYtMmNmNzc5NWNhMDA3IiwiaWR4IjotOTk5fQ%3D%3D%2CPS_1ea08de2-9943-447d-857e-8e07534c8a57_L1_N12%2C%2C%2C%2C%2CVideo%3A81210705%2CdetailsPagePlayButton').text
# print(page)
# page=requests.get('https://www.thehindu.com/news/national/lok-sabha-clears-anti-paper-leak-amendment-bill-amid-opposition-din/article71281283.ece')
# print(page.status_code)
# print(page.headers["Content-Type"])
# sample_read=requests.get('https://www.thehindu.com/news/national/lok-sabha-clears-anti-paper-leak-amendment-bill-amid-opposition-din/article71281283.ece')
# with open("sample_reading.html", "w") as file:
#     file.write(sample_read.text)

# with open("sample_reading.html", "r") as file:
#         content=file.read()
# print(content)
#these above 2 code block helped us scrap the website using restapi
location=requests.get(f'https://ip-api.com/json/{ip_address}').json()
print(location)