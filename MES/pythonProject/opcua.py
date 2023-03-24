import main as Mn
import asyncio
from asyncua import Client
from asyncua import ua


url = "opc.tcp://127.0.0.1:4840/"


async def main():
    print(Mn.Out_bool_value)
    print(Mn.Out_uint_value)
    async with Client(url=url) as client:
        while True:
            # Read Boolean Value
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Test")
            Mn.In_bool_value = await node.read_value()

            # Read Uint16 Value
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[0]")
            Mn.In_uint_value = await node.read_value()

            # Write Boolean Value
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Test")
            await node.write_value(ua.Variant(Mn.Out_bool_value, ua.VariantType.Boolean))

            # Write Uint16 Value
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[0]")
            await node.write_value(ua.Variant(Mn.Out_uint_value, ua.VariantType.UInt16))


if __name__ == "__main__":
    asyncio.run(main())
