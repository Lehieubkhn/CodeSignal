def depositProfit(deposit, rate, threshold):
    year = 0
    percent = (rate/100)
    while deposit < threshold:
        deposit += percent*deposit
        year += 1
    return year


deposit = 100
rate = 20
threshold = 170
print(depositProfit(deposit, rate, threshold))