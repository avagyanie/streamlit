from time import sleep
import streamlit as st
# import pandas as pd
import plotly.express as px

with st.echo():
    st.title("My Streamlit App")
    st.header("Welcome!")
    st.subheader("text")
    st.markdown("This is a markdown block. You can write *italic*, **bold**, or even use [links](https://www.youtube.com/watch?v=_Z0JVmqZzeo)")
    # st.balloons()
    # st.snow()

st.divider()

with st.echo():
    st.latex(r"Y = \alpha + \beta X_i")

with st.echo():
    st.write("You can also use LaTeX for mathematical expressions like this: $E = mc^2$")

st.divider()

st.subheader("Tables")

with st.echo():
    st.dataframe([{"Name": "Գինի", "age": 3}, {"Name": "Պանիր", "age": 1}])

st.divider()

with st.echo():
    st.json({
        "Product": "Պանիր",
        "Type": "Չանախ",
    })

st.divider()

# Plotly
st.subheader("Plotly Bar Chart")

# with st.echo():
#     st.divider()
#     fig = px.bar(df, x = "Name", y = "Age")
#     st.plotly_chart(fig)

with st.echo():
    st.line_chart([10, 20, 45, 8, 109, 70, 28, 3, 57])

st.divider()

st.subheader("Interactive Widgets")

with st.echo():
    if st.button("Click me!"):
        st.write("Button clicked!")

with st.echo():
    checkbox_value = st.checkbox("Check me!")
    if checkbox_value:
        st.write("Checkbox checked!")

with st.echo():
    option = st.selectbox("Choose an option", ["Option1", "Option2", "Option3"])
    st.write("You selected:", option)

with st.echo():
    slider_value = st.slider("Slide me", 0, 100, step=5)
    st.write("Slider value:", slider_value)

with st.echo():
    num_input_value = st.number_input("Num input", min_value=0.0, max_value=100.0, step=5.0)
    st.write("Number input value:", num_input_value)


with st.echo():
    text = st.text_input("Please input text")
    st.write("Text input value:", text)

with st.echo():
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file is not None:
        st.write("File uploaded")

# with st.echo():
#     progress_bar = st.progress(0)

#     for i in range(100):
#         sleep(0.1)
#         progress_bar.progress(i)

st.divider()

with st.echo():
    st.sidebar.header("Sidebar")
    st.sidebar.text("This iis a sidebar")

st.divider()

with st.echo():
    rating1 = st.feedback("stars")
    rating2 = st.feedback("faces")
    st.write(f"Rating 1: {rating1}")
    st.write(f"Rating 2: {rating2}")

st.divider()

with st.echo():
    color = st.color_picker("Pick a color")
    st.write("You picked a color", color)

st.divider()

with st.echo():
    enable = st.checkbox("Enable camera")
    picture = st.camera_input("Take a picture", disabled=not enable)

    if picture:
        st.image(picture)

# with st.echo():
#     audio_value = st.audio_input("Record a voice message")

#     if audio_value:
#         st.audio(audio_value)

# with st.echo():
#     audio_value = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

#     if audio_value:
#         st.audio(audio_value)

with st.echo():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("A cat")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJUAkS7ARQvvaNaxlwiFUNF2b1A1laot-uUw&s")
    
    with col2:
        st.header("A dog")
        st.image("https://petzyo.com.au/cdn/shop/articles/Poodle.png?v=1656027168&width=1024")
    
    with col3:
        st.header("A bird")
        st.image("https://rangerrick.org/wp-content/uploads/2020/06/Call-a-Bird-Activity-Hero.jpg")

    