def pos():
    sum_of_numbers = 0
    for num in numbers:
        if num > 0:
            sum_of_numbers += num
    return sum_of_numbers


def neg():
    sum_of_numbers = 0
    for num in numbers:
        if num < 0:
            sum_of_numbers += num
    return sum_of_numbers


def print_diff(negative, positive):
    print(negative)
    print(positive)

    if abs(negative) > positive:
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"


numbers = [int(number) for number in input().split()]
positive_sum = pos()
negative_sum = neg()
print(print_diff(negative_sum, positive_sum))