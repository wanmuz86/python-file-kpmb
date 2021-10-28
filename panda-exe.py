# shortform pandas to pd 
import pandas as pd 

#Open a CSV file using pandas..
df = pd.read_csv("pokemon.csv")

# print(df)

#We can do some operation with pandas..
# give me the first 5 infos in the CSV
# print(df.head(5))

#give me the last 5 infos from the CSV

#print(df.tail(5))

#Give me all the columns available in this CSV
print(df.columns) 

# print(df['HP'])
print(df[['Name','HP','Attack','Defense']])
print(df.iloc[0,:])
print(df.iloc[0:10,:])
print(df.iloc[1,1])

#sort 

print(df.sort_values(['Attack'],ascending=[0])[['Name']])

#filter
## give me all the pokemon where type 1 == Grass
grassPokemon = df.loc[df['Type 1']=='Grass']

#write back to file
grassPokemon.to_csv('grass.txt',sep=",")

