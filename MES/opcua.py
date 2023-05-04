import asyncio
from asyncua import Client
from asyncua import ua
import db
import PieceTransformer as Piece
import Transformer_to_Piece as Transformer

url = "opc.tcp://127.0.0.1:4840/"

Write_bool_value = False

# Get daily Plan
daily_plan = db.get_daily_plan(db.get_day())
if daily_plan is not None:
    get_date, get_purchase_orders, get_delivery_orders, get_p1_tobuy, get_p2_tobuy = daily_plan
    order1, order2, order3, order4 = get_delivery_orders.split(', ')
    order1 = Piece.define_vector(order1)
    order2 = Piece.define_vector(order2)
    order3 = Piece.define_vector(order3)
    order4 = Piece.define_vector(order4)
else:
    order1 = 0
    order2 = 0
    order3 = 0
    order4 = 0


async def main():
    machine_times = []
    machine_transforms = []
    for i in range(5):
        machine_transforms.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

    async with Client(url=url) as client:
        if order1 != 0:
            # Write Order #1 of the day
            for i in range(1, 6):
                for j in range(1, 3):
                    node = client.get_node(
                        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.MES_TESTE1[{}][{}]".format(i, j))
                    await node.write_value(ua.Variant(order1[i - 1][j - 1], ua.VariantType.Int16))

        if order2 != 0:
            # Write Order #2 of the day
            for i in range(1, 6):
                for j in range(1, 3):
                    node = client.get_node(
                        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.MES_TESTE2[{}][{}]".format(i, j))
                    await node.write_value(ua.Variant(order2[i - 1][j - 1], ua.VariantType.Int16))

        if order3 != 0:
            # Write Order #3 of the day
            for i in range(1, 6):
                for j in range(1, 3):
                    node = client.get_node(
                        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.MES_TESTE3[{}][{}]".format(i, j))
                    await node.write_value(ua.Variant(order3[i - 1][j - 1], ua.VariantType.Int16))

        if order4 != 0:
            # Write Order #4 of the day
            for i in range(1, 6):
                for j in range(1, 3):
                    node = client.get_node(
                        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.MES_TESTE4[{}][{}]".format(i, j))
                    await node.write_value(ua.Variant(order4[i - 1][j - 1], ua.VariantType.Int16))

        # Ler Tempo de Funcionamento de cada máquina
        for i in range(1, 5):
            node = client.get_node(
                "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Tempo_Operacao_Maq[{}]".format(i))
            machine_times.append(await node.read_value())

        machine1_time, machine2_time, machine3_time, machine4_time = machine_times

        # Ler Numero de Pecas_Produzidas_Maq
        for i in range(1, 5):
            for j in range(1, 9):
                node = client.get_node(
                    "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Pecas_Produzidas_Maq[{}][{}]".format(i, j))
                machine_transforms[i][j] = await node.read_value()

        machine1_p1, machine1_p2, machine1_p3, machine1_p4, machine1_p5, machine1_p6, machine1_p7, machine1_p8, machine1_p9 = Transformer.n_of_pieces(
            machine_transforms[1])
        machine2_p1, machine2_p2, machine2_p3, machine2_p4, machine2_p5, machine2_p6, machine2_p7, machine2_p8, machine2_p9 = Transformer.n_of_pieces(
            machine_transforms[2])
        machine3_p1, machine3_p2, machine3_p3, machine3_p4, machine3_p5, machine3_p6, machine3_p7, machine3_p8, machine3_p9 = Transformer.n_of_pieces(
            machine_transforms[3])
        machine4_p1, machine4_p2, machine4_p3, machine4_p4, machine4_p5, machine4_p6, machine4_p7, machine4_p8, machine4_p9 = Transformer.n_of_pieces(
            machine_transforms[4])

        db.update_facility(1, machine1_p1, machine1_p2, machine1_p3, machine1_p4, machine1_p5, machine1_p6, machine1_p7, machine1_p8, machine1_p9,
                           machine1_time)
        db.update_facility(2, machine2_p1, machine2_p2, machine2_p3, machine2_p4, machine2_p5, machine2_p6, machine2_p7, machine2_p8, machine2_p9,
                           machine2_time)
        db.update_facility(3, machine3_p1, machine3_p2, machine3_p3, machine3_p4, machine3_p5, machine3_p6, machine3_p7, machine3_p8, machine3_p9,
                           machine3_time)
        db.update_facility(4, machine4_p1, machine4_p2, machine4_p3, machine4_p4, machine4_p5, machine4_p6, machine4_p7, machine4_p8, machine4_p9,
                           machine4_time)


# if __name__ == "__main__":
def run_opcua():
    asyncio.run(main())
