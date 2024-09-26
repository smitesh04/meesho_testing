import random
import time
import urllib

import requests
from fake_useragent import UserAgent
ua = UserAgent()
import json

for i in range(100):
  try:
    time.sleep(random.choice(range(2,20)))
    ses = requests.Session()
    # headers = {
    #       'accept': 'application/json, text/plain, */*',
    #       'accept-language': 'en-US,en;q=0.9',
    #       'content-type': 'application/json',
    #       'meesho-iso-country-code': 'IN',
    #       'origin': 'https://www.meesho.com',
    #       'priority': 'u=1, i',
    #       'user-agent': ua.random
    #     }
    # response_cookie = ses.get("https://www.meesho.com", headers = headers)
    # cookie = response_cookie.cookies.get_dict()
    # anonymous_user_config = cookie['ANONYMOUS_USER_CONFIG']
    # abck = cookie['_abck']
    # ak_bmsc = cookie['ak_bmsc']
    # bm_sz = cookie['bm_sz']
    # # encoded_cookie = urllib.parse.quote(str(cookie))
    # # print(encoded_cookie)
    # url = "https://www.meesho.com/api/v1/user/login/request-otp"
    #
    # payload = json.dumps({
    #   "phone_number": "9328052205"
    # })
    # def headers(anonymous_user_config, abck, ak_bmsc, bm_sz):
    def headers():
        headers = {
          'accept': 'application/json, text/plain, */*',
          'accept-language': 'en-US,en;q=0.9',
          'content-type': 'application/json',
          # 'cookie': f'ANONYMOUS_USER_CONFIG={anonymous_user_config};_abck={abck};ak_bmsc={ak_bmsc};bm_sz={bm_sz};',
          'cookie': f'ANONYMOUS_USER_CONFIG=j%3A%7B%22clientId%22%3A%225d255aaf-1f4c-4e90-a9ef-d2ef6b10%22%2C%22instanceId%22%3A%225d255aaf-1f4c-4e90-a9ef-d2ef6b10%22%2C%22xo%22%3A%22eyJ0eXBlIjoiY29tcG9zaXRlIn0%3D.eyJqd3QiOiJleUpvZEhSd2N6b3ZMMjFsWlhOb2J5NWpiMjB2ZG1WeWMybHZiaUk2SWpFaUxDSm9kSFJ3Y3pvdkwyMWxaWE5vYnk1amIyMHZhWE52WDJOdmRXNTBjbmxmWTI5a1pTSTZJa2xPSWl3aVlXeG5Jam9pU0ZNeU5UWWlmUS5leUpwWVhRaU9qRTNNalkzTXpjeE9Ea3NJbVY0Y0NJNk1UZzRORFF4TnpFNE9Td2lhSFIwY0hNNkx5OXRaV1Z6YUc4dVkyOXRMMmx1YzNSaGJtTmxYMmxrSWpvaU5XUXlOVFZoWVdZdE1XWTBZeTAwWlRrd0xXRTVaV1l0WkRKbFpqWmlNVEFpTENKb2RIUndjem92TDIxbFpYTm9ieTVqYjIwdllXNXZibmx0YjNWelgzVnpaWEpmYVdRaU9pSXdNREF4TURoaE1pMHpOMlZtTFRRNVpHWXRPVE13TXkxaE5qVTROV1UwWkRReU9UY2lmUS5vUVJmRG9ZWmVfdy1nTHpWQy1RMDBUa2ViZjhaMjgyQlMtNjJYc2YzNWZ3IiwieG8iOm51bGx9%22%2C%22createdAt%22%3A%222024-09-19T09%3A13%3A09.188Z%22%7D; CAT_NAV_V2_COOKIE=0.956950716716821; ak_bmsc=8289BB48ABA631DF6DB1E61D4905CC35~000000000000000000000000000000~YAAQvrRmUog0wbKRAQAA45WOCRm1g/6rkxs2PSX6ogexMLEnCUgyQUeTex0YKk9EWJMdbDsipvYFdE1ckH98IVIDDsYcKFPjq1T9cMidMUflUIMUV6kokEVjqem7bSoQUfwFgmGiuYxczCRb/dd7wI9Sp+xDVOKhaQRF5XrhN4h0ynm2XImF3seAT2r5wapTI5UGEXlL5a91pp1tagwz5e9zUxh/qoQhZLc1qu4Zvl8BUCLz6J17I7PO+5OrtwIQs5n7whwJw77z7+7KqaHuhSfs3CnN/7GotHMmS63A/HLcT3J4ZVZzJNpC4NvOr41VA9jKDMB/tki6qhuV1Dd7+LWm+czAPpUwE16EEeiIz5/K+IrQdPn8dB6UUgdk0yL8u6Oqjseosh9Cn/XbR0gbZx+vBLRjqQ/fR02x30B59Vt+bcs1DUWtuDb15tk0dIdjWUSG; __logged_in_user_id_=384134770; _is_logged_in_=1; __connect.sid__=s%3AzfozMz7lfFz9gpJi4lpdE37NcSGRfrvR.Aew6LJg87JNZm%2F05nVmeIEjGgDq%2FLOVx5MOktpN3eK4; INP_POW=0.22550765299745423; location-details=%7B%22city%22%3A%22Gandhinagar%22%2C%22lat%22%3A%2223.2631%22%2C%22long%22%3A%2272.6739%22%2C%22pincode%22%3A%22382610%22%7D; _abck=FB3F21ECA16C06BD4487DD1D0E297DF1~0~YAAQtphmUglvg/2RAQAAzYmyCQyc+QLULj455vGM5iXXfchx3g/kf8XFcVmVjImt6oFmZNwG+ZqT5JyvnPLVHgp9KojtNBhv7bdLsuuj8BWfUqCggR0OxQT/inlxNsohE29OI7/NhkcVkYd7SCZhrrzwLoSgDRURJnP0QZumkHts9DyupxcMTmohz7FeVF8iICWD4+x4kTOEGXko2wYtsOqRxM3Ra5oxDX2VHG3fvuAqFQ3BSh3IAC38H6qFZ7spPagRggVHYF1FtV0zY5ApDP0RtzKFQhzLDKpK2z7YgL6Ossns9kTcvCg6roKXUWZtBusraMhP65YwCYcbHUQuqn8cvwLRYU4fufsopEOB1rpmHY+Xk76My+ioiBrVaJbxugeBxPbYFzIRjD9YW8aA+thdZytrpqzBkh2OcJrjQirHM857sWNRyFfNUjm7Kyah7b5ODbQl00QCi9l+OeEVlRX9hAmzNeNMyTJoP6lSd5FZEMho+CbnduzOeRMCPyAExRG65LkVz4IGHRzhqAcSN4O0Cqx2RavCKC6tKBwW/DLEr9ciEOdPJgFepaUZ+BmdEa8RXPo8154=~-1~||0||~1726740790; bm_sz=32718431D27F6E53B0ACD0DD77703AE1~YAAQtphmUgpvg/2RAQAAzYmyCRn2N99Pi2Lie7qb1lGkKRq56SBrwmG7HFejeaPFGeFfUg61AN6IlMsy706xTSwWi5CEs4qRMYRa8aGFZE+s70g3cKxybQ6deQPhaAqvaa0o4coHagPiHo8q/ROchWqMs6xasVRiMZ1Fb1L9/36ytmuye1g3c/nxTOZfxsRAn9X+7rcIK/phl3kfy6/hsLxabhAXPsHDX9RB1i8hacNjD/kIhrOAvLoo7ypEQKv4hZCw39R+nX7a+oVOrQ89iS7GYLYDgEKFK3AYuWPee+c9Wn4pMowWPz2dXbco0nHWpWxsuQ9YT7qhTLG+ckkKdtfyHkbI/z8kMLC3oUomTqtMEgSmyyNzvvXm/RdfMUv9I9fhFGRG8ul0miWtq5yqwllvHkOM56YoBL8P4qNA/QHeMc+mx1nd23MAfyxM~4605494~4469554; bm_sv=56FEFB83FAD6E9F7D9E9CB65E674B132~YAAQtphmUiJvg/2RAQAA+5ayCRnotRrwJOe+Q/twL2ER3wIHmPbURaPaGDkeKN/xvegm/mVGAiYjw8rd/D+zOt3qdY7Awe1uBP7dEh/w4I0B+B++js3av0I14xf4HXBQMjnvGz9ItrcAC4Z6e39j3HFkIhqZrOXvZkD5BTX8eYqe5ySf+iaDIksOgM7IGo5sX2xOi8+DPgLN3ZILMF4xtdC6mIEQPwGp3QJphOFdWoH7/SwNC6rzdj7/6VxpcFiPtA==~1; mp_60483c180bee99d71ee5c084d7bb9d20_mixpanel=%7B%22distinct_id%22%3A%20%22192098e98c34aa-09a2d3ba8dda1f-26001151-e1000-192098e98c4267%22%2C%22%24device_id%22%3A%20%22192098e98c34aa-09a2d3ba8dda1f-26001151-e1000-192098e98c4267%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22Is%20Anonymous%22%3A%20%22False%22%2C%22Instance_Id%22%3A%20%225d255aaf-1f4c-4e90-a9ef-d2ef6b10%22%2C%22Session%20ID%22%3A%20%223573cf0d-cda8-4572-8288-3df5f5df%22%2C%22V2%20Cat-Nav%20Exp%20Enabled%22%3A%20true%2C%22last%20event%20time%22%3A%201726739555691%2C%22__alias%22%3A%20384134770%2C%22%24user_id%22%3A%20384134770%7D',
          'meesho-iso-country-code': 'IN',
          'origin': 'https://www.meesho.com',
          'priority': 'u=1, i',
          'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': ua.random
        }
        return headers

    # response_otp = ses.request("POST", url, headers=headers(), data=payload)
    #
    # url2 = "https://www.meesho.com/api/v1/user/login"
    # otp = input("enter otp: ")
    # payload2 = json.dumps({
    #   "request_id": "b3M.skAK82LwCN",
    #     "otp":str(otp),
    #   "instance_id": "1c967514-8f08-4081-ae6a-18b79173",
    #   "phone_number": "9328052205",
    #   "login_type": "meesho_sms_auth"
    # })
    #
    # response_login = ses.request("POST", url2, headers=headers(), data=payload2)

    url3 = "https://www.meesho.com/api/v1/check-shipping-delivery-date"

    payload3 = json.dumps({
      "dest_pin": "382017",
      "product_id": "4zmepw",
      "supplier_id": 23046,
      "quantity": 1
    })

    response_final = ses.request("POST", url3, headers=headers(), data=payload3)
    # print(response_final.text)
    print(response_final.status_code)
    print(i)
  except Exception as e: print(e)