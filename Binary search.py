import csv


def get_data():
    numbers = []
    with open('num.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            if row is not 'num':
                numbers += row
    numbers = list(map(int, numbers))
    return numbers


def binary_search(searched_num):
    numbers = get_data()
    left, right = 0, len(numbers) - 1
    while left <= right:
        m = int((left + right) / 2)
        if numbers[m] > searched_num:
            right = m - 1
        elif numbers[m] < searched_num:
            left = m + 1
        else:
            return m
    return 'unsuccessful'


if __name__ == '__main__':
    searched_num = input('Enter number:')
    result = binary_search(int(searched_num))

    if result == 'unsuccessful':
        print('There is no such number in the data set.')
    else:
        print(f'The index of number: {searched_num} is {result} (starting from 0).')
