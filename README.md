Programble-Utils
================

Proxpy
------

Proxpy is a small proxy script that allows for monitoring incoming and
outgoing data. Its primary purpose is to test IRC bots, clients, and
servers, but it can also be used for any other network protocol
debugging.

### Usage

    proxpy.py <local port> <remote address> <remote port>

Local port is the port proxpy will listen on locally, and the port
which you will connect your client to. Remote address is the address
of the remote server which you want the proxy to connect to, and
remote port is the port to connect to.

#### Examples

    proxpy.py 6667 irc.freenode.net 6667
    irssi -c localhost -p 6667

This will open port 6667 on localhost as a proxy to port 6667 at
irc.freenode.net. Irssi is then connected to local port 6667, and
proxpy relays data between irssi and irc.freenode.net while also
outputting all incoming and outgoing data.
