import streamlit as set 

# find more emojis here:https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My webpage",page_icon+":trade:",layout="wide")

# ---- HEADER SECTION ---
with st.container():
    st.subheader("Hi, I am Sven :wave:")
    st.title("A Data Analyst From Germany")
    st.write(I am passionate about finding ways to use python and VBA  to be more efficient and effective in  setting" )
    st.write("[Learn More >]"(httpds://pythonandvba.com)")

# ----WHAT I DO  --
withst.container():
    st.wite("---")
    left_column, right_coloum = st.colums(2)
    with left_column:
        st.hearder("What I do")
        st.write("##")
        st.write(
            ---
            On my YouTube I am creating tutorials for people who:
            -are looking for a way to leaverage the power of python in ther day-to-day work,
            -are struggling with repetitive tasks in Exceland are looking for a way to use python and VBA
            -want to learn Data Analysis &Data Science to perform meaningful and impactful Analysis,
            -are working with Exel and found themselves thinking" "there has to be a batter way."

            if this sounds intersting to you, consider subscribing ana turning on the notifications so you 
            ---
        )
        st.wite("[YouTube  channel >](https://youtube.com/c/CodingIsFun)")















from flask import Flask


def main() -> None:
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "hello world"

    return app
