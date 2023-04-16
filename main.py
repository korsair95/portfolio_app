import json
import streamlit as st
from streamlit_lottie import st_lottie


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile("images/88252-data-security.json")


st.set_page_config(page_title="My Webpage", layout="wide")

st.subheader("Hi, I am Paweł")
st.title("A Cybersecurity enthusiast from Poland")
st.write(
        """I am passionate about cybersecurity topics since 2020, at the beginning as a hobby (on CTF platforms like HTB or OS Proving Grounds) and from 2022 commercially working in a Cybersecurity Team. 
        """
    )

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write(
            """
            - I am constantly learning since my Cybersecurity journey is still at the beginning phase
            - I worked for a year and a half as a Project Manager for Santander Poland coordinating projects of implementation cloud technologies (based on Azure) and cybersecurity technologies within The Cybersecurity Transformation Programme
            - In 2023 I started to develop python skills to help me automate some of tasks related to the cybersecurity (also in  2023 decided to learn Spanish if we are speaking about new languages ☺️ )
            - Developing skills related to cloud 
            - I like to spend my free time with a good read
                        """
        )
    with right_column:
        st_lottie(lottie_coding, height=350, key="coding")
        
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    ln, mail, resume, github  = st.columns(4)
    with ln:
        st.image("images/linkedin.png", width=50)
        st.write("[LinkedIn](https://www.linkedin.com/in/pawel-bedra/)")
    with mail:
        st.image("images/gmail.png", width=50)
        st.markdown('<a href="mailto:p.bedra95@gmail.com">E-mail</a>', unsafe_allow_html=True)
    with resume:
        st.image("images/cv.png", width=50)
        st.write("[My Resume](https://drive.google.com/file/d/1CaBAspOTQr1ij2Y7E5kofEXhFksJQnDr/view?usp=sharing)")
    with github:
        st.image("images/icons8-github-logo-96.png", width=50)
        st.write("[Github](https://github.com/korsair95)")



