import socket
import computer


class Server(computer.Computer):

    def createSocket(self, remoteIP, remotePort):
        # Socket erstellen
        self.__remoteIP = remoteIP
        self.__remotePort = remotePort
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Socket an IP-Adresse und Port binden
        self.server_socket.bind((self.__remoteIP, self.__remotePort))

        # Information für den Benutzer
        print(f"Server läuft auf {self.__remoteIP}:{self.__remotePort}")

    def runningServer(self):
        # Server starten und auf eingehende Verbindungen warten
        self.server_socket.listen()

        # Informationen für den Benutzer
        print("Server wartet auf eingehende Verbindungen...")

        # Verbindung akzeptieren und mit Client kommunizieren
        conn, addr = self.server_socket.accept()
        with conn:
            print(f"Eingehende Verbindung von {addr[0]}:{addr[1]}")
            while True:
                # Nachricht vom Client empfangen
                data = conn.recv(1024)
                client_message = data.decode()
                print(f"Nachricht von Client: {client_message}")

                # Nachricht an Client senden
                conn.send(f"Nachricht '{client_message}' mit {len(client_message.encode('utf-8'))} Byte empfangen\n".encode())

                if client_message == "shutdown":
                    print("SHUTDOWN BEFEHL ERHALTEN.. BEENDE DIENST.")
                    conn.send("SERVER HAT SHUTDOWN BEFEHL ERHALTEN.. BEENDE DIENST.".encode())
                    break

        # Socket schließen
        self.server_socket.close()


# Server erstellen, nur Testwerte
server = Server("1000W", "AMD EPYC 7763", 2.45, 512, "Windows Server 2019", "192.168.0.2")

# Informationen über den Server ausgeben
server.getInfo()

# Socket erstellen
server.createSocket("127.0.0.1", 1337)

# Server starten
server.runningServer()