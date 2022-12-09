import socket # Importiere die socket Bibliothek

# Erstelle einen Socket
def createSocket():
    try:
        global host
        global port
        global s
        host = "" # Setze den Host auf leer
        port = 9999 # Setze den Port auf 9999
        s = socket.socket() # Erstelle einen Socket
    except socket.error as msg: # Fange Socket Fehler ab
        print("Fehler: " + str(msg))

# Binde den Socket an einen Port und horche auf Verbindungen
def runningServer():
    try:
        global host
        global port
        global s
        print("Binde Socket an Port: " + str(port))
        s.bind((host, port)) # Binde den Socket an den Host und Port
        s.listen(5) # Horche auf Verbindungen (maximal 5)
    except socket.error as msg: # Fange Socket Fehler ab
        print("Fehler: " + str(msg) + "\n" + "Wiederhole Vorgang...")
        runningServer()

# Stelle eine Verbindung mit einem Client her (Socket muss horchen)
def setupConnection():
    global s
    global conn
    global address
    conn, address = s.accept() # Stelle die Verbindung her und speichere Client-Informationen
    print("Verbindung hergestellt mit: " + address[0] + ":" + str(address[1]))

# Empfange Daten vom Client
def receiveData():
    data = conn.recv(1024).decode() # Empfange Daten (maximal 1024 Bytes) und decodiere sie
    return data

# Hauptfunktion
def main():
    createSocket()
    runningServer()
    setupConnection()
    data = receiveData()
    print("Empfangene Daten: " + data)

main()
