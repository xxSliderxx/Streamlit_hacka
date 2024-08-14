import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors


# Background
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://diapogram.com/upload/2018/04/11/20180411162221-dd86ff34.jpg");
    background-size: cover;
    
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0); /* En-tête transparent */
}


/* Styles pour les paragraphes et divs */
p, div {
    font-size: 1.02em; 
    font-weight: bold; 
}

.big-bold-label {
    font-size: 1.02em; /* Augmente la taille de la police */
    font-weight: bold; /* Rend le texte en gras */
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)







df_try = pd.read_csv('Matrice.csv')





st.header("Plannification de voyage")

Choix = st.radio("Avez vous une idée du continent sur lequel vous voulez aller ?",['Oui','Non'])

if Choix == 'Oui':
    X2 = ['Continent_enc',                                                   
    'Séjour euro',                                                       
    'Sur place euro',                                                    
    'Cost_of_Living_Index',                                             
    'Air_Quality_Index',                                           
    'Happiness_Score']
    

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df_try[X2])

    knn = NearestNeighbors(n_neighbors=5)
    knn.fit(scaled_features)

    st.write("Afin de vous proposer une destination possible, pourriez vous répondre aux questions suivantes ?")

    List_Continent = ['Amerique du Nord', 'Europe', 'Asie', 'Australie/Pacifique Sud', 'Moyen Orient', 'Amérique Centrale / du Sud & Caraïbes', 'Afrique']
    Dico_cont = {'Europe':1,'Asie':2,'Amérique Centrale / du Sud & Caraïbes':3,'Amerique du Nord':4,'Australie/Pacifique Sud':5,'Moyen Orient':6,'Afrique':7 }
    cont = st.radio('Sur quel continent souhaiteriez vous aller ? ',List_Continent)
    cont = Dico_cont[cont] 






    x = st.number_input("Quel montant souhaiteriez vous dépenser par personne pour un voyage d'une semaine tout compris ?")
    if x>=0:
        Sej = x
    else:
        st.write("La valeur donnée n'est pas cohérente. Veuillez corriger !")



    y = st.number_input('Quel est le budget quotidien par personne (hébergement compris) ?')
    if y>= 0:
        Place = y
    else :
        st.write("La valeur donnée n'est pas cohérente. Veuillez corriger !")


    Res2 = st.radio("Est ce que la coût de la vie est un critère important pour vous ?", ['Oui', 'Non'])
    if Res2 == 'Oui':
        Cout_vie = st.number_input("Donnez alors une valeur correspondant au niveau de vie entre 0 et 10.", key="Cout_vie_input")
        if 0 <= Cout_vie <= 10:
            Cout_vie = Cout_vie * 10 + 30
        else:
            st.write("La valeur donnée n'est pas cohérente. Veuillez corriger !")
    else:
        Cout_vie = 80

    Res = st.radio("Est ce que la qualité de l'air est une notion importante pour vous ?", ['Oui', 'Non'])
    if Res == 'Oui':
        Air = st.number_input("Donnez alors une valeur correspondant au niveau de la qualité de l'air souhaité entre 0 et 10 (0 : air pur, 10 : air pollué).", key="Air_input")
        if 0 <= Air <= 10:
            Air = Air * 20 + 20
        else:
            st.write("La valeur donnée n'est pas cohérente. Veuillez corriger !")
    else:
        Air = 70

    Res3 = st.radio("Est ce que le bien être dans la ville est un critère important pour vous ?", ['Oui', 'Non'])
    if Res3 == 'Oui':
        Bien_etre = st.number_input("Donnez alors une valeur entre 0 et 10.", key="Bien_etre_input")
        if 0 <= Bien_etre <= 10:
            Bien_etre = Bien_etre * 0.6 + 2.5
        else:
            st.write("La valeur donnée n'est pas cohérente. Veuillez corriger !")
    else:
        Bien_etre = 6.7

    user_input = [cont,Sej,Place,Cout_vie,Air,Bien_etre]


    user_input_scaled = scaler.transform([user_input])
    distances, indices = knn.kneighbors(user_input_scaled)
    recommended_cities = df_try.loc[indices[0], ['City','Country']].values





    st.write("Avec les renseignemens précédents on peut vous proposer les destinations suivantes :")



    st.write(f'{recommended_cities[0][0]}({recommended_cities[0][1]}),{recommended_cities[1][0]}({recommended_cities[1][1]}),{recommended_cities[2][0]}({recommended_cities[2][1]})')
    st.write(f'{recommended_cities[3][0]}({recommended_cities[3][1]}),{recommended_cities[4][0]}({recommended_cities[4][1]})')
