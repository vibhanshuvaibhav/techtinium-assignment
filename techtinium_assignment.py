#techtinium assignment

# get new york calculations
def get_new_york_details(capacity_required, hours):
    # get the required inputs
    capacity_units_required = capacity_required
    hours_required = hours
    
    # capacity dictionary
    capacities = {"Large" : 10, "XLarge" : 20, "2XLarge" : 40, "4XLarge" : 80, "8XLarge" : 160, "10XLarge" : 320 }
    
    # new york costs
    new_york_costs = {"Large" : 120, "XLarge" : 230, "2XLarge" : 450, "4XLarge" : 774, "8XLarge" : 1400, "10XLarge" : 2820 }
    
    # multiply costs by hours required
    # this will get cost of each for the required hours
    for key in new_york_costs.keys():
        new_york_costs[key] = new_york_costs[key] * hours_required
    
    # marker and min cost
    marker = [0, 0, 0, 0, 0, 0]
    marker_values = ["Large", "XLarge", "2XLarge", "4XLarge", "8XLarge", "10XLarge"]
    min_cost = 0
    
    # 2D array
    bottom_up_ar = []
    
    # create upper row
    units_list = [0]
    for index in range(0, capacity_units_required + 10, 10):
        units_list.append(index)
    
    # cost list for only large machine
    large_cost_list = [10]
    for index in range(len(units_list) - 1):
        large_cost_list.append(new_york_costs["Large"] * index)
    
    # create initial 2D array
    bottom_up_ar.append(units_list)
    bottom_up_ar.append(large_cost_list)
    bottom_up_ar.append([20])
    bottom_up_ar.append([40])
    bottom_up_ar.append([80])
    bottom_up_ar.append([160])
    bottom_up_ar.append([320])
    for upper_index in range(2, len(bottom_up_ar)):
        for lower_index in range(len(units_list) - 1):
            bottom_up_ar[upper_index].append(0)
    
    # index finder
    def index_finder(number):
        for index in range(len(units_list)):
            if units_list[index] == number:
                return index
    
    # finding min cost starting index 2
    for upper_index in range(2, len(bottom_up_ar)):
        base_value = 0
        if upper_index == 2:
            base_value = new_york_costs["XLarge"]
        elif upper_index == 3:
            base_value = new_york_costs["2XLarge"]
        elif upper_index == 4:
            base_value = new_york_costs["4XLarge"]
        elif upper_index == 5:
            base_value = new_york_costs["8XLarge"]
        elif upper_index == 6:
            base_value = new_york_costs["10XLarge"]
        for lower_index in range(2, len(bottom_up_ar[upper_index])):
            if bottom_up_ar[0][lower_index] < bottom_up_ar[upper_index][0]:
                bottom_up_ar[upper_index][lower_index] = bottom_up_ar[upper_index - 1][lower_index]
            elif bottom_up_ar[0][lower_index] == bottom_up_ar[upper_index][0]:
                bottom_up_ar[upper_index][lower_index] = base_value
            else:
                bottom_up_ar[upper_index][lower_index] = min(bottom_up_ar[upper_index - 1][lower_index], base_value + bottom_up_ar[upper_index][index_finder(bottom_up_ar[0][lower_index] - bottom_up_ar[upper_index][0])])
    
    # finding the machine combination
    min_cost = bottom_up_ar[len(bottom_up_ar) - 1][-1]
    current_row = len(bottom_up_ar) - 1
    current_column = -1
    
    while((current_column != 1 or current_column != 0) and current_row >= 1):
        if bottom_up_ar[current_row][current_column] == bottom_up_ar[current_row - 1][current_column]:
            current_row = current_row - 1
        else:
            marker[current_row - 1] += 1
            last_column = index_finder(bottom_up_ar[0][current_column] - bottom_up_ar[current_row][0])
            if last_column == 0:
                break
            else:
                current_column = last_column
    
    # generating result
    machine_list = []
    for index in range(len(marker)):
        if marker[index] != 0:
            number_machine_pair = (marker_values[index], marker[index])
            machine_list.append(number_machine_pair)
    machine_list.sort()
    result = { "region" : "New York", "total_cost" : "$"+str(min_cost), "machines" : machine_list }
    return result

