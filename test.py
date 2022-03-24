input = 120000

second = input % 60
input = int(input / 60)

minute = input % 60
input = int(input / 60)

hour = input % 24
day = int(input / 24)

print(day, hour, minute, second)
