import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# ======== CONFIGURAÇÕES DO APP =========
st.set_page_config(page_title="Preço da Pizza 🍕", page_icon="🍕", layout="centered")

# ======== CSS PERSONALIZADO =========
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .titulo {
            text-align: center;
            color: #d90429;
            font-size: 40px;
            font-weight: bold;
        }
        .texto {
            text-align: center;
            color: #343a40;
            font-size: 18px;
        }
        .resultado {
            text-align: center;
            color: #1b4332;
            font-size: 22px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ======== MACHINE LEARNING =========
df = pd.read_csv('pizzas.csv')
modelo = LinearRegression()
x = df[["diametro"]]
y = df["preco"]
modelo.fit(x, y)

# ======== CONTEÚDO =========
st.markdown("<h1 class='titulo'>🍕 Preço da Pizza</h1>", unsafe_allow_html=True)
st.markdown("<p class='texto'>Descubra quanto deve custar sua pizza com base no tamanho do diâmetro!</p>", unsafe_allow_html=True)
st.divider()

diametro = st.number_input("Digite o tamanho do diâmetro da pizza (cm):", min_value=0.0, step=0.5)

if diametro > 0:
    preco_previsto = modelo.predict([[diametro]])[0]
    st.markdown(f"<p class='resultado'>O preço previsto para uma pizza de {diametro:.1f} cm é <br><strong>R$ {preco_previsto:.2f}</strong></p>", unsafe_allow_html=True)

