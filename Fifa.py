#Download files
import webget

url = 'https://raw.githubusercontent.com/INFINITE-KH/Python-Dataset/master/complete.csv'


webget.download(url)


#Read file
import pandas as pd
dataframe = pd.read_csv('complete.csv')



#Choose specific columns 
#(REMOVE # BELOW TO SEARCH FOR SPECIFIC COLUMNS)
#columns = dataframe[dataframe.columns[16:23]]
#pd.DataFrame(columns)



#Choose specific rows 
#(REMOVE # BELOW TO SEARCH FOR SPECIFIC ROWS)
#rows = dataframe.head(15)
#print(rows)


#QUESTION 1: The 3 most expensive teams and the 3 cheapest teams according to player value.

#Create dataframe with the wanted columns
data = {
    'Value':dataframe['eur_value'],
    'Club':dataframe['club'],
    'Name':dataframe['full_name']
    } 

#put columns together (remove the # from print to se the result)
result = pd.DataFrame(data, columns=['Club', 'Name', 'Value'])


#QUESTION 1: get the largest value 
print(result['Value'].nlargest(3))

result[1:4]


#Need help to put these information together


#QUESTION 1: get the smallest value
print(result['Value'].nsmallest(3))

print(result[163:164])
print(result[168:169])
print(result[271:272])


#Need help to put these information together and to remove result if the value is 0

#Question 2: Which nationality is the most frequent amongst all players
nationality = dataframe['nationality'].value_counts()

print(nationality[0:10])

#Question 3: What is the difference between the release clause and the value of top 10 most valuable players

release_clause = dataframe['eur_release_clause'].nlargest(10)
eur_value = dataframe['eur_value'].nlargest(10)

#Create dataframe with the wanted columns
data = {
  'Club':dataframe['club'][0:9],
    'Name':dataframe['full_name'][0:9],
    'Release Clause':dataframe['eur_release_clause'].nlargest(10),
    'Eur Value':dataframe['eur_value'].nlargest(10),
    'Difference':dataframe['eur_release_clause'].subtract(eur_value)[0:9]
    } 

#put columns together
result = pd.DataFrame(data, columns=['Club', 'Name', 'Eur Value', 'Release Clause', 'Difference'])
print(result)

#Question 4: Collect the needed data

#Create dataframe with the wanted columns
data = {
    'Name':dataframe['full_name'],
    'Age':dataframe['age'],
    'Height':dataframe['height_cm'],
    'Weight':dataframe['weight_kg']
    } 

#put columns together
result = pd.DataFrame(data, columns=['Name', 'Age', 'Height', 'Weight'])
#Print specific amount of rows
print(result[:10])


#Question 4: What is the frequency of age, height and weight for all players
ages = dataframe['age'].value_counts()
heights = dataframe['height_cm'].value_counts()
weights = dataframe['weight_kg'].value_counts()

print(ages, heights, weights)


#Question 5: How big is the average difference between value and wage of the players


#Create dataframe with the wanted columns
data = {
    'Name':dataframe['full_name'][0:9],
    'Eur Value':dataframe['eur_value'],
    'Eur Wage':dataframe['eur_wage'],
    'Difference (value, wage)':dataframe['eur_value'].subtract(eur_wage),
    'Average (value, wage)':(dataframe['eur_value']+dataframe['eur_wage'])/2
    } 

#put columns together
result = pd.DataFrame(data, columns=['Name', 'Eur Value', 'Eur Wage', 'Difference (value, wage)', 'Average (value, wage)'])
print(result[:10])


