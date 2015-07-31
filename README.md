BarTracker stores a database of barcodes, and stores who has scanned these barcodes, effectively allowing you to see where the item has been.

BarTracker works in 3 segments: A server ,a creator program, and a reader program.


The server works by listening on a port,until it recieves communication (the serverAssist.py script sends garbage data every so often to make the server program loop around, so it will periodically check if it needs to delete files).
When it recieves a "create" command, it creates a file with the name of its code, and stores what the product is, and who created it.
When it recieves a "read" command, it adds the cleint to the list of people accessing the file with the name of the code requested,reads the file ,and sends each line to the client.
Each time it loops, it checks all the data files, and checks if a certain elapsed time has elapsed since they were last accessed (In a real life implementation, we would set this to a week, in our test implementation, it is much shorter.).


The reader simply recieves a code from the user of the item (such as from the barcode scanner.)
It sends a "read" request to the server, with the code, and waits to recieve the number of lines the file contains, and recieves each of these lines.
It then outputs this data in a more human-readable way, in order of the last access to the file first.
If it recieves a "file does not exis" message, it tells the user as such.

The creator reveives a code, similiary to the reader, but also recieves a name of the product being logged.
It sends a "create" message to the server, with the code and and procuct name. It does not realy information back to the user.