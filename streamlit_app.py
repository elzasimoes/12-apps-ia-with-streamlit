from datetime import datetime, timedelta

import streamlit as st
from streamlit_cookies_controller import CookieController

cookie_expires = datetime.now() + timedelta(days=30)
controller = CookieController()

user_id = controller.get('user_id')

if user_id is None:
    try:
        param = st.query_params['user']
        controller.set('user_id', param, expires=cookie_expires)
        st.success('User authenticated')
    except IndexError:
        st.error('Auth error')

pages = {
    f'Aplicações de Inteligência Artificial - {user_id}': [
        st.Page(
            'application_pages/franchise_linear_regression.py',
            title='1. Prevendo Custos para Abrir Franquia (Regressão)',
        ),
        st.Page(
            'application_pages/car_ml_classification.py',
            title='2. Prevendo a qualidade dos Veículos',
        ),
        st.Page(
            'application_pages/milk_production_stimated.py',
            title='3. Estimativa da Produção de Leite',
        ),
        st.Page(
            'application_pages/equipment_failure_probability_assessment.py',
            title='4. Avaliação da Probabilidade de Falha de Equipamentos',
        ),
        st.Page(
            'application_pages/data_normality_analysis.py',
            title='5. Teste de normalidade',
        ),
        st.Page(
            'application_pages/retail_recommendation_system.py',
            title='6 Sistema de Recomendação para Varejo',
        ),
        st.Page(
            'application_pages/benchmarking_temporal_series.py',
            title='7. Benchmarking de Séries Temporais',
        ),
        st.Page(
            'application_pages/analysis_of_public_accountability_data.py',
            title='8. Análise de Dados Públicos de Prestação de Conta',
        ),
        st.Page(
            'application_pages/optimize_cargo_transportation.py',
            title='9. Otimização do Lucro no Transporte de Carga',
        ),
        st.Page(
            'application_pages/genai.py',
            title='10. Produção de Imagens para Marketing',
        ),
        st.Page(
            'application_pages/finance.py',
            title='11. Análise de Dados da Bolsa de Valores',
        ),
    ],
}

pages = st.navigation(pages)
pages.run()
