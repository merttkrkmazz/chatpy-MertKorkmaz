import asyncio
import websockets

closing_message = "close"

async def hello():
        async with websockets.connect("ws://localhost:8791") as websocket:
            response = await websocket.recv()
            print(f"Response from server: {response}")
            print("Type your name")
            message = input("") #To start client should enter name
            await websocket.send(message)

            while True:      
                server_response = await websocket.recv()
                print(f"Client's message is: {server_response}")  #Receive messages from clients
            
                client_message = input("Type: ")
                await websocket.send(client_message) #Send message to server
                if client_message == closing_message:
                    break

                
        
                
asyncio.run(hello())
