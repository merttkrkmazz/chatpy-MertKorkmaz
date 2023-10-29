# WebSocket Chat Application

## Introduction
This is a WebSocket-based chat application in Python using the `websockets` library. It allows multiple clients to connect to a central server and exchange messages in real time.
The server and clients use the websockets library to create a simple chat application. 


## How To Use The Code

#### SERVER
1. Clone this repository to your local machine.
2. Run the server with command python3 server.py
3. Server will be started and listening for the client's messages.

#### CLIENT
1. Clone this repository to your local machine.
2. Run the client by executing the client.py script:
3. The client will connect to the server and allow to send and receive chat messages.
4. Enter "close" to exit the chat session gracefully.

## SAFETY CONCERNS
Data Validation: The code does not perform extensive data validation. Users can send any text as messages, which could potentially lead to security problems or unexpected behavior. 

Error Handling: The code does not provide comprehensive error handling. 

Security: This is a simple example and does not include advanced security features. Be cautious when using WebSocket applications in production
