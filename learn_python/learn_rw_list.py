list1 = [{"name":"koos1", "surname":"smith1"}, {"name":"piet2", "surname":"jones2"}]

for x in list1:
    print(x)
    if x['name'] == "koos1":
        print(" detail - " + str(x) )