# get india calculations
def get_india_details(capacity_required, hours):
    # get the required inputs
    capacity_units_required = capacity_required
    hours_required = hours
    
    # capacity dictionary
    capacities = {"Large" : 10, "2XLarge" : 40, "4XLarge" : 80, "8XLarge" : 160, "10XLarge" : 320 }
    
    # new york costs
    india_costs = {"Large" : 140, "2XLarge" : 413, "4XLarge" : 890, "8XLarge" : 1300, "10XLarge" : 2970 }
    
    # multiply costs by hours required
    # this will get cost of each for the required hours
    for key in india_costs.keys():
        india_costs[key] = india_costs[key] * hours_required
    
    # marker and min cost
    marker = [0, 0, 0, 0, 0]
    marker_values = ["Large", "2XLarge", "4XLarge", "8XLarge", "10XLarge"]
    min_cost = 0
    
    # 2D array
    bottom_up_ar = []
    
    # create upper row
    units_list = [0]
    for index in range(0, capacity_units_required + 10, 10):
        units_list.append(index)
    
    # cost list for only large machine
    large_cost_list = [10]
    for index in range(len(units_list) - 1):
        large_cost_list.append(india_costs["Large"] * index)
    
    # create initial 2D array
    bottom_up_ar.append(units_list)
    bottom_up_ar.append(large_cost_list)
    bottom_up_ar.append([40])
    bottom_up_ar.append([80])
    bottom_up_ar.append([160])
    bottom_up_ar.append([320])
    for upper_index in range(2, len(bottom_up_ar)):
        for lower_index in range(len(units_list) - 1):
            bottom_up_ar[upper_index].append(0)
    
    # index finder
    def index_finder(number):
        for index in range(len(units_list)):
            if units_list[index] == number:
                return index
    
    # finding min cost starting index 2
    for upper_index in range(2, len(bottom_up_ar)):
        base_value = 0
        if upper_index == 2:
            base_value = india_costs["2XLarge"]
        elif upper_index == 3:
            base_value = india_costs["4XLarge"]
        elif upper_index == 4:
            base_value = india_costs["8XLarge"]
        elif upper_index == 5:
            base_value = india_costs["10XLarge"]
        for lower_index in range(2, len(bottom_up_ar[upper_index])):
            if bottom_up_ar[0][lower_index] < bottom_up_ar[upper_index][0]:
                bottom_up_ar[upper_index][lower_index] = bottom_up_ar[upper_index - 1][lower_index]
            elif bottom_up_ar[0][lower_index] == bottom_up_ar[upper_index][0]:
                bottom_up_ar[upper_index][lower_index] = base_value
            else:
                bottom_up_ar[upper_index][lower_index] = min(bottom_up_ar[upper_index - 1][lower_index], base_value + bottom_up_ar[upper_index][index_finder(bottom_up_ar[0][lower_index] - bottom_up_ar[upper_index][0])])
    
    min_cost = bottom_up_ar[len(bottom_up_ar) - 1][-1]
    current_row = len(bottom_up_ar) - 1
    current_column = -1
    
    while((current_column != 1 or current_column != 0) and current_row >= 1):
        if bottom_up_ar[current_row][current_column] == bottom_up_ar[current_row - 1][current_column]:
            current_row = current_row - 1
        else:
            marker[current_row - 1] += 1
            last_column = index_finder(bottom_up_ar[0][current_column] - bottom_up_ar[current_row][0])
            if last_column == 0:
                break
            else:
                current_column = last_column
    
    # generating result
    machine_list = []
    for index in range(len(marker)):
        if marker[index] != 0:
            number_machine_pair = (marker_values[index], marker[index])
            machine_list.append(number_machine_pair)
    machine_list.sort()
    result = { "region" : "India", "total_cost" : "$"+str(min_cost), "machines" : machine_list }
    return result

