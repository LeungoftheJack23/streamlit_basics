import streamlit as st
import pandas as pd
import numpy as np

# 隨機生成 IMDB 電影數據集
np.random.seed(42)
data = {
    'Movie': ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'],
    'Duration': np.random.randint(80, 180, 5),
    'IMDb Rating': np.random.uniform(1, 10, 5),
    'Genre': ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi'],
    'Director': ['Director1', 'Director2', 'Director3', 'Director4', 'Director5'],
    'Box Office Gross': np.random.randint(1000000, 100000000, 5),
    'Number of Votes': np.random.randint(1000, 100000, 5),
    'Release Year': np.random.randint(2000, 2022, 5)
}
df = pd.DataFrame(data)

# 在側邊欄選擇圖表類型
# chart_type = st.sidebar.selectbox(
#     "Select Chart Type",
#     ("Scatter Chart", "Bar Chart", "Line Chart", "Area Chart")
# )

with st.sidebar:
    chart_type = st.selectbox(
        "Select Chart Type",
        ("Scatter Chart", "Bar Chart", "Line Chart", "Area Chart")
    )

# 顯示數據表
st.write("## Movie Dataset")
st.dataframe(df)

# 根據選擇的圖表類型顯示圖表
if chart_type == "Scatter Chart":
    st.write("### Scatter Chart: Movie Duration vs IMDb Rating")
    st.write("This scatter chart shows the relationship between movie duration and IMDb rating.")
    st.scatter_chart(df[['Duration', 'IMDb Rating']])

elif chart_type == "Bar Chart":
    category = st.sidebar.selectbox("Select Category", ("Genre", "Director"))
    value = st.sidebar.selectbox("Select Value", ("Box Office Gross", "Number of Votes"))
    st.write(f"### Bar Chart: {category} vs {value}")
    st.write(f"This bar chart shows the {value} for each {category}.")
    st.bar_chart(df.set_index(category)[value])

elif chart_type == "Line Chart":
    value = st.sidebar.selectbox("Select Value", ("IMDb Rating", "Box Office Gross"))
    st.write(f"### Line Chart: Release Year vs {value}")
    st.write(f"This line chart shows the {value} over the release years.")
    st.line_chart(df.set_index('Release Year')[value])

elif chart_type == "Area Chart":
    st.write("### Area Chart: Release Year vs Box Office Gross")
    st.write("This area chart shows the box office gross over the release years.")
    st.area_chart(df.set_index('Release Year')['Box Office Gross'])