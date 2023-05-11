import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime
import plotly.express as px

# Chargement en local en pikle
df = pd.read_csv("df.csv")

# Mise en forme du df
df['genre'].replace("Children’s Music", "Children's Music", inplace=True)
df.astype({"year" : "int"})

# Configuration de la page
st.set_page_config(
    page_title="Reconver'Son",
    #layout="wide",
    page_icon="🎙️")

# titre
#st.title("Présentation du dataset")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}<style>, unsafe_allow_html=True)
st.title(""Présentation du dataset")



# Top 5 Genres
genres5 = df.groupby(["genre"]).count().reset_index().sort_values(by = "artist_name", ascending = False)[:5].iloc[:,:2]
list_genres5 = ["Alternative", "Dance", "Folk", "Blues", "Hip-Hop"]
df_top5 = df[df["genre"].isin(list_genres5)]
# Visualisation
fig2 = px.histogram(df_top5, x = "genre", text_auto=True,
                   template="xgridoff",
            color_discrete_sequence= px.colors.sequential.Burg)

fig2.update_yaxes(title_text = "Total")
fig2.update_xaxes(title_text = "Genres")
fig2.update_layout(title = {"text" : "Top 5 des genres les plus représentés", "x":0.5})
st.plotly_chart(fig2)


# TEMPO
genres10 = df.groupby(["genre"]).count().reset_index().sort_values(by = "artist_name", ascending = False)[:10].iloc[:,:2]
list_genres10 = ["Alternative", "Dance", "Folk", "Blues", "Hip-Hop", "Country", "Soundtrack", "Soundtrack", "Electronic", "Classical", "Anime"]
df_top10 = df[df["genre"].isin(list_genres10)]
df1 = df_top10.groupby(["genre"]).count().reset_index()
# Visualisation
fig3 = px.bar(df1,
             x='tempo',
             y='popularity', color = "genre",
            barmode='stack',
              template="xgridoff",
             labels={"tempo": "Tempo", "popularity" : "Popularité", "genre" : "Genres"})
fig3.update_layout(title = {"text" : "Popularité en fonction du tempo par genre", "x":0.5})
st.plotly_chart(fig3)

# TOP Artistes
artist = df.groupby(["artist_name"]).count().reset_index().sort_values(by = "genre", ascending = False)[:10].iloc[:,:2]
# Visualisation
fig5 = px.bar(artist,
             x='artist_name',
             y='genre', color = "genre",
            barmode='stack',
              template="xgridoff",
             labels={"artist_name": "Nom de l'artiste", "genre" : "Total", "genre" : "Total"}
             )
fig5.update_layout(title = {"text" : "Artistes les plus représentés", "x":0.5})
st.plotly_chart(fig5)

# TOP Danceability
# Visualisation
fig7 = px.histogram(df, x="year", y="danceability",
                    template="xgridoff",
                    color_discrete_sequence= px.colors.sequential.Burg,
                   #labels = {"year" : "Années", "danceability" : "Danceability"}
                   )

fig7.update_yaxes(title_text = "Années")
fig7.update_xaxes(title_text = "Danceability")
fig7.update_layout(title_text = "Danceability en fonction des années", title_x=0.5)
st.plotly_chart(fig7)


# Grenres les plus représentés
genres2 = df.groupby(["genre"]).count().reset_index().sort_values(by = "artist_name", ascending = False)[:].iloc[:,:2]
st.header('Genres les plus représentés')
fig9 = px.histogram(genres2, x="genre", y ="artist_name", text_auto=True,
                   template="xgridoff",
                    color_discrete_sequence= px.colors.sequential.Burg,)

fig9.update_yaxes(title_text = "Total")
fig9.update_xaxes(title_text = "Genres")
fig9.update_layout(title_text = "Nombre de genres les plus représentés", title_x=0.5)
st.plotly_chart(fig9)
