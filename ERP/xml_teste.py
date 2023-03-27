import xml.etree.ElementTree as ET
import socket
import time


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

    def run(self):
        try:
            self.data, self.addr = self.sock.recvfrom(self.buffer)
            self.data = self.data.decode(self.format)
            return True
        except socket.error:
            return False

    def read_orders(self):

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

        return self.i

class Order:
    def __init__(self):

        self.nameID = None
        self.number = []
        self.workpiece = []
        self.quantity = []
        self.duedate = []
        self.latepen = []
        self.earlypen = []

class Get_Orders:

    def __init__(self):
        self.orders = []


def read_xml(get_orders):

    start = time.time()
    end = 0

    while end - start < 20:
        if xml.run():

            for i in range(xml.read_orders()):
                order = Order()
                order.nameID = xml.nameID
                order.number = xml.number[i]
                order.workpiece = xml.workpiece[i]
                order.quantity = xml.quantity[i]
                order.duedate = xml.duedate[i]
                order.latepen = xml.latepen[i]
                order.earlypen = xml.earlypen[i]
                get_orders.append(order)
        end = time.time()




# --------------------Inicializations-------------------------------#


xml = Xml("127.0.0.1", 54321)

get_orders = Get_Orders()
read_xml(get_orders)
for i in range(len(get_orders.orders)):
    print(get_orders.orders[i])
