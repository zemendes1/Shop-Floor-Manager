def assign_machines(string):
    """
    Assigns machines to each transformation based on the given tools and time constraints.

    Args:
        string (str): A string of the format "x, x, x, x" where each 'x' represents a tool mapping.

    Returns:
        str: A string representing the assigned machines for each transformation in the format "x, x, x, x".
             If the input string is None, returns None.
    """

    # If the input string is None or empty, return None
    if string is None or string == "":
        return "0, 0, 0, 0"

    non_assigned_machines = ['1', '2', '3', '4']
    # Define the mappings from source to target tools
    mappings_tool = {
        'P3_from_P2': "T2",
        'P4_from_P2': "T3",
        'P5_from_P9': "T4",
        'P6_from_P1': "T1",
        'P6_from_P3': "T1",
        'P7_from_P4': "T4",
        'P7_from_P9': "T4",
        'P8_from_P6': "T3",
        'P9_from_P7': "T3",
        'null': None
    }

    # Define the mappings from transformation to time taken
    mappings_time = {
        'P3_from_P2': 10,
        'P4_from_P2': 10,
        'P5_from_P9': 15,
        'P6_from_P1': 20,
        'P6_from_P3': 20,
        'P7_from_P4': 10,
        'P7_from_P9': 10,
        'P8_from_P6': 30,
        'P9_from_P7': 10,
        'null': None
    }

    # Define the available tools for each machine
    machines_tools = {
        1: ['T1', 'T2', 'T3'],
        2: ['T1', 'T3', 'T4'],
        3: ['T2', 'T3', 'T4'],
        4: ['T1', 'T3', 'T4']
    }

    # Split the input string into individual transformations
    transformations = string.split(', ')

    # Initialize an empty list to store the assigned machines
    assigned_machines = []

    # Initialize a set to keep track of assigned machines
    assigned_set = set()

    # Iterate over each transformation and assign a machine
    for transformation in transformations:
        if transformation == "null":
            assigned_machines.append("0")
            continue

        # Get the required tool for the transformation
        required_tool = mappings_tool[transformation]

        # Get the time taken for the transformation
        time_taken = mappings_time[transformation]

        # Initialize a variable to store the assigned machine
        assigned_machine = None

        # Iterate over each machine and check if the required tool is available and not assigned yet
        for machine, tools in machines_tools.items():
            if required_tool in tools and machine not in assigned_set:
                # Check if the machine is not assigned yet and the time constraint is met
                if assigned_machine is None or (time_taken >= 15 and machine >= 3):
                    assigned_machine = machine

        # If no machine is assigned, assign the first available machine
        if assigned_machine is None:
            possible_machines = []
            # possible machines for the problematic trasnformation
            for machine, tools in machines_tools.items():
                if required_tool in tools:
                    possible_machines.append(machine)

            for machine, tools in machines_tools.items():
                if machine in possible_machines:
                    index = assigned_machines.index(str(machine))

                    required_tool_alternative = mappings_tool[transformations[index]]

                    for machines_possibles, possible_tools in machines_tools.items():

                        if required_tool_alternative in possible_tools:

                            if str(machines_possibles) in non_assigned_machines:
                                assigned_machines[index] = str(machines_possibles)

                                assigned_machine = machine

                                non_assigned_machines.append(str(machine))
                                non_assigned_machines.remove(str(machines_possibles))
                                break

        # Add the assigned machine to the set
        assigned_set.add(assigned_machine)

        # Add the assigned machine to the list
        assigned_machines.append(str(assigned_machine))
        non_assigned_machines.remove(str(assigned_machine))

    # Join the assigned machines into a string
    assigned_string = ', '.join(assigned_machines)

    return assigned_string