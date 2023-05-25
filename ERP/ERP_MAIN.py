from ERP import interfaceErp
import multiprocessing
from MES import db
from ERP import MPS
from ERP import receive_xml


def execute_everything_else():
    receive_xml.run_xml()


def execute_interface():
    interfaceErp.setup_interface()


def execute_mps():
    # MPS.continuous_processing()
    pass


if __name__ == '__main__':
    db.db_startup()
    # add this check and freeze_support() call
    multiprocessing.freeze_support()

    # create processes for each function
    process3 = multiprocessing.Process(target=execute_everything_else)
    process1 = multiprocessing.Process(target=execute_interface)
    process2 = multiprocessing.Process(target=execute_mps)

    # start the processes
    process1.start()
    process2.start()
    process3.start()

    # wait for the processes to finish
    process1.join()
    process2.join()
    process3.join()
