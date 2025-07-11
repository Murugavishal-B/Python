def generate_pattern(input_string):
    length = len(input_string)
    for i in range(length):
        substring = input_string[-(i+1):] + input_string[:-(i+1)]
        print(substring)
input_string = "PROGRAM"
generate_pattern(input_string)
