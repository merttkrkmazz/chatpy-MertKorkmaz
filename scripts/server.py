import asyncio
import websockets

clients = []

async def greet(websocket, path):
    print("Server Created!!")
    clients.append(websocket)
    response = "Hello Client!"
    print(f"Sending Response: {response}")
    await websocket.send(response)

    try:
        while True:   #Always listening for a message
            
            new_message = await websocket.recv()
            print(f"Received message from client: {new_message}")
            await broadcast(new_message)

    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed by the client")
                

async def broadcast(new_message: str):
    for client in clients:
        await client.send(new_message) #Sends the message for all clients who joined the server.

async def main():
    async with websockets.serve(greet, "localhost", 8791):
        await asyncio.Future()

asyncio.run(main())




