import asyncio
from asyncua import Client
from asyncua import ua
import db

url = "opc.tcp://127.0.0.1:4840/"

Write_bool_value = False

# exemplo de uso da db
get_num_dock, get_p1_dock, get_p2_dock, get_p3_dock, get_p4_dock, get_p5_dock, get_p6_dock, get_p7_dock, get_p8_dock, get_p9_dock = db.get_dock(3)

Write_uint_value = get_p9_dock


async def main():
    async with Client(url=url) as client:
        # Read Boolean Value
        node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Test")
        Read_bool_value = await node.read_value()

        # Read Uint16 Value
        node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[0]")
        Read_uint_value = await node.read_value()

        # Write Boolean Value
        node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Test")
        await node.write_value(ua.Variant(Write_bool_value, ua.VariantType.Boolean))

        # Write Uint16 Value
        node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.vetor[0]")
        await node.write_value(ua.Variant(Write_uint_value, ua.VariantType.UInt16))
        print(Read_bool_value)
        print(Read_uint_value)


if __name__ == "__main__":
    asyncio.run(main())
