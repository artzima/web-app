import asyncio
import json
import websockets
import socket

async def addition(websocket, path):
    host = socket.gethostname()         #запись hostname в переменную
    data = await websocket.recv()       #получение запроса от клиента
    data = json.loads(data)             #преобразования строки JSON в объект Python
    number1 = data["number1"]           #первое число от фронта, полученные на предыдущем шаге
    number2 = data["number2"]           #второе число от фронта, полученные на предыдущем шаге
    
    result = number1 + number2
    
    response = {
        "result": f"{host} -> {result}" #формирование строки вывода, отправляемые на фронтенд
    }
    
    await websocket.send(json.dumps(response))              #отправка данных, с обратным преобразованием объекта Python в строку JSON

start_server1 = websockets.serve(addition, "0.0.0.0", 8888) #открытие web-сокета на стороне сервера на порту 8888
asyncio.get_event_loop().run_until_complete(start_server1)  #запуск и получение текущего цикла события 
asyncio.get_event_loop().run_forever()                      #обеспечения бесконечного цикла событий