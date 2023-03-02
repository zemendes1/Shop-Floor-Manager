import asyncio
from asyncua import Client
from asyncua import ua

url = "opc.tcp://127.0.0.1:4840/"


async def main():
    async with Client(url=url) as client:
        while True:
            # Read Boolean Value
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Test")
            bool_value = await node.read_value()

            # Write Boolean Value
            new_value = not bool_value
            await node.write_value(ua.Variant(new_value, ua.VariantType.Boolean))

            # Read Uint16 Value
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[0]")
            uint_value = await node.read_value()

            # Write Uint16 Value
            new_value = uint_value + 1
            await node.write_value(ua.Variant(new_value, ua.VariantType.UInt16))


if __name__ == "__main__":
    asyncio.run(main())
