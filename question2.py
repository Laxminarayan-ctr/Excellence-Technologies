

dict = {"1" : 60, "2" : 20, "3" : 16, "4" : 14}

print(max(dict.items(), key=lambda i: i[1]))