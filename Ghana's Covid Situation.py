import bs4
import requests
import re
import pandas as pd
import plotly.graph_objects as go #Sorry no matplotlib :(, plotly is much more attractive xD but it only works in jupyter notebooks

#Regular expression used to only select numeric data in a list
def getNumbers(array): 
    arr = re.findall(r'[0-9]', array) 
    return arr 

#Clean() function removes commas in lists
def clean(data):
    strings = [str(num) for num in data]
    concatenated = "".join(strings)
    return(concatenated)
    
res = requests.get('https://www.worldometers.info/coronavirus/country/ghana/')
text = bs4.BeautifulSoup(res.text)
cases = clean(getNumbers(str(text.select('div span')[4])))
deaths = clean(getNumbers(str(text.select('div span')[5])))
recoveries = clean(getNumbers(str(text.select('div span')[6])))

print("Total Cases:", cases,  "\n")
print("Total Recoveries:", recoveries, "\n")
print("Total Deaths:", deaths,'\n')

js = text.select('script[type="text/javascript"]') #Js contains the javascript of the website

#Js is a list and the various list indices extract the useful part of the list needed
data_for_days = list(js[7])
data_for_cases = list(js[7])
data_for_deaths = list(js[10])

#Regular expression \w\w\w\s\d+ matches any three digit word with a space followed by one or more numbers
days_reg = re.compile(r'\w\w\w\s\d+')
days = days_reg.findall(data_for_days[0])

#Regular expression d{1,7} matches any number with at most 7 digits. 
cases_reg = re.findall(r'\d{1,7}',data_for_cases[0]) #Edit this line of code if Ghana's Corona Virus Cases surpass 1 million :(

deaths_reg = re.findall(r'\d{1,7}',data_for_deaths[0]) #Edit this line of code if Ghana's Corona Virus Cases surpass 1 million :(

data_for_cases = [int(i) for i in cases_reg]
data_for_deaths = [int(i) for i in deaths_reg]

data_for_cases = data_for_cases[350::]
data_for_deaths = data_for_deaths[350::]

case_index = data_for_cases.index(0)
death_index = data_for_deaths.index(0)

total_cases = data_for_cases[case_index:len(data_for_cases) - 1]
total_cases = [int(i) for i in total_cases]
total_deaths = data_for_deaths[death_index:len(data_for_deaths) - 1]
total_deaths = [int(i) for i in total_deaths]
total_cases = total_cases[26::]
total_deaths = total_deaths[26::]

ind = days.index('Jul 29')
days = days[ind::]
ind = days.index('Mar 12')
days = days[ind::]

data = {'Days': days,
        'Total Cases':total_cases,
        'Total Deaths': total_deaths
       }


original_df = pd.DataFrame(data)
original_df.reset_index(inplace=True)
del original_df["index"]

original_df.to_csv("Ghana's Covid-19 Dataset.csv")
#Cleaned_df contains same data but with the days before first case recorded removed
#cleaned_df = original_df.drop([i for i in range(26)],axis=0)
#cleaned_df.reset_index(inplace=True)
#cleaned_df.to_csv("Ghana's Covid-19 Dataset.csv")



y_data = total_cases
x_data = days

fig = go.Figure()

fig.add_trace(go.Scatter(x=x_data, y=y_data
    ))

fig.update_layout(
    title_text="Ghana's Corona Virus Cases", title_x=0.5,
    xaxis=dict(
        showgrid=True,    
        linewidth=2,
        ticks='outside',
        tickangle = -67,
        tickfont=dict(
            family='Arial',
            size=12
        ),
    )
    )
fig.show()
