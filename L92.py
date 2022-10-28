#Emily Rusch and Kaylen Nyhuis

def remove_substring(string, target):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(target)] == target:
            index += len(target)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))

string = "WOWToday is such a WOWbeautifulWOW day!"
target = "WOW"

remove_substring(string, target)
