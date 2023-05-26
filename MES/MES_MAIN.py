from MES import opcua
from MES import interface as inter
import multiprocessing
from MES import db
import time


def execute_interface():
    inter.setup_interface()


def execute_everything_else(begin_time):
    while True:
        # Get actual time
        now_time = time.time() * 1000.0
        elapsed_time = now_time - begin_time
        db.insert_or_update_time(elapsed_time)

        opcua.run_opcua()


if __name__ == '__main__':
    start_time = time.time() * 1000.0
    db.create_table("orders")
    db.create_table("order_status")
    db.create_table("dailyplan")
    db.create_table("facilities")
    db.create_table("docks")
    db.create_table("day")
    db.create_table("warehouse")
    db.create_table("docks_total")
    db.create_table("facilities_total")
    db.create_table("in_progress_view")
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
