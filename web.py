import streamlit as st
import pandas as pd
import altair as alt

st.title("Indian Textile Export")

data = {
    "Year": ["2017-18", "2018-19", "2019-20", "2020-21", "2021-22", "2022-23"],
    "Readymade Garment": [16707, 16138, 15488, 12272, 16015, 16192],
    "Cotton Textiles": [11212, 12405, 10263, 11128, 17166, 11083],
    "Man-made Textiles": [5413, 5551, 5324, 4180, 6294, 5411],
    "Wool & Woolen Textiles": [187, 222, 181, 109, 166, 205],
    "Silk Products": [69, 76, 72, 76, 109, 94],
    "Handloom Products": [356, 344, 319, 223, 269, 182],
    "Carpets": [1430, 1482, 1373, 1491, 1790, 1366],
    "Jute Products": [350, 340, 357, 397, 537, 462],
    "Total Textile & Apparel": [35723, 36559, 33379, 29877, 42347, 34995],
    "Handicrafts": [1823, 1838, 1798, 1708, 2088, 1689],
    "Total T&A including Handicrafts": [37546, 38397, 35177, 31585, 44435, 36684]
}

df = pd.DataFrame(data)
st.write(df)




st.subheader("Readymade Garment Production Over Years")

# Set index to Year
df = df.set_index("Year")

# Create Altair chart
chart = alt.Chart(df.reset_index()).mark_bar(color='yellow').encode(
    x='Year',
    y='Readymade Garment'
).properties(
    width=700,  # Adjust width as needed
    height=500  # Adjust height as needed
)

# Display Altair chart
st.altair_chart(chart, use_container_width=True)

# Additional information
st.markdown("****")

st.subheader("Cotton Textile Production Over Years")


chart2=alt.Chart(df.reset_index()).mark_bar(color="Grey").encode(
    x='Year',
    y="Cotton Textiles"
).properties(
    width=700,
    height=500
)
st.altair_chart(chart2,use_container_width=True)
st.markdown("---")


st.subheader("Man-made Textile Production Over Years")

chart3=alt.Chart(df.reset_index()).mark_bar(color="black").encode(
    x="Year",
    y="Man-made Textiles"
).properties(
    width=700,
    height=500
)
st.altair_chart(chart3,use_container_width=True)
st.markdown("---")

st.subheader("Wool & Woolen Textiles Production Over Years")
chart4=alt.Chart(df.reset_index()).mark_bar(color=" brown").encode(
    x="Year",
    y="Wool & Woolen Textiles"
).properties(
    width=500,
    height=500
)
st.altair_chart(chart4,use_container_width=True)
st.markdown("---")

st.subheader("Silk Products Production Over Years")
chart5=alt.Chart(df.reset_index()).mark_bar(color="skyblue").encode(
    x="Year",
    y="Silk Products"
).properties(
    width=700,
    height=500
)
st.altair_chart(chart5,use_container_width=True)
st.markdown("---")

st.altair_chart(chart4,use_container_width=True)
st.markdown("---")


st.subheader("Handloom Products Production Over Years")
chart6=alt.Chart(df.reset_index()).mark_bar(color="hotpink").encode(
    x="Year",
    y="Handloom Products"
).properties(
    width=700,
    height=500
)
st.altair_chart(chart6,use_container_width=True)
st.markdown("---")

st.subheader("Carpet Products Production Over Years")
chart7=alt.Chart(df.reset_index()).mark_bar(color="red").encode(
    x="Year",
    y="Carpets"
).properties(
    width=700,
    height=500
)
st.altair_chart(chart7,use_container_width=True)
st.markdown("---")

st.subheader("Jute Products Production Over Years")


chart8=alt.Chart(df.reset_index()).mark_bar(color="yellowgreen").encode(
    x="Year",
    y="Jute Products"
).properties(
    width=700,
    height=500
)
st.altair_chart(chart8,use_container_width=True)
st.markdown("---")


st.subheader("Handicraft")

chart9=alt.Chart(df.reset_index()).mark_bar(color="cyan").encode(
    x="Year",
    y="Handicrafts"
).properties(
    width=700,
    height=500
)
st.altair_chart(chart9,use_container_width=True)
st.markdown("---")
