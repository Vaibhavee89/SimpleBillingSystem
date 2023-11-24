print('Billing Software')
sum=0
lst_category=['Rice and Flours','Pulses','Spice','Oils','Nuts','Other Ingredients','Dairy']

dict_riceflour={"Turmeric":256,"Sugar":31, "Jaggery":100, "Basmati rice":180,"Wheat flour":67,"Maida":60,"Rice flour":49,"Poha":205,"Vermicelli":100,"Tea powder":135,"Cocoa powder":300,"Instant Coffee powder":250,"Baking soda":50}
dict_oil={"Coking Oil":170,"Coconut Oil":260,"Ghee":700, "Butter":417,"Olive Oil":500,"Seasame oil":150}
dict_pulses= {"Tur dal":94,"Channa":70,"Urad":120,"Moong":250,"Rajma":200}
dict_spice= {"Powder salt":30,"Red Chilli":185, "Dhania Powder":140,"Garam Masala":80,"Chat Masala":80}
dict_nuts={"Cashew nuts":490,"Dry raisins":150,"Almonds":610,"Peanut":90}
dict_other={"Papad":140,"Noodles":20,"Pasta":37,"Tomato Ketchup":140,"Jam":300,"Mayonaise":200,"Bread":30}
dict_dairy={"Cheese":780,"Butter":55,"Curd":40,"Paneer":378,"Fresh milk":60,"Fresh cream":280}

print(lst_category)

while True:
    order= input("Enter 1st category: ")
    if order in lst_category:
        if order== 'Rice and Flours':
            print(dict_riceflour.keys())
            lst= (dict_riceflour.keys())
            a= input('Enter subcategory: ')
            if a in lst:
                print(dict_riceflour[a])
                sum= sum+dict_riceflour[a]
            else:
                print('Enter correct subcategory')
        elif order== 'Pulses':
            print(dict_pulses.keys())
            lst= (dict_pulses.keys())
            a= input('Enter subcategory: ')
            if a in lst:
                print(dict_pulses[a])
                sum= sum+dict_pulses[a]
            else:
                print('Enter correct subcategory')
        elif order== 'Spice':
            print(dict_spice.keys())
            lst= (dict_spice.keys())
            a= input('Enter subcategory: ')
            if a in lst:
                print(dict_spice[a])
                sum= sum+dict_spice[a]
            else:
                print('Enter correct subcategory')
        elif order== 'Oils':
            print(dict_oil.keys())
            lst= (dict_oil.keys())
            a= input('Enter subcategory: ')
            if a in lst:
                print(dict_oil[a])
                sum= sum+dict_oil[a]
            else:
                print('Enter correct subcategory')
        elif order== 'Nuts':
            print(dict_nuts.keys())
            lst= (dict_nuts.keys())
            a= input('Enter subcategory: ')
            if a in lst:
                print(dict_nuts[a])
                sum= sum+dict_nuts[a]
            else:
                print('Enter correct subcategory')
        elif order== 'Other Ingredients':
            print(dict_other.keys())
            lst= (dict_other.keys())
            a= input('Enter subcategory: ')
            if a in lst:
                print(dict_other[a])
                sum=sum+dict_other[a]
            else:
                print('Enter subcategory')
        elif order== 'Dairy':
            print(dict_dairy.keys())
            lst= (dict_dairy.keys())
            a= input('Enter subcategory: ')
            if a in lst:
                print(dict_dairy[a])
                sum= sum+dict_dairy[a]
            else:
                print('Enter correct subcategory')
    elif order== 'E':
        break
    else:
        print('Enter correct category')
print('Total Bill is: ' ,sum)
