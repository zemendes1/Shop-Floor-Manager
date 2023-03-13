import xml.etree.ElementTree as ET
import socket


class Xml:

    def __init__(self, id, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((id, port))

        self.buffer = 1024
        self.format = "utf-8"
        self.i = 0
        self.nameID = None
        self.root = None
        self.data = None
        self.addr = None
        self.number = []
        self.workpiece = []
        self.quantity = []
        self.duedate = []
        self.latepen = []
        self.earlypen = []

    def xml2string(self):
        try:
            self.data, self.addr = self.sock.recvfrom(self.buffer)
            self.data = self.data.decode(self.format)
            return True
        except socket.error:
            return False

    def get_order(self):

        self.root = ET.fromstring(self.data)

        self.nameID = self.root.find("Client").attrib["NameId"]

        # print(self.nameID)

        for order in self.root.findall("Order"):
            self.number.append(int(order.attrib["Number"]))
            self.workpiece.append(str(order.attrib["WorkPiece"]))
            self.quantity.append(int(order.attrib["Quantity"]))
            self.duedate.append(int(order.attrib["DueDate"]))
            self.latepen.append(int(order.attrib["LatePen"]))
            self.earlypen.append(int(order.attrib["EarlyPen"]))
            self.i += 1


xml = Xml("127.0.0.1", 54321)
xml.xml2string()
xml.get_order()
