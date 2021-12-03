import sys
with open(sys.argv[1],"r",encoding="utf-8") as file:
    list_1 = file.read().split("\n")
dict_1 = {}
for i in list_1:
    temp_list = i.split(":")
    dict_1[temp_list[0]] = temp_list[1]
for i2 in sys.argv[2].split(","):
    try:
        print("Name: {}, University: {}".format(i2,dict_1[i2]))
    except:
        print("No record of {} was found".format(i2))