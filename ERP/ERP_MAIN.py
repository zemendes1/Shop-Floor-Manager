import multiprocessing
from ERP import receive_xml
from ERP import interfaceErp
from ERP import MPS
from MES import db


def execute_xml():
    while True:
        receive_xml.run_xml()


def execute_interface():
    interfaceErp.setup_interface()


def execute_mps():
    while True:
        MPS.continuous_processing()


if __name__ == '__main__':
    db.db_startup()
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
