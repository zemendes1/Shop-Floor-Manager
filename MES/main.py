from MES import opcua
from MES import interface as inter
import multiprocessing


def execute_interface():
    inter.setup_interface()


def execute_everything_else():
    while True:
        opcua.run_opcua()


if __name__ == '__main__':
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