else :
    
    X3 = [                                                 
    'Séjour euro',                                                       
    'Sur place euro',                                                    
    'Cost_of_Living_Index',                                             
    'Air_Quality_Index',                                           
    'Happiness_Score']


    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df_try[X3])

    knn = NearestNeighbors(n_neighbors=5)
    knn.fit(scaled_features)
    x = st.number_input("Quel montant souhaiteriez vous dépenser par personne pour un voyage d'une semaine tout compris ?")
    if x>=0:
        Sej = x
    else:
        st.write("La valeur donnée n'est pas cohérente. Veuillez corriger !")



    y = st.number_input('Quel est le budget quotidien par personne (hébergement compris) ?')
    if y>= 0:
        Place = y
    else :
        st.write("La valeur donnée n'est pas cohérente. Veuillez corriger !")


    Res2 = st.radio("Est ce que la coût de la vie est un critère important pour vous ?", ['Oui', 'Non'])
    if Res2 == 'Oui':
        Cout_vie = st.number_input("Donnez alors une valeur correspondant au niveau de vie entre 0 et 10.", key="Cout_vie_input")
        if 0 <= Cout_vie <= 10:
            Cout_vie = Cout_vie * 10 + 30
        else:
            st.write("La valeur donnée n'est pas cohérente. Veuillez corriger !")
    else:
        Cout_vie = 80

    Res = st.radio("Est ce que la qualité de l'air est une notion importante pour vous ?", ['Oui', 'Non'])
    if Res == 'Oui':
        Air = st.number_input("Donnez alors une valeur correspondant au niveau de la qualité de l'air souhaité entre 0 et 10 (0 : air pur, 10 : air pollué).", key="Air_input")
        if 0 <= Air <= 10:
            Air = Air * 20 + 20
        else:
            st.write("La valeur donnée n'est pas cohérente. Veuillez corriger !")
    else:
        Air = 70

    Res3 = st.radio("Est ce que le bien être dans la ville est un critère important pour vous ?", ['Oui', 'Non'])
    if Res3 == 'Oui':
        Bien_etre = st.number_input("Donnez alors une valeur entre 0 et 10.", key="Bien_etre_input")
        if 0 <= Bien_etre <= 10:
            Bien_etre = Bien_etre * 0.6 + 2.5
        else:
            st.write("La valeur donnée n'est pas cohérente. Veuillez corriger !")
    else:
        Bien_etre = 6.7

    user_input = [Sej,Place,Cout_vie,Air,Bien_etre]


    user_input_scaled = scaler.transform([user_input])
    distances, indices = knn.kneighbors(user_input_scaled)
    recommended_cities = df_try.loc[indices[0], ['City','Country']].values





    st.write("Avec les renseignemens précédents on peut vous proposer les destinations suivantes :")



    st.write(f'{recommended_cities[0][0]}({recommended_cities[0][1]}),{recommended_cities[1][0]}({recommended_cities[1][1]}),{recommended_cities[2][0]}({recommended_cities[2][1]})')
    st.write(f'{recommended_cities[3][0]}({recommended_cities[3][1]}),{recommended_cities[4][0]}({recommended_cities[4][1]})')