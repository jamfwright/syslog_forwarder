# Python Syslog Forwarder

Python built syslog forwarder.  Accepts and redirects to a collector.  Handy for a single allowed host in a restricted network or security zone to send logs to a SIEM or other collector.  

Allows a Windows computer to play the role.

Pretty basic, just sits there accepting and forwarding syslog on UDP port 514.  Set the destination syslog collector by IP address in the forwarder.conf file and make sure it is in the same directory.

ZIP file is the same program converted to a Windows EXE so that it can be run without installing Python.

Designed for use in niche cases, but could see it used in pentesting and red teaming (one example:  ARP poisoning, then send logs to pentest owned collector)


Wrote the forwarding code, the listener code came from this awesome example from marcelom:  https://gist.github.com/marcelom/4218010
