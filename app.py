import streamlit as st
import pandas as pd
import seaborn as sns

st.write("Presentation of Dataset US Housing")

housing = pd.read_csv("USA_Housing.csv")
st.dataframe(housing)
sns.jointplot(data=housing, x="Avg. Area House Age", y="Price")
