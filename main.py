"""Search for the given string in file and return lines containing that string,
along with line numbers"""
line_number = 1
list_of_results = []

with open('Telegram копія.txt', 'r') as read_obj:
    # Read all lines in the file one by one
    for line in read_obj:
        # For each line, check if line contains the string
        line_number += 1
        if "Name:" in line:
            # If yes, then add the line number & line as a tuple in the list
            list_of_results.append(line.rstrip())
            if "Form Name: Cart" in line:
                list_of_results.remove(line.rstrip())
        elif "Phone" in line:
            list_of_results.append(line.lstrip())
        elif "Payment Amount:" in line:
            list_of_results.append(line.rstrip())
        elif "Email:" in line:
            list_of_results.append(line.rstrip())
        elif "date_to__pickup:" in line:
            list_of_results.append(line.rstrip())
        if "§" in line:
            list_of_results.append(line.rstrip())
            
            
with open("experiment_FINALt.txt", 'w') as write_name:

    for line in list_of_results:
        write_name.write(str(line) + ';')
