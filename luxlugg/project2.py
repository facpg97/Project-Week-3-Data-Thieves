#importing the libraries
from itertools import cycle
import requests
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import webbrowser

#tables import:

#travels table:
travels_table= pd.read_csv(r'travels/Project-Week-3-Data-Thieves/Project-Week-3-Data-Thieves/flights_tap.csv')

#women clothes tables:
women_bags=pd.read_csv('travels/Project-Week-3-Data-Thieves/Project-Week-3-Data-Thieves/women/women_bags.csv')
women_bottoms=pd.read_csv('travels/Project-Week-3-Data-Thieves/Project-Week-3-Data-Thieves/women/women_bottoms.csv')
women_jackets=pd.read_csv('travels/Project-Week-3-Data-Thieves/Project-Week-3-Data-Thieves/women/women_jackets.csv')
women_shoes=pd.read_csv('travels/Project-Week-3-Data-Thieves/Project-Week-3-Data-Thieves/women/women_shoes.csv')
women_tops=pd.read_csv('travels/Project-Week-3-Data-Thieves/Project-Week-3-Data-Thieves/women/women_tops.csv')

#men clothes tables:
men_coats=pd.read_csv('travels/Project-Week-3-Data-Thieves/Project-Week-3-Data-Thieves/men/men_coats.csv')
men_shorts=pd.read_csv('travels/Project-Week-3-Data-Thieves/Project-Week-3-Data-Thieves/men/men_shorts.csv')
men_tops=pd.read_csv('travels/Project-Week-3-Data-Thieves/Project-Week-3-Data-Thieves/men/men_tops.csv')
men_trainers=pd.read_csv('travels/Project-Week-3-Data-Thieves/Project-Week-3-Data-Thieves/men/men_trainers.csv')
men_trousers=pd.read_csv('travels/Project-Week-3-Data-Thieves/Project-Week-3-Data-Thieves/men/men_trousers.csv')

# initiate product
print('\nWelcome to LuxLugg, we hope you enjoy the journey to your final destination. A more trendy, stylish and exclusive trip to a destination of your choice.')
#input the city:
print('\n')
city_input=input('What is your European city of choice for this experience? ')
print('\n')
city_text= str(city_input)

#input the gender:

gender_input=input('Are you interested in a LuxLugg with women or men clothing? ')
print('\n')
gender_text= str(gender_input).lower()

# uses the response to create a dataframe with the weather info:
def weather_function(x):
    series=pd.Series(x)
    data1=pd.DataFrame(series['list'])
    data1=data1[['main','weather','dt_txt']]
    data2=pd.DataFrame(series['city'])  
    data2=data2[['name','country']]
    data2=data2.T
    data2=data2['lat']
    main=pd.json_normalize(data1['main'])
    weather=pd.json_normalize(data1['weather'])
    weather=pd.json_normalize(weather[0])
    data3=pd.concat([weather,main], axis=1)
    data3['city']=[data2['name'] for el in range(0,len(data3))]
    data3=data3[['main', 'temp', 'city']]
    data3=pd.concat([data3,data1['dt_txt']], axis=1)
    data3['temp_celsius']=[el-(272.15) for el in data3['temp']]
    data3=data3[data3['dt_txt'].str.contains('12')]
    data3=data3.reset_index(drop="True")
    return data3

# returns the response from the API
def weather_api(city_text):
    parameters={'q':city_text,
    'appid':'848d0de82969372b0eb09e4c7106d12f'}
    url='https://api.openweathermap.org/data/2.5/forecast'
    response=requests.get(url=url, params=parameters)
    x=response.json()
    dataf = weather_function(x)
    return dataf

#geting data from weathers api:
weather_df = weather_api(city_text)
print('The weather forecast for the days of your trip is:')
print('\n')
print(weather_df)
print('\n')
#temperatures per day:
day1_temp = weather_df['temp_celsius'][1]
day2_temp = weather_df['temp_celsius'][2]
day3_temp = weather_df['temp_celsius'][3]


#geting the info of the city we are going to travel:

#print(travels_table)

#city_index:
city_index=travels_table[travels_table['city']==city_text].index
#print(city_index)

#travel price:
travel_price=travels_table.loc[city_index,'price']
#print(travel_price)

#travel description:
travel_description=travels_table.loc[city_index,'category']
#print(travel_description)

#travel_country:
travel_country=travels_table.loc[city_index,'country']

#clothes for day 1:
list_clothes1=[]
if gender_text=='women':
    if day1_temp>20:
        list_clothes1.append(women_tops[['name','price','url']].sample())
        list_clothes1.append(women_bottoms[['name','price','url']].sample())
        list_clothes1.append(women_shoes[['name','price','url']].sample())
        list_clothes1.append(women_bags[['name','price','url']].sample())
    else:
        list_clothes1.append(women_tops[['name','price','url']].sample())
        list_clothes1.append(women_bottoms[['name','price','url']].sample())
        list_clothes1.append(women_shoes[['name','price','url']].sample())
        list_clothes1.append(women_bags[['name','price','url']].sample())
        list_clothes1.append(women_jackets[['name','price','url']].sample())
