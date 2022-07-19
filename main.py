import requests, asyncio, os
import brotli
import aiohttp
from itertools import product, cycle

class tcheck:
    def __init__(self):
        self.token = str(input('\u001b[0m[\x1b[\x1b[38;5;63m/\u001b[0m] Token \x1b[\x1b[38;5;63m>> \u001b[0m'))
        print('\u001b[0m[\x1b[\x1b[38;5;63m/\u001b[0m] Checking Token...\n')
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(tcheck.checkToken(self))

    async def checkToken(self):
        headers = {':authority': 'discordapp.com', ':method': 'GET', ':path': '/api/v6/users/@me', ':scheme': 'https', 'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9', 'authorization': self.token, 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'cross-site', 'sec-gpc': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}
        async with aiohttp.ClientSession(headers=headers) as client:
            async with client.get('https://discordapp.com/api/v6/users/@me/library') as res:
                if res.status != 200:
                    print('\u001b[0m[\x1b[\x1b[38;5;63mLOCKED\u001b[0m] True')
                    print('\u001b[0m[\x1b[\x1b[38;5;63mMESSAGE\u001b[0m] %s' % (((await res.json())["message"])))
                    return
                async with client.get("https://discordapp.com/api/v6/users/@me") as resp:
                    print('\u001b[0m[\x1b[\x1b[38;5;63mLOCKED\u001b[0m] False')
                    print('\u001b[0m[\x1b[\x1b[38;5;63mTAG\u001b[0m] %s#%s' % (((await resp.json())["username"]), (await resp.json())["discriminator"]))
                    print('\u001b[0m[\x1b[\x1b[38;5;63mEMAIL\u001b[0m] %s' % (((await resp.json())["email"])))
                    print('\u001b[0m[\x1b[\x1b[38;5;63mID\u001b[0m] %s' % (((await resp.json())["id"])))
                    if ((await resp.json())["email"]) == 'null':  print('\u001b[0m[\x1b[\x1b[38;5;63mPHONE\u001b[0m] %s' % "✓") 
                    else:  print('\u001b[0m[\x1b[\x1b[38;5;63mPHONE\u001b[0m] %s' % "✗")
                    if ((await resp.json())["verified"]) == True:  print('\u001b[0m[\x1b[\x1b[38;5;63mEMAIL VERIFED\u001b[0m] %s' % "✓") 
                    else:  print('\u001b[0m[\x1b[\x1b[38;5;63mEMAIL VERIFED\u001b[0m] %s' % "✗")
                    print('\u001b[0m[\x1b[\x1b[38;5;63mPFP\u001b[0m] https://cdn.discordapp.com/avatars/%s/%s.png?size=256 \u001b[0m' % (((await resp.json())["id"]), (await resp.json())["avatar"]))
                
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    doozle = tcheck()
