from ERP import interfaceErp
import multiprocessing
from MES import db
from ERP import MPS
from ERP import receive_xml


def execute_interface():
    interfaceErp.setup_interface()


def execute_everything_else():
    while True:
        pass
        MPS.continuous_processing()
        receive_xml.run_xml()


if __name__ == '__main__':
    db.db_startup()
    # add this check and freeze_support() call
    multiprocessing.freeze_support()

    # create processes for each function
    process1 = multiprocessing.Process(target=execute_interface)
    process2 = multiprocessing.Process(target=execute_everything_else)

    # start the processes
    process1.start()
    process2.start()

    # wait for the processes to finish
    process1.join()
    process2.join()
