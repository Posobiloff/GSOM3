def rod_profit_max(length, prices):
    maximum_value = [0] * (length + 1)
    number_of_cuts = [0] * (length + 1)
    for i in range(1, length + 1):
        maximum_value_obtained = 0
        for j in range(i):
            if maximum_value_obtained < prices[j] + maximum_value[i - j - 1]:
                maximum_value_obtained = prices[j] + maximum_value[i - j - 1]
                number_of_cuts[i] = j + 1
        maximum_value[i] = maximum_value_obtained

    recommended_lengths = []
    while length > 0:
        recommended_lengths.append(number_of_cuts[length])
        length -= number_of_cuts[length]

    return f"The recommended lengths are {recommended_lengths}. You can sell them for {maximum_value[-1]} dollars"
#1
length = 8
prices = [2, 5, 8, 9, 10, 26, 25, 20]
print(rod_profit_max(length, prices))
#2
length = 8
prices = [90, 5, 8, 9, 10, 26, 25, 20]
print(rod_profit_max(length, prices)) 
#3
length = 10
prices = [1, 3, 5, 7, 9, 12, 13, 16, 17, 17]
print(rod_profit_max(length, prices))  