# get china calculations
def get_china_details(capacity_required, hours):
    # get the required inputs
    capacity_units_required = capacity_required
    hours_required = hours
    
    # capacity dictionary
    capacities = {"Large" : 10, "XLarge" : 20, "4XLarge" : 80, "8XLarge" : 160}
    
    # new york costs
    china_costs = {"Large" : 110, "XLarge" : 200, "4XLarge" : 670, "8XLarge" : 1180}
    
    # multiply costs by hours required
    # this will get cost of each for the required hours
    for key in china_costs.keys():
        china_costs[key] = china_costs[key] * hours_required
    
    # marker and min cost
    marker = [0, 0, 0, 0]
    marker_values = ["Large", "XLarge", "4XLarge", "8XLarge"]
    min_cost = 0
    
    # 2D array
    bottom_up_ar = []
    
    # create upper row
    units_list = [0]
    for index in range(0, capacity_units_required + 10, 10):
        units_list.append(index)
    
    # cost list for only large machine
    large_cost_list = [10]
    for index in range(len(units_list) - 1):
        large_cost_list.append(china_costs["Large"] * index)
    
    # create initial 2D array
    bottom_up_ar.append(units_list)
    bottom_up_ar.append(large_cost_list)
    bottom_up_ar.append([20])
    bottom_up_ar.append([80])
    bottom_up_ar.append([160])
    for upper_index in range(2, len(bottom_up_ar)):
        for lower_index in range(len(units_list) - 1):
            bottom_up_ar[upper_index].append(0)
    
    # index finder
    def index_finder(number):
        for index in range(len(units_list)):
            if units_list[index] == number:
                return index
    
    # finding min cost starting index 2
    for upper_index in range(2, len(bottom_up_ar)):
        base_value = 0
        if upper_index == 2:
            base_value = china_costs["XLarge"]
        elif upper_index == 3:
            base_value = china_costs["4XLarge"]
        elif upper_index == 4:
            base_value = china_costs["8XLarge"]
        for lower_index in range(2, len(bottom_up_ar[upper_index])):
            if bottom_up_ar[0][lower_index] < bottom_up_ar[upper_index][0]:
                bottom_up_ar[upper_index][lower_index] = bottom_up_ar[upper_index - 1][lower_index]
            elif bottom_up_ar[0][lower_index] == bottom_up_ar[upper_index][0]:
                bottom_up_ar[upper_index][lower_index] = base_value
            else:
                bottom_up_ar[upper_index][lower_index] = min(bottom_up_ar[upper_index - 1][lower_index], base_value + bottom_up_ar[upper_index][index_finder(bottom_up_ar[0][lower_index] - bottom_up_ar[upper_index][0])])
    
    min_cost = bottom_up_ar[len(bottom_up_ar) - 1][-1]
    current_row = len(bottom_up_ar) - 1
    current_column = -1
    
    while((current_column != 1 or current_column != 0) and current_row >= 1):
        if bottom_up_ar[current_row][current_column] == bottom_up_ar[current_row - 1][current_column]:
            current_row = current_row - 1
        else:
            marker[current_row - 1] += 1
            last_column = index_finder(bottom_up_ar[0][current_column] - bottom_up_ar[current_row][0])
            if last_column == 0:
                break
            else:
                current_column = last_column
    
    # generating result
    machine_list = []
    for index in range(len(marker)):
        if marker[index] != 0:
            number_machine_pair = (marker_values[index], marker[index])
            machine_list.append(number_machine_pair)
    machine_list.sort()
    result = { "region" : "China", "total_cost" : "$"+str(min_cost), "machines" : machine_list }
    return result

def assignment(capacity_required, hours_required):

    new_york_dict = get_new_york_details(capacity_required, hours_required)
    india_dict = get_india_details(capacity_required, hours_required)
    china_dict = get_china_details(capacity_required, hours_required)

    final_list = [new_york_dict, india_dict, china_dict]

    final_result = {"Output" : final_list}

    return final_result

if __name__ == "__main__":
    capacity_required = int(input("Enter units of capacity required: "))
    hours_required = int(input("Enter the number of hours machine is required to run: "))
    print(assignment(capacity_required, hours_required))