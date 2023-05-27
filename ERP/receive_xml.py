import xml.etree.ElementTree as et
import socket
import MES.db


class Xml:

    def __init__(self, identificador, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((identificador, port))

        # Instruções de Apresentação
        # self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.sock.bind(('', 4321))  # binds to all interfaces (insecure)
        # OR
        # self.sock.bind(('0.0.0.0', 4321)) # binds to all interfaces (insecure)

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

        self.nameID = None
        self.number = []
        self.workpiece = []
        self.quantity = []
        self.duedate = []
        self.latepen = []
        self.earlypen = []

        self.root = et.fromstring(self.data)

        self.nameID = self.root.find("Client").attrib["NameId"]

        for order in self.root.findall("Order"):
            self.number.append(int(order.attrib["Number"]))
            self.workpiece.append(str(order.attrib["WorkPiece"]))
            self.quantity.append(int(order.attrib["Quantity"]))
            self.duedate.append(int(order.attrib["DueDate"]))
            self.latepen.append(int(order.attrib["LatePen"]))
            self.earlypen.append(int(order.attrib["EarlyPen"]))
            self.i += 1
        return self.nameID, self.number, self.workpiece, self.quantity, self.duedate, self.latepen, self.earlypen


def run_xml():
    xml = Xml("127.0.0.1", 54321)
    xml.xml2string()
    nameID, number, workpiece, quantity, duedate, latepen, earlypen = xml.get_order()
    for i in range(len(number)):
        MES.db.add_order(number[i], nameID, number[i], workpiece[i], quantity[i], duedate[i], latepen[i],
                         earlypen[i], '{}', 'TBD', 0, 0)
