number = int(input('Enter the power: '))
total_times = number
operation_count = 0

while 0 <= total_times:
    value = 2 ** operation_count
    print(operation_count, value)

    operation_count += 1
    total_times -= 1



