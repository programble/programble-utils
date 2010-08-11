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

While Proxpy is running, you may send data to the local connected
client as if the remote server had sent it by typing `>`, and then the
string of data. The data will be added to the buffer and will be sent
along with any other data the remote server has sent.

Similarly, you can send data to the remote server as if the local
client had sent it by first typing `<`, then the data to be sent.

#### Examples

    proxpy.py 6667 irc.freenode.net 6667
    irssi -c localhost -p 6667

This will open port 6667 on localhost as a proxy to port 6667 at
irc.freenode.net. Irssi is then connected to local port 6667, and
proxpy relays data between irssi and irc.freenode.net while also
outputting all incoming and outgoing data.

Updates.sh
----------

Updates.sh is a simple bash script used to determine the amount of
pending system updates in Arch Linux using the `pacman` package
manager. It can be used easily with the system monitor Conky to show
the amount of updates.

This script assumes you have Sudo set up so you can run `sudo pacman
-Sy` without providing a password.

### Usage

On a terminal:

    $ /path/to/updates.sh
    5

In Conky:

    ${texeci 3600 /path/to/updates.sh}


PBFC
----

PBFC is a Brainfuck to C compiler written in BASH.

### Usage

    pbfc source.bf [size]

Size defaults to 5000, and determines the amount of cells available to
the Brainfuck program.

PBFC will output a `.bf.c` file, which contains the generated C code,
along with an executable file compiled by the C compiler from this
code.

Squish
------

Squish is a little shell script that squishes things.

### Dependencies

 * curl
 * imagemagick
 * gzip
 * tar
 * bzip2

### Installation

To install Squish, run
    ./squish.sh -install squish.sh

As user, Squish will be installed to `~/bin/sq`. As root, Squish will
be installed to `/usr/bin/sq`.

### Usage

Squish can squish URLs, images, files, and directories.

#### URLs

Squish will create an is.gd shortened URL.

    $ sq http://github.com/programble/programble-utils
    http://is.gd/dI6SU

#### Images

Squish will create a thumbnail of the image 128 pixels wide.

    $ sq awesome_face.png
    awesome_face_thumb.png
    
#### Files

Squish will either gzip (default) or bzip2 a file.

    $ sq giant_virtual_disk.img
    giant_virtual_disk.img.gz
    $ sq -bzip2 giant_virtual_disk.img
    giant_virtual_disk.img.bz2

#### Directories

Squish will tar and either gzip (default) or bzip2 a directory.

    $ sq images/
    images.tar.gz
    $ sq -tarbzip2 images/
    image.tar.bz2
    
Ed Clone
--------

Ed is the standard text editor.

### Compilation

To compile Ed, run
    gcc -o ed ed.c
