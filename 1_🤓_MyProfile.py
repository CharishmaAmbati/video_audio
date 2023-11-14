import streamlit as st
import utils as utl
from views import home,resume,projects,configuration, emotionDetection

st.set_page_config(layout="wide", page_title="Charishma's profile", page_icon="👋",)
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

if "disabled" not in st.session_state:
    st.session_state["disabled"] = False


def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "resume":
        resume.load_view()
    elif route == "projects":
        Projects.load_view()
    elif route == "emotionDetection":
        emotionDetection.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        home.load_view()

navigation()
