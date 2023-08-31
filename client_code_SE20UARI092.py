
import websockets
import asyncio

async def listen():
    url = "ws://10.59.228.49:1900"
    async with websockets.connect(url) as websocket:
        await websocket.send("Hello Server!")
        while True:
            message = await websocket.recv()
            print(message)

asyncio.get_event_loop().run_until_complete(listen())

