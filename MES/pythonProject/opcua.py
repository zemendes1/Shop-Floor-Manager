import asyncio
from asyncua import Client
from asyncua import ua
import db
import PieceTransformer as PT

url = "opc.tcp://127.0.0.1:4840/"

Write_bool_value = False

# exemplo de uso da db e piece trasnformer
get_date, get_purchase_orders, get_delivery_orders, get_p1_tobuy, get_p2_tobuy = db.get_daily_plan(7)
order1, order2, order3, order4 = get_delivery_orders.split(', ')
order1 = PT.define_vector(order1)
order2 = PT.define_vector(order2)
order3 = PT.define_vector(order3)
order4 = PT.define_vector(order4)

Write_uint_value = 0  # get_delivery_orders


async def main():
    async with Client(url=url) as client:

        # Write Order #1 of the day
        for i in range(1, 6):
            for j in range(1, 3):
                node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.MES_TESTE1[{}][{}]".format(i, j))
                await node.write_value(ua.Variant(order1[i - 1][j - 1], ua.VariantType.Int16))

        """"
        # Write Order #3 of the day
        for i in range(1, 6):
            for j in range(1, 3):
                node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.MES_TESTE3[{}][{}]".format(i, j))
                await node.write_value(ua.Variant(order3[i - 1][j - 1], ua.VariantType.Int16))
                
        # Write Order #2 of the day
        for i in range(1, 6):
            for j in range(1, 3):
                node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.MES_TESTE2[{}][{}]".format(i, j))
                await node.write_value(ua.Variant(order2[i - 1][j - 1], ua.VariantType.Int16))
                
        # Write Order #4 of the day
        for i in range(1, 6):
            for j in range(1, 3):
                node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.MES_TESTE4[{}][{}]".format(i, j))
                await node.write_value(ua.Variant(order4[i - 1][j - 1], ua.VariantType.Int16))                
        """


if __name__ == "__main__":
    asyncio.run(main())
