import pandas as pd
import streamlit as st
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')
#read the data
df['is_4wd'] = df['is_4wd'].where(df['is_4wd'] != 1.0 , 'yes')
df['is_4wd'] = df['is_4wd'].fillna('no')
#replace four wheel drive values with yes and no
st.title('Figures on car sales')

st.header('Data viewer')
st.dataframe(df)
#There will be two plots
#A scatterplot should be able to show a strong or week correlation between two variables
#The two variables ill select is price and odometer
#I was able to observe that odometer contains some missing information so i will remove the cars with missing values
#I will be able to observe the strength of the correlation between these variables
#i will now create a data set with all missing values in the odometer collumn removed

df_model_year = df.dropna(subset = ['odometer'])
st.header('Scatter Plot: click on scatter points to see car model and other details')
fig = px.scatter(df , x = 'odometer', 
                 y = 'price', 
                 color = 'condition',
                 title = 'Odometer vs Price (Make selection to see different car condition selections)',
                 hover_name = 'model'
                 )
#also contains name of car
st.write(fig)

st.header('Histogram: Manfacturer and fuel type (make a fuel type selection)')

df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

st.write(px.histogram(df, x='manufacturer', color='fuel',opacity = .7))
