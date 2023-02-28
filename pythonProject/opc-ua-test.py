from opcua import Client
from opcua import ua
import cryptography


def read_input_value(_node_id):
    url = "opc.tcp://DESKTOP-CORDIAL:4840"
    client = Client(url)
    client.connect()
    clientNode = client.get_node(_node_id)
    clientNodeValue = clientNode.get_value()
    # print("Value of : " + str(clientNode)+ ' : ' + str(clientNodeValue))
    return clientNodeValue
    # client.disconnect()


def write_int_value(_node_id, _value):
    url = "opc.tcp://DESKTOP-CORDIAL:4840"
    client = Client(url)
    client.connect()
    clientNode = client.get_node(_node_id)
    clientNodeValue = _value
    clientNodeInput = ua.DataValue(ua.Variant(clientNodeValue, ua.VariantType.UInt16))
    clientNode.set_value(clientNodeInput)
    client.disconnect()


def write_bool_value(_node_id, _value):
    url = "opc.tcp://DESKTOP-CORDIAL:4840"
    client = Client(url)
    client.connect()
    clientNode = client.get_node(_node_id)
    clientNodeValue = _value
    clientNodeInput = ua.DataValue(ua.Variant(clientNodeValue, ua.VariantType.Boolean))
    clientNode.set_value(clientNodeInput)
    client.disconnect()

write_bool_value("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Test",True)

# write_int_value("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[0]",4)
# write_int_value("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[1]",4)
# write_int_value("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[2]",4)
