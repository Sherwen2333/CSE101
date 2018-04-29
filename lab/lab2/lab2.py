# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Lab 2


def compute2(x, y):
    if x <= 0:
        return x + 2 * y
    elif 0 < x <= 8:
        return (1 - y) / x
    else:
        return (y * y) / (x * x * x)


def computer_price(cpu, ghz, disk_type, disk_size):
    price = 1000
    if cpu != 'AMD' and price != 'Intel': return -1.0
    if cpu == 'AMD': price += 175
    if cpu == 'Intel': price += 200
    if ghz < 1: return -1.0
    if 2 > ghz >= 1: price += 80
    if ghz >= 2: price += 150
    if disk_type != 'HDD' and disk_type != 'SSD': return -1.0
    if disk_type == 'HDD': price += 100
    if disk_type == 'SSD': price += 225
    if disk_size <= 0: return -1.0
    return price + disk_size * 2
