import asyncio
from asyncua import Client
from asyncua import ua
import db

import PieceTransformer as Piece
import Transformer_to_Piece as Transformer
from MES import dock_transformer
from MES import Assign_Machines


async def main():
    url = "opc.tcp://127.0.0.1:4840/"

    delivery = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    order1, order2, order3, order4 = 0, 0, 0, 0
    machine_order1, machine_order2, machine_order3, machine_order4 = 0, 0, 0, 0

    # Get daily Plan
    current_day = db.get_day()
    daily_plan = db.get_daily_plan(current_day)
    if daily_plan is not None:
        get_date, get_working_orders, get_delivery_orders, get_p1_tobuy, get_p2_tobuy, get_p1_arriving, get_p2_arriving = daily_plan

        order1, order2, order3, order4 = get_working_orders.split(', ')
        order1 = Piece.define_vector(order1)
        order2 = Piece.define_vector(order2)
        order3 = Piece.define_vector(order3)
        order4 = Piece.define_vector(order4)

        machine_order1, machine_order2, machine_order3, machine_order4 = Assign_Machines.assign_machines(get_working_orders).split(', ')
        machine_order1 = int(machine_order1)
        machine_order2 = int(machine_order2)
        machine_order3 = int(machine_order3)
        machine_order4 = int(machine_order4)

        delivery1, delivery2, delivery3, delivery4, delivery5, delivery6, delivery7, delivery8 = get_delivery_orders.split(
            ', ')
        delivery[1] = dock_transformer.define_dock(delivery1)
        delivery[2] = dock_transformer.define_dock(delivery2)
        delivery[3] = dock_transformer.define_dock(delivery3)
        delivery[4] = dock_transformer.define_dock(delivery4)
        delivery[5] = dock_transformer.define_dock(delivery5)
        delivery[6] = dock_transformer.define_dock(delivery6)
        delivery[7] = dock_transformer.define_dock(delivery7)
        delivery[8] = dock_transformer.define_dock(delivery8)

    machine_times = []
    pecas_armazem = []
    unloaded = []
    machine_transforms = []
    for i in range(5):
        machine_transforms.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

    async with Client(url=url) as client:
        # Write current day
        node = client.get_node(
            "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.dia_atual")
        await node.write_value(ua.Variant(current_day, ua.VariantType.Int16))

        if order1 != 0:
            # Write Working Order #1 of the day
            for i in range(1, 3):
                for j in range(1, 3):
                    node = client.get_node(
                        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Ordem_Producao1[{}][{}]".format(i, j))
                    await node.write_value(ua.Variant(order1[i - 1][j - 1], ua.VariantType.Int16))
            # Write day
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Ordem_Producao1[3][1]")
            await node.write_value(ua.Variant(current_day, ua.VariantType.Int16))
            # Write Machine
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Ordem_Producao1[3][2]")
            await node.write_value(ua.Variant(machine_order1, ua.VariantType.Int16))

        if order2 != 0:
            # Write Working Order #2 of the day
            for i in range(1, 3):
                for j in range(1, 3):
                    node = client.get_node(
                        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Ordem_Producao2[{}][{}]".format(i, j))
                    await node.write_value(ua.Variant(order2[i - 1][j - 1], ua.VariantType.Int16))
            # Write day
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Ordem_Producao2[3][1]")
            await node.write_value(ua.Variant(current_day, ua.VariantType.Int16))
            # Write Machine
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Ordem_Producao2[3][2]")
            await node.write_value(ua.Variant(machine_order2, ua.VariantType.Int16))

        if order3 != 0:
            # Write Working Order #3 of the day
            for i in range(1, 3):
                for j in range(1, 3):
                    node = client.get_node(
                        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Ordem_Producao3[{}][{}]".format(i, j))
                    await node.write_value(ua.Variant(order3[i - 1][j - 1], ua.VariantType.Int16))
            # Write day
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Ordem_Producao3[3][1]")
            await node.write_value(ua.Variant(current_day, ua.VariantType.Int16))
            # Write Machine
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Ordem_Producao3[3][2]")
            await node.write_value(ua.Variant(machine_order3, ua.VariantType.Int16))

        if order4 != 0:
            # Write Working Order #4 of the day
            for i in range(1, 3):
                for j in range(1, 3):
                    node = client.get_node(
                        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Ordem_Producao4[{}][{}]".format(i, j))
                    await node.write_value(ua.Variant(order4[i - 1][j - 1], ua.VariantType.Int16))
            # Write day
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Ordem_Producao4[3][1]")
            await node.write_value(ua.Variant(current_day, ua.VariantType.Int16))
            # Write Machine
            node = client.get_node("ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Ordem_Producao4[3][2]")
            await node.write_value(ua.Variant(machine_order4, ua.VariantType.Int16))

        if delivery[1] != 0:
            # Write Deliveries of the day
            for i in range(1, 9):
                for j in range(1, 3):
                    node = client.get_node(
                        "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Delivery_Day[{}][{}]".format(i, j))
                    await node.write_value(ua.Variant(delivery[i][j - 1], ua.VariantType.Int16))
            # Write day
            node = client.get_node(
                "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Delivery_Day[9][1]".format(i, j))
            await node.write_value(ua.Variant(current_day, ua.VariantType.Int16))

        # Ler Tempo de Funcionamento de cada máquina
        for i in range(1, 5):
            node = client.get_node(
                "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.Tempo_Operacao_Maq[{}]".format(i))
            machine_times.append(await node.read_value())

        # Ler Peças do Armazém
        for i in range(1, 10):
            node = client.get_node(
                "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.npecas_armazem[{}]".format(i))
            pecas_armazem.append(await node.read_value())

        # Ler Peças do Unloaded Pieces
        for i in range(1, 10):
            node = client.get_node(
                "ns=4;s=|var|CODESYS Control Win V3 x64.Application.GVL.pecas_entregues[{}]".format(i))
            unloaded.append(await node.read_value())

        db.update_unloaded(unloaded[0], unloaded[1], unloaded[2], unloaded[3], unloaded[4],
                           unloaded[5], unloaded[6], unloaded[7], unloaded[8])

        db.update_warehouse(pecas_armazem[0], pecas_armazem[1], pecas_armazem[2], pecas_armazem[3], pecas_armazem[4],
                            pecas_armazem[5], pecas_armazem[6], pecas_armazem[7], pecas_armazem[8])

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

        db.update_facility(1, machine1_p1, machine1_p2, machine1_p3, machine1_p4, machine1_p5, machine1_p6, machine1_p7,
                           machine1_p8, machine1_p9,
                           machine1_time)
        db.update_facility(2, machine2_p1, machine2_p2, machine2_p3, machine2_p4, machine2_p5, machine2_p6, machine2_p7,
                           machine2_p8, machine2_p9,
                           machine2_time)
        db.update_facility(3, machine3_p1, machine3_p2, machine3_p3, machine3_p4, machine3_p5, machine3_p6, machine3_p7,
                           machine3_p8, machine3_p9,
                           machine3_time)
        db.update_facility(4, machine4_p1, machine4_p2, machine4_p3, machine4_p4, machine4_p5, machine4_p6, machine4_p7,
                           machine4_p8, machine4_p9,
                           machine4_time)


# if __name__ == "__main__":
def run_opcua():
    asyncio.run(main())
