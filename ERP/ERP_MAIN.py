import multiprocessing
from ERP import receive_xml
from ERP import interfaceErp
from ERP import MPS
from DB import db


def execute_xml():
    while True:
        receive_xml.run_xml()


def execute_interface():
    interfaceErp.setup_interface()


def execute_mps():
    while True:
        MPS.continuous_processing()


if __name__ == '__main__':

    db.create_table("orders")
    db.create_table("order_status")
    db.create_table("dailyplan")
    db.create_table("facilities")
    db.create_table("docks")
    db.create_table("day")
    db.create_table("warehouse")
    db.create_table("docks_total")
    db.create_table("facilities_total")
    db.create_table("unloaded")
    db.create_table("arrivals")
    # add this check and freeze_support() call
    multiprocessing.freeze_support()

    # create processes for each function
    process1 = multiprocessing.Process(target=execute_xml)
    process2 = multiprocessing.Process(target=execute_interface)
    process3 = multiprocessing.Process(target=execute_mps)

    # start the processes
    process1.start()
    process2.start()
    process3.start()

    # wait for the processes to finish
    process1.join()
    process2.join()
    process3.join()
