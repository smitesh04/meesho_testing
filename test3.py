import urllib.parse

cookie = 'ANONYMOUS_USER_CONFIG=j%3A%7B%22clientId%22%3A%221c967514-8f08-4081-ae6a-18b79173%22%2C%22instanceId%22%3A%221c967514-8f08-4081-ae6a-18b79173%22%2C%22xo%22%3A%22eyJ0eXBlIjoiY29tcG9zaXRlIn0%3D.eyJqd3QiOiJleUpvZEhSd2N6b3ZMMjFsWlhOb2J5NWpiMjB2ZG1WeWMybHZiaUk2SWpFaUxDSm9kSFJ3Y3pvdkwyMWxaWE5vYnk1amIyMHZhWE52WDJOdmRXNTBjbmxmWTI5a1pTSTZJa2xPSWl3aVlXeG5Jam9pU0ZNeU5UWWlmUS5leUpwWVhRaU9qRTNNalkzTWpZd01UY3NJbVY0Y0NJNk1UZzRORFF3TmpBeE55d2lhSFIwY0hNNkx5OXRaV1Z6YUc4dVkyOXRMMmx1YzNSaGJtTmxYMmxrSWpvaU1XTTVOamMxTVRRdE9HWXdPQzAwTURneExXRmxObUV0TVRoaU56a3hOek1pTENKb2RIUndjem92TDIxbFpYTm9ieTVqYjIwdllXNXZibmx0YjNWelgzVnpaWEpmYVdRaU9pSmtNVEEyWm1FNVl5MDVOREkwTFRSbE0yWXRPRGsxWWkwME16WmhOV1ZrT0dKbE9Ua2lmUS54c2lYejJLYko0enBoYXYwTFY1bGRpRlM5YThhUFh5YWgxYUJfS1dPenRnIiwieG8iOm51bGx9%22%2C%22createdAt%22%3A%222024-09-19T06%3A06%3A57.725Z%22%7D'

# URL decode
decoded_cookie = urllib.parse.unquote(cookie)
print(decoded_cookie)
import urllib.parse
import base64

cookie = 'ANONYMOUS_USER_CONFIG=j%3A%7B%22clientId%22%3A%221c967514-8f08-4081-ae6a-18b79173%22%2C%22instanceId%22%3A%221c967514-8f08-4081-ae6a-18b79173%22%2C%22xo%22%3A%22eyJ0eXBlIjoiY29tcG9zaXRlIn0%3D.eyJqd3QiOiJleUpvZEhSd2N6b3ZMMjFsWlhOb2J5NWpiMjB2ZG1WeWMybHZiaUk2SWpFaUxDSm9kSFJ3Y3pvdkwyMWxaWE5vYnk1amIyMHZhWE52WDJOdmRXNTBjbmxmWTI5a1pTSTZJa2xPSWl3aVlXeG5Jam9pU0ZNeU5UWWlmUS5leUpwWVhRaU9qRTNNalkzTWpZd01UY3NJbVY0Y0NJNk1UZzRORFF3TmpBeE55d2lhSFIwY0hNNkx5OXRaV1Z6YUc4dVkyOXRMMmx1YzNSaGJtTmxYMmxrSWpvaU1XTTVOamMxTVRRdE9HWXdPQzAwTURneExXRmxObUV0TVRoaU56a3hOek1pTENKb2RIUndjem92TDIxbFpYTm9ieTVqYjIwdllXNXZibmx0YjNWelgzVnpaWEpmYVdRaU9pSmtNVEEyWm1FNVl5MDVOREkwTFRSbE0yWXRPRGsxWWkwME16WmhOV1ZrT0dKbE9Ua2lmUS54c2lYejJLYko0enBoYXYwTFY1bGRpRlM5YThhUFh5YWgxYUJfS1dPenRnIiwieG8iOm51bGx9%22%2C%22createdAt%22%3A%222024-09-19T06%3A06%3A57.725Z%22%7D'

# URL decode
decoded_cookie = urllib.parse.unquote(cookie)
print("URL Decoded Cookie:", decoded_cookie)

# Extract and decode base64 parts
# The "xo" part and potentially other parts need to be base64 decoded.
base64_part = decoded_cookie.split('"xo":"')[1].split('"')[0]
decoded_base64 = base64.b64decode(base64_part).decode('utf-8')
print("Base64 Decoded Part:", decoded_base64)
