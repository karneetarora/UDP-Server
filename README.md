Implemented a UDP Server that has a Server and a Client. 

The goal of the Server is to reply to any Client with the IP address of any domain name sent to it. 

The server sends a UDP message to the Google DNS server at 8.8.8.8 and requests for the IP address. 

The server has two sockets: one socket 
- Socket 1: used to talk to the client 
- Socket 2: used to communicate with the Google DNS server
