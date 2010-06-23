#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       proxpy.py
#       
#       Copyright 2010 Curtis (Programble) <programble@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import socket
import sys

from select import select

# Command-line arguments
# proxy.py <local port> <remote address> <remote port>
if len(sys.argv) < 4:
    print "Usage: %s <local port> <remote address> <remote port>" % sys.argv[0]
    sys.exit(1)

# Validate arguments
try:
    int(sys.argv[1])
    int(sys.argv[3])
except ValueError:
    print "Invalid port number"
    sys.exit(1)

# Set up local listener socket
local = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "\033[31m---\033[0m binding socket to port %s" % sys.argv[1]
local.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # To allow port reuse upon crash
local.bind(('', int(sys.argv[1])))
print "\033[31m---\033[0m listening"
local.listen(1)

# Accept a connection
x = local.accept()
print "\033[31m---\033[0m local connection from %s" % x[1][0]
local.close()
local = x[0]

# Connect to remote server
print "\033[31m---\033[0m connecting to remote server %s:%s" % (sys.argv[2], sys.argv[3])
remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    remote.connect((sys.argv[2], int(sys.argv[3])))
except (socket.error, socket.gaierror), e:
    print "\033[31m---\033[0m %s" % e
    print "\033[31m---\033[0m closing local connection"
    local.close()
    sys.exit(1)
print "\033[31m---\033[0m established connection, starting relay"

# Relay buffers
localbuffer = ""
remotebuffer = ""

# Main loop
try:
    while True:
        read, write, error = select([local, remote, sys.stdin], [], [local, remote], 5.0)
        
        # Check if closed
        _, write, _ = select([], [local, remote], [], 0.0)
        if local not in write:
            print "\033[31m---\033[0m local socket closed"
            break
        if remote not in write:
            print "\033[31m---\033[0m remote socket closed"
            break 
        
        # Check for errors
        if local in error:
            print "\033[31m---\033[0m error on local socket"
            break
        if remote in error:
            print "\033[31m---\033[0m error on remote socket"
            break
        
        # Read from sockets
        if local in read:
            localbuffer += local.recv(4096)
        if remote in read:
            remotebuffer += remote.recv(4096)
        
        # Relay data
        if len(localbuffer):
            x = remote.send(localbuffer)
            print "\033[32m<<<\033[0m %s" % localbuffer[:x]
            localbuffer = localbuffer[x:]
        if len(remotebuffer):
            x = local.send(remotebuffer)
            print "\033[33m>>>\033[0m %s" % remotebuffer[:x]
            remotebuffer = remotebuffer[x:]

        # Read from standard input
        if sys.stdin in read:
            x = raw_input()
            if len(x) == 0:
                continue
            direction = x[0]
            if direction == '>':
                # Send to local
                remotebuffer += x[1:] + "\n"
            elif direction == '<':
                # Send to remote
                localbuffer += x[1:] + "\n"
            
except KeyboardInterrupt:
    print "\033[31m---\033[0m closing sockets"
except Exception, e:
    print "\033[31m---\033[0m error: %s" % e
finally:
    local.close()
    remote.close()

