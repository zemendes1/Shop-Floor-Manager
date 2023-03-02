"""
import asyncio
from asyncua import Client

url = "opc.tcp://DESKTOP-CORDIAL:4840"
namespace = ["0:Objects",
             "2:DeviceSet",
             "4:CODESYS Control Win V3 ×64",
             "3:Resources",
             "4:Application",
             "3:GlobalVars",
             "4:GVL",
             "Test"]


async def main():
    print(f"Connecting to {url} ...")
    async with Client(url=url) as client:

        # Find the namespace index
        nsidx = await client.get_namespace_index(namespace)
        print(f"Namespace Index for '{namespace}': {nsidx}")

        # Get the variable node for read / write
        var = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:MyObject", f"{nsidx}:MyVariable"]
        )
        value = await var.read_value()
        print(f"Value of MyVariable ({var}): {value}")

        new_value = True
        # value - 50
        print(f"Setting value of MyVariable to {new_value} ...")
        await var.write_value(new_value)

        # Calling a method
        res = await client.nodes.objects.call_method(f"{nsidx}:ServerMethod", 5)
        print(f"Calling ServerMethod returned {res}")


if __name__ == "__main__":
    asyncio.run(main())
"""

import asyncio

from asyncua import Client

url = "opc.tcp://localhost:4840/freeopcua/server/"
namespace = "http://examples.freeopcua.github.io"


async def main():

    print(f"Connecting to {url} ...")
    async with Client(url=url) as client:
        # Find the namespace index
        nsidx = await client.get_namespace_index(namespace)
        print(f"Namespace Index for '{namespace}': {nsidx}")

        # Get the variable node for read / write
        var = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:MyObject", f"{nsidx}:MyVariable"]
        )
        value = await var.read_value()
        print(f"Value of MyVariable ({var}): {value}")

        new_value = value - 50
        print(f"Setting value of MyVariable to {new_value} ...")
        await var.write_value(new_value)

        # Calling a method
        res = await client.nodes.objects.call_method(f"{nsidx}:ServerMethod", 5)
        print(f"Calling ServerMethod returned {res}")


if __name__ == "__main__":
    asyncio.run(main())