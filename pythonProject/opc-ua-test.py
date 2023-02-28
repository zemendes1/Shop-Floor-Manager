from opcua import Client
from opcua import ua
import cryptography

url = "opc.tcp://DESKTOP-CORDIAL:4840"

def read_input_value(_node_id):
    client = Client(url)
    client.connect()
    client_node = client.get_node(_node_id)
    client_node_value = client_node.get_value()
    # print("Value of : " + str(client_node)+ ' : ' + str(client_node_value))
    return client_node_value
    # client.disconnect()


def write_int_value(_node_id, _value):
    client = Client(url)
    client.connect()
    client_node = client.get_node(_node_id)
    client_node_value = _value
    client_node_input = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.UInt16))
    client_node.set_value(client_node_input)
    client.disconnect()


def write_bool_value(_node_id, _value):
    client = Client(url)
    client.connect()
    client_node = client.get_node(_node_id)
    client_node_value = _value
    client_node_input = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))
    client_node.set_value(client_node_input)
    client.disconnect()


write_bool_value("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Test", True)

# write_int_value("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[0]",4)
# write_int_value("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[1]",4)
# write_int_value("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[2]",4)
