This is the classic Snakes and Ladder game which I have coded in python. By use of socket programming we can play between two different devices connected via ethernet cable or must be on same network. 
I have made use of TCP protocol to exchange messages between two players. 
 
1) Client : The client function initializes the objects and also updates the window at 
every frame.  Here is the logic part of the game which moves the players constantly and depends on the timing of requests and data send/received by Server. There are different methods such as snake_ladder, ladder_jump, snake_bite, etc to keep the game running. All these methods move the two players’ positions in the 
game.  

2) Server : The server is the heart of the game.  The server is the place where send and receive of data occurs.  A  TCP socket is created and it can connect 2 clients. At start, two objects of the player class are created  whose positions are continuously updated and sent to the respective clients. If the 1st player sends data, the position of 2nd client is sent and vice versa. Thus the game keeps on running.
When a new client connects, a new dedicated thread for it is started which allows us to simultaneously communicate at two clients so that conflicts are not created. 