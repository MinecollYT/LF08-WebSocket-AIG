class Computer():

    powerSupply = ""
    _cpu = ""
    _cpuSpeed = 0.0
    _ram = 0
    _os = ""
    _ip = ""

    def __init__(self, powerSupply, cpu, cpuSpeed, ram, os, ip):
        self.powerSupply = powerSupply
        self.cpu = cpu
        self.cpuSpeed = cpuSpeed
        self.ram = ram
        self.os = os
        self.ip = ip

    def getInfo(self):
        print(f"Hardwareinformationen: Netzteil: {self.powerSupply}; CPU: {self.cpu}; CPU-Takt: {self.cpuSpeed} GHz; RAM: {self.ram} GB; Betriebssystem: {self.os}; IP-Adresse: {self.ip}")