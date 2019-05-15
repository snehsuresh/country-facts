from db import country_info
#GDP - per capita (PPP) compares GDP on a purchasing power parity basis divided by population as of 1 July for the same year.
print("         ****Welcome to our Database. Find out about your country.****         \n")
#print("\n\nNote:This ranking is based on projection by International Monetary Fund (IMF) outlook April 2017 for year 2017.\nWe as a group of students assume no responsibility for any errors or omissions in the content of this program.\nThe information here is given on an “as is” basis with no guarantees of completeness, accuracy or usefulness.\n*Source:Wikipedia*\n\n")
country=input("Enter Country name : ")
country = country.lower()
if country in country_info:
    print("\tCapital : " + country_info[country][0]+"      \n\tGDP(nominal)per capita : " +country_info[country][1]+"      \n\tRank : " +country_info[country][2])
else:
    print("Country not found")
again ="yes"
while again == "yes":
    again = input("search again? yes/no: ").lower()
    if again == "yes":
        country = input("Enter Country name : ")
        country = country.lower()
        if country in country_info:
          print("\tCapital : " + country_info[country][0]+"      \n\tGDP(nominal)per capita : " +country_info[country][1]+"      \n\tRank : " +country_info[country][2])
        else:
          print("Country not found")
    elif again == "no":
        print("Your search is completed successfully. Thank you!")
        break
