import time

import requests_async as requests

a = time.time()

async def get():
    responce = await requests.get('http://www.google.com')
    print("aaaaaa")

for i in range(1000):
    get()

print(time.time()-a)


async def main():
    loop = asyncio.get_event_loop()
    future1 = loop.run_in_executor(None, requests.get, 'http://www.google.com')
    future2 = loop.run_in_executor(None, requests.get, 'http://www.google.co.uk')
    response1 = await future1
    response2 = await future2
    print(response1.text)
    print(response2.text)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())