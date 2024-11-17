import streamlit as st

pages = {
    '12 Aplicações Web de Inteligência Artificial': [
        st.Page(
            'franchise_linear_regression.py',
            title='1. Prevendo Custos para Abrir Franquia (Regressão)',
        ),
        st.Page(
            'car_ml_classification.py',
            title='2. Prevendo a qualidade dos Veículos',
        ),
        st.Page(
            'milk_production_stimated.py',
            title='3. Estimativa da Produção de Leite',
        ),
    ],
}

pages = st.navigation(pages)
pages.run()
