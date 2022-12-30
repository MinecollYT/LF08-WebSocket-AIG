import computer
import socket


class Client(computer.Computer):

    def createSocket(self, remoteIP, remotePort):
        # Socket erstellen
        self.__remoteIP = remoteIP
        self.__remotePort = remotePort
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Verbindung zum Server herstellen
            self.client_socket.connect((self.__remoteIP, self.__remotePort))

            # Informationen für den Benutzer
            print(f"Verbunden mit {self.__remoteIP}:{self.__remotePort}")

            # Variable connected auf True setzen
            self.connected = True
        except ConnectionRefusedError:
            print("Verbindungsaufbau abgelehnt, da Server nicht gestartet ist.")
            self.client_socket.close()

            # Variable connected auf False setzen
            self.connected = False

    def sendData(self):
        # Falls Verbindung zum Server hergestellt wurde
        if self.connected:
            # Nachrichten senden, bis "shutdown" gesendet wurde
            while True:
                message = input("Nachricht eingeben: ")
                self.client_socket.send(message.encode())

                # Antwort vom Server empfangen
                response = self.client_socket.recv(1024).decode()
                print(f"Antwort vom Server: {response}")

                if message == "shutdown":
                    print("SHUTDOWN BEFEHL ERHALTEN.. BEENDE DIENST.")
                    print("SHUTDOWN BEFEHL AN SERVER GESCHICKT..")
                    break

        # Socket schließen
        self.client_socket.close()


# Client erstellen, nur Testwerte
client = Client("500W", "Intel Core i7", 3.5, 16, "Windows 10", "192.168.0.3")

# Informationen über den Client ausgeben
client.getInfo()

# Socket erstellen
client.createSocket("127.0.0.1", 1337)

# Nachrichten senden
client.sendData()