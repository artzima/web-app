import asyncio
import json
import websockets
import socket

async def mult(websocket, path):
    host = socket.gethostname()
    data = await websocket.recv()
    data = json.loads(data)
    number1 = data["number1"]
    number2 = data["number2"]
    
    result = number1 * number2
    
    response = {
        "result": f"{host} -> {result}"
    }
    
    await websocket.send(json.dumps(response))

start_server2 = websockets.serve(mult, "0.0.0.0", 8899)
asyncio.get_event_loop().run_until_complete(start_server2)
asyncio.get_event_loop().run_forever()