else:
    if day1_temp>20:
        list_clothes1.append(men_tops[['name','price','url']].sample())
        list_clothes1.append(men_shorts[['name','price','url']].sample())
        list_clothes1.append(men_trainers[['name','price','url']].sample())
    else:
        list_clothes1.append(men_tops[['name','price','url']].sample())
        list_clothes1.append(men_trousers[['name','price','url']].sample())
        list_clothes1.append(men_trainers[['name','price','url']].sample())
        list_clothes1.append(men_coats[['name','price','url']].sample())
df_list_clothes1=pd.concat(list_clothes1)

print('The outfit for the first day: ')
print('\n')
print(df_list_clothes1)
print('\n')
#clothes for day 2:
list_clothes2=[]
if gender_text=='women':
    if day2_temp>20:
        list_clothes2.append(women_tops[['name','price','url']].sample())
        list_clothes2.append(women_bottoms[['name','price','url']].sample())
        list_clothes2.append(women_shoes[['name','price','url']].sample())
        list_clothes2.append(women_bags[['name','price','url']].sample())
    else:
        list_clothes2.append(women_tops[['name','price','url']].sample())
        list_clothes2.append(women_bottoms[['name','price','url']].sample())
        list_clothes2.append(women_shoes[['name','price','url']].sample())
        list_clothes2.append(women_bags[['name','price','url']].sample())
        list_clothes2.append(women_jackets[['name','price','url']].sample())
else:
    if day2_temp>20:
        list_clothes2.append(men_tops[['name','price','url']].sample())
        list_clothes2.append(men_shorts[['name','price','url']].sample())
        list_clothes2.append(men_trainers[['name','price','url']].sample())
    else:
        list_clothes2.append(men_tops[['name','price','url']].sample())
        list_clothes2.append(men_trousers[['name','price','url']].sample())
        list_clothes2.append(men_trainers[['name','price','url']].sample())
        list_clothes2.append(men_coats[['name','price','url']].sample())
df_list_clothes2=pd.concat(list_clothes2)

print('The outfit for the second day: ')
print('\n')
print(df_list_clothes2)
print('\n')
#clothes for day 3:
list_clothes3=[]

if gender_text=='women':
    if day3_temp>20:
        list_clothes3.append(women_tops[['name','price','url']].sample())
        list_clothes3.append(women_bottoms[['name','price','url']].sample())
        list_clothes3.append(women_shoes[['name','price','url']].sample())
        list_clothes3.append(women_bags[['name','price','url']].sample())
    else:
        list_clothes3.append(women_tops[['name','price','url']].sample())
        list_clothes3.append(women_bottoms[['name','price','url']].sample())
        list_clothes3.append(women_shoes[['name','price','url']].sample())
        list_clothes3.append(women_bags[['name','price','url']].sample())
        list_clothes3.append(women_jackets[['name','price','url']].sample())
else:
    if day1_temp>20:
        list_clothes3.append(men_tops[['name','price','url']].sample())
        list_clothes3.append(men_shorts[['name','price','url']].sample())
        list_clothes3.append(men_trainers[['name','price','url']].sample())
    else:
        list_clothes3.append(men_tops[['name','price','url']].sample())
        list_clothes3.append(men_trousers[['name','price','url']].sample())
        list_clothes3.append(men_trainers[['name','price','url']].sample())
        list_clothes3.append(men_coats[['name','price','url']].sample())
df_list_clothes3=pd.concat(list_clothes3)

print('The outfit for the third day: ')
print('\n')
print(df_list_clothes3)
print('\n')

#making a list of all clothes ans sending and count the price
df_all_clothes= pd.concat([df_list_clothes1,df_list_clothes2,df_list_clothes3])
clothes_price_list= [float(pr[0].replace(',', '')) for pr in df_all_clothes['price'].str.split(' €')]
total_clothes_price = sum(clothes_price_list)

# generating a pdf file with the list os outfits, price and url of the website:

answer1_input=input('Would you like to dowload your Farfetch shopping list? ')
print('\n')
answer1_text= str(answer1_input)

if answer1_text == 'yes':

    fig, ax =plt.subplots(figsize=(20,4))
    ax.axis('tight')
    ax.axis('off')

    the_table = ax.table(cellText=df_all_clothes.values,colLabels=df_all_clothes.columns,loc='center')

    the_table.auto_set_font_size(False)
    the_table.set_fontsize(8)
    the_table.auto_set_column_width(col=list(range(len(df_all_clothes.columns))))

    pp = PdfPages("shopping_list.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()

#open the web browser:

answer2_input=input('Would you like to open the links of your shopping list? ')
print('\n')
answer2_text= str(answer2_input)

if answer2_text=='yes':
    for el in df_all_clothes['url']:
        url = el
        webbrowser.open(url=url)
else:
    print('Thank you for using LuxLugg, we hope you have an amazing time, we already know you will have amazing fits!')
   