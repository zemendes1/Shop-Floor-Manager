from opcua import Client
from opcua import ua

url = "opc.tcp://DESKTOP-CORDIAL:4840"


def funcao_opc(_node_id, action, _value):
    client = Client(url)
    client.connect()
    client_node = client.get_node(_node_id)

    if action == "read":
        client_node_value = client_node.get_value()
        # print("Value of : " + str(client_node)+ ' : ' + str(client_node_value))
        client.disconnect()
        return client_node_value

    elif action == "write_uint":
        client_node_value = _value
        client_node_input = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.UInt16))
        client_node.set_value(client_node_input)
        client.disconnect()

    elif action == "write_bool":
        client_node_value = _value
        client_node_input = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))
        client_node.set_value(client_node_input)
        client.disconnect()


funcao_opc("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Test", "write_bool", False)

funcao_opc("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[0]", "write_uint", 4)
funcao_opc("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[1]", "write_uint", 4)
funcao_opc("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[2]", "write_uint", 4)
