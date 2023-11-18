import streamlit as st
import numpy as np
import pandas as pd

# Main
st.title ("Esta es mi primera aplicación")
datos = pd.DataFrame(
	np.random.randn(20, 3),
	columns = ['a', 'b', 'c'])


st.write('aaa')
st.line_chart(datos)
aa = st.number_input(label='titulo')

st.dataframe(datos)
