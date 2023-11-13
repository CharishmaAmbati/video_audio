import streamlit as st
import base64
from streamlit.components.v1 import html

from PATHS import NAVBAR_PATHS, SETTINGS, PROJECTS_DROPDOWN


def inject_custom_css():
    with open('assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def get_current_route():
    try:
        return st.experimental_get_query_params()['nav'][0]
    except:
        return None


def navbar_component():

    navbar_items = ''
    for key, value in NAVBAR_PATHS.items():
        navbar_items += (f'<a class="navitem" href="/?nav={value}">{key}</a>')

    settings_items = ''
    for key, value in SETTINGS.items():
        settings_items += (
            f'<a href="/?nav={value}" class="settingsNav">{key}</a>')


    component = rf'''
            <nav class="container navbar" id="navbar">
                <ul class="navlist">
                {navbar_items}
                </ul>
                <div class="dropdown" id="settingsDropDown">
                    <button style = "position:fixed; left:165px; top:2px;" class="dropbtn" data-bs-toggle="dropdown" data-bs-auto-close="true">Projects
                    <i class="fa fa-caret-down"></i></button>
                    <div id="myDropdown" class="dropdown-content">
                        {settings_items}
                    </div>
                </div>
            </nav>
            '''
    st.markdown(component, unsafe_allow_html=True)
    js = '''
    <script>
    // navbar elements
    var navigationTabs = window.parent.document.getElementsByClassName("navitem");
    var cleanNavbar = function(navigation_element) {
        navigation_element.removeAttribute('target');
    };

    for (var i = 0; i < navigationTabs.length; i++) {
        cleanNavbar(navigationTabs[i]);
    }

    // Dropdown hide / show on hover
    var dropdown = window.parent.document.getElementById("settingsDropDown");
    var dropWindow = window.parent.document.getElementById("myDropdown");

    dropdown.onmouseover = function() {
        dropWindow.style.visibility = "visible";
    };

    // Hide dropdown when not hovered
    dropdown.onmouseout = function() {
        dropWindow.style.visibility = "hidden";
    };

    var settingsNavs = window.parent.document.getElementsByClassName("settingsNav");
    var cleanSettings = function(navigation_element) {
        navigation_element.removeAttribute('target');
    };

    for (var i = 0; i < settingsNavs.length; i++) {
        cleanSettings(settingsNavs[i]);
    }
</script>
    '''
    html(js)
