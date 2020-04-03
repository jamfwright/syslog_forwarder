#!/usr/bin/env python


LOG_FILE = 'youlogfile.log'
HOST, PORT = "0.0.0.0", 514
syslogconfig = open("forwarder.conf", "r")
rhost = syslogconfig.readline().strip()
syslogconfig.close()
rport = 514


import logging
import socketserver
import socket

logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=LOG_FILE, filemode='a')


class SyslogUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = bytes.decode(self.request[0].strip())
        data2 = ("%s : " % self.client_address[0], str(data))

        #print("%s : " % self.client_address[0], str(data))
        logging.info(data2)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((rhost, rport))
        s.send(self.request[0])
        s.close()

if __name__ == "__main__":
    try:
        server = socketserver.UDPServer((HOST, PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)


    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print("Crtl+C Pressed. Shutting down.")
