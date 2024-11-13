import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# Initialize undetected Chromedriver
options = uc.ChromeOptions()
# options.
# options.add_argument("--headless")  # Run in headless mode if needed

driver = uc.Chrome(options=options)
devtools = driver.execute_cdp_cmd("Network.enable", {})
driver.execute_cdp_cmd(
    "Network.setExtraHTTPHeaders",
    {"headers": {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'cookie': 'ANONYMOUS_USER_CONFIG=j%3A%7B%22clientId%22%3A%222bffe2fc-d2b2-4478-9892-881e8e2c%22%2C%22instanceId%22%3A%222bffe2fc-d2b2-4478-9892-881e8e2c%22%2C%22xo%22%3A%22eyJ0eXBlIjoiY29tcG9zaXRlIn0%3D.eyJqd3QiOiJleUpvZEhSd2N6b3ZMMjFsWlhOb2J5NWpiMjB2ZG1WeWMybHZiaUk2SWpFaUxDSm9kSFJ3Y3pvdkwyMWxaWE5vYnk1amIyMHZhWE52WDJOdmRXNTBjbmxmWTI5a1pTSTZJa2xPSWl3aVlXeG5Jam9pU0ZNeU5UWWlmUS5leUpwWVhRaU9qRTNNekUwTVRZNU1qUXNJbVY0Y0NJNk1UZzRPVEE1TmpreU5Dd2lhSFIwY0hNNkx5OXRaV1Z6YUc4dVkyOXRMMmx1YzNSaGJtTmxYMmxrSWpvaU1tSm1abVV5Wm1NdFpESmlNaTAwTkRjNExUazRPVEl0T0RneFpUaGxNbU1pTENKb2RIUndjem92TDIxbFpYTm9ieTVqYjIwdllXNXZibmx0YjNWelgzVnpaWEpmYVdRaU9pSXhaV00zWm1KbE5DMDNaV1F6TFRRNE1qVXRPV013WXkwek16UmpOamcxTURRME1HWWlmUS5oaDltOUVaUl9HMzNTbXpfSjVVUkc4Z05ZRGRQLV9jY2VId3ZUbjByc3E0IiwieG8iOm51bGx9%22%2C%22createdAt%22%3A%222024-11-12T13%3A08%3A44.145Z%22%7D; ak_bmsc=DB77140AFF841788D70C78BCC5B545D2~000000000000000000000000000000~YAAQX/7UF/6+ugeTAQAAT6B9IBlVrTRe2lkYiA/shInlUFnOZGPjNqVZ4rPBv9yZfa5s217XtnjYLSs2e7DI/+9kgNHLQ7QOUO41djXJDETpaXmhdUeaVRpWxtHTnnUyb/e1tzprJf7kh8sAx55e0BN3urVWX5qhEnhK7DaRs3wcY62Agc1jIMT/ipl352PQLceOu6+oDuFykrgYwMHnCK3T7gGOW7gWcH4oRHq2F4+IufFlONh61U7ZEeFXVRy+ycwEpPRrOX0DnW5E966RVm91dqXHoRYzsh9KjBdHvlgcRahewZKUk8FwfuFsbn9rSkllZ3y93t7Dqv3WrTUsbNjE/oyozuswfpKyxm0zZrwJKXr7ZbFc8sBT5TqP2bDpieDldMrHoBBU; CAT_NAV_V2_COOKIE=0.24300817770694505; INP_POW=0.0957020407919611; __logged_in_user_id_=405180161; _is_logged_in_=1; __connect.sid__=s%3AWdagH2Ah_NvmtV3IuHbo74f1KQP_h3-B.dpcAZxBJRG4%2B1lX5NrA2essLFyV7mtG%2BF4spSDHhmpA; bm_sz=A296222E6532D5B04396620C9F46373D~YAAQX/7UF6nOugeTAQAAecJ+IBlG4ogvgQ3j/2PEA+5IgTv161rw0+kNQVKU7cyKo+wmQDvgohSS1weqFHfxg5xnhtvweBNW2AT9zgkt+bcrasIykqBVSRiJwr1dBPmi2V5LHUwPgJjl78EupCGixa64MILt8d9XscXY66N9G+J0GRqBywh0v1U1j/y1PhWRxa6F1ioxCqYxdC/irJlmlZIZDv3ikkIJT8WiF+IGKhVps2TmZtMMsRyd4Bogc+HccIDneJpiRRRkM7o9hM4HTJhvolPnnCJu+uSS0P/3zwB0XIS0r+JFf95uK/h0kiTRKSxomnabBh8HO8N497FdJEy77QXeXiGl+49qzb+w7uTrpBCxvKLmOnHK8yy4IfaXjBms3pbiqDqcVqrAcwBesg6kSokVzF8vEBeJPk3cG00lfJ3XzzD5Qg==~3354950~3682608; location-details=%7B%22city%22%3A%22Bengaluru%22%2C%22lat%22%3A%2213.2257%22%2C%22long%22%3A%2277.575%22%2C%22pincode%22%3A%22560001%22%7D; _abck=1C918A55263667B5E17B40BD66C1499A~0~YAAQX/7UFzXPugeTAQAANct+IAywgB1cw45sCPwjIQwy0Hn0osZ1gSSGXVkOHHDWfaqwsma5Pamgt5TVgQi/ucVq9A08F7z33vaix6/QjgnaqpSNknCk2w6ES378DxvFNpAkrrlqvBHIjGa+iDadJ9FbQZhscqiKIMVh/kIC967VVZOqiTPpVNyqkwJRCgI4OkJhJ5J/zUIymy88VUEeaEdcvRs+qqM+FwmTMk/CGZVKw9HBcZaj8GjDprKY5AUz66f+LEcGSW7bnTdOVtJCjpM6LybV3jLhR1VAeNYDKhI/y4gWGnmFtLouBkOksW7S7Q4wISqP5ZEC2QStLBooT/cnABjg5fDfhcnKxiC8O1tQBhGti+PL0gq/F2fXgWY/mgicVbUfYGJ8Zj8/QLnJ/dAahWtU3AFWsf5HO2BWhDnTC1FlAbpoFqzUfNgCUZ9YjsWXRfy7yAeiY5fwVMj/4dYILbnZGEGl0LHKJ4PDhRj4oRn/Ak5hz/iO6dYujCpDEA9FqL8eYqn1gwADetpMLO4aEdBXb3UdRjqbjLML/JFeT0dSnfx682Sy9hsN9bE9Cnd0KRSdtOOphA5DE7RKkM98VD+bq/xA2f1vl+XyIJbdwB6HcfTna+xI6ibl7NGA5GS1UuhswUanpz5B5Ot2/OaDd4WKdOOMP9tk5Z8uFD2vHuLvWzpuzsztZVw9s/zzA8rRsw==~-1~||0||~1731420529; bm_sv=BED92F7A1AAFCF3AA31A3DC14AD3DCE6~YAAQX/7UFx3RugeTAQAAoet+IBklhgZUb6cjJZg8DNOSHKfeWX2ui/gGIaekzOEIovMXxNirrMhPJ49CYBbvl8hznvQfQqpcLkGy5foM2bWlVlOKXr52o3ZcudkXbqo0L972l0+T28oa38WJGYG8wTV4Ld8l1SMRRZwP78aOtK2gNmfPzkpoZyEq0ZV24MlbqLQ9+opVPBFJRYSsyYEyfeSwJwtt5Std/Clh1DP+TOg9IGME69B3/uyF8UFyVTc4dw==~1; mp_60483c180bee99d71ee5c084d7bb9d20_mixpanel=%7B%22distinct_id%22%3A%20%22193207db4321ec-0c97bec408b0cf-26011951-e1000-193207db4336df%22%2C%22%24device_id%22%3A%20%22193207db4321ec-0c97bec408b0cf-26011951-e1000-193207db4336df%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20405180161%2C%22Is%20Anonymous%22%3A%20%22False%22%2C%22Instance_Id%22%3A%20%222bffe2fc-d2b2-4478-9892-881e8e2c%22%2C%22Session%20ID%22%3A%20%22367ec2fe-48ff-4437-90a1-94f3245c%22%2C%22V2%20Cat-Nav%20Exp%20Enabled%22%3A%20true%2C%22last%20event%20time%22%3A%201731417014450%2C%22__alias%22%3A%20405180161%7D',
  'meesho-iso-country-code': 'IN',
  'origin': 'https://www.meesho.com',
  'priority': 'u=1, i',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}}
)
pid = '1006o8'
pin = '400001'

url = f'https://www.meesho.com/s/p/{pid}'
url = 'https://www.meesho.com/mens-latest-light-weight-comfortable-and-stylish-slipper-colorfull-flip-flops/p/67vvq7'
# Navigate to a webpage
driver.get(url)

# Extract title
print("Page title:", driver.title)

# Close the browser
driver.quit()
