#import aionmap
import asyncio
import sys

print(sys.version)

async def extraer_banner(ip):
    scanner = aionmap.PortScannerYield()
    async for result in scanner.scan(ip, None, "-sS -n --open -F"):
        if isinstance(result, Exception):
            print("error")
        else:
            print(result["portid"], result["scripts"][0]["raw"])

ip = "212.170.34.137"
loop = asyncio.get_event_loop()
loop.run_until_complete(extraer_banner(ip))