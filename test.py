from macheronte import WhatsappClient
from macheronte import Browsers

import time

client = WhatsappClient(Browsers.CHROME, '')
client.connect()

while True:
    try:
        if client.is_logged():
            status = client.get_user_status('Баха')

            print(status.value)
    except Exception as e:
        print(e)

    time.sleep(2)
