mobiles={"Apple":{"model":"iphone15","price":120000,"color":"Black"},
         "Samsung":{"model":"S23 Ultra","price":180000,"color":"white"},
         "Sony":{"model":"xperia ultra","price":130000,"color":"red"},
         "Huawei":{"model":"Pura 70 ultra","price":170000,"color":"Black"}
         }

# print(mobiles["Apple"]["model"])

# for i in mobiles:
    
#     if mobiles[i]["color"] == "Black":

#         print(mobiles[i])




# # price above 50k 

# for i in mobiles:

#     if mobiles[i]["price"] > 50000:

#         print(mobiles[i])




# iphone or xperia

# for i in mobiles:

#     if mobiles[i]["model"] == "iphone15" or mobiles[i]["model"] == "xperia ultra":

#         print(mobiles[i])




# colors other than black

# for i in mobiles:

#     if mobiles[i]["color"] != "Black":

#         print(mobiles[i])

    


# Black in color and less than 150000

# for i in mobiles:

#     if mobiles[i]["color"] == "Black" and mobiles[i]["price"] < 150000:

#         print(mobiles[i])




# price in b/w 100000 and 150000

# for i in mobiles:

#     if mobiles[i]["price"] >= 100000 and mobiles[i]["price"] < 150000:

#         print(mobiles[i])




# price in b/w 100000 and 150000 and the color is red

for i in mobiles:

    if 100000 < mobiles[i]["price"]  < 150000 and mobiles[i]["color"] == "red":

        print(mobiles[i])