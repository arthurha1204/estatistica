import streamlit as st
from plot.interactive import plot_line_i

st.title('Jogo do Bicho')

st.sidebar.header('User Input')
symbol = st.sidebar.text_input('Escolha um ativo:','AAPL')
st.write(symbol)

fig = plot_line_i(symbol)
st.plotly_chart(fig)
