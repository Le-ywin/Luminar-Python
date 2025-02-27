# Write a function  that takes a positive integer n and returns the sum of its digits.


def sum_of_digits(num):

    if num > 0:

        sum = 0

        for i in str(num):

            sum += int(i)

sum_of_digits(345)