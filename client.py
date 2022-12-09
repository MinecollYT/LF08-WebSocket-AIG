import socket # Importiere die socket Bibliothek

# Erstelle einen Socket
def createSocket():
    try:
        global host
        global port
        global s
        host = "localhost" # Setze den Host auf localhost
        port = 9999 # Setze den Port auf 9999
        s = socket.socket() # Erstelle einen Socket
    except socket.error as msg: # Fange Socket Fehler ab
        print("Fehler: " + str(msg))

# Stelle eine Verbindung mit einem Server her (angegeben durch Host und Port)
def setupConnection():
    global host
    global port
    global s
    try:
        s.connect((host, port)) # Stelle die Verbindung her
        print("Verbunden mit dem Server: " + host + ":" + str(port))
    except socket.error as msg: # Fange Socket Fehler ab
        print("Fehler: " + str(msg))

# Sende Daten an den Server
def sendData(data):
    s.send(str.encode(data)) # Sende die Daten (encodiere sie als String)

# Hauptfunktion
def main():
    createSocket()
    setupConnection()
    sendData("Hallo vom Client!")

main()
