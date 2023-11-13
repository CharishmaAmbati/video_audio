import streamlit as st


from pathlib import Path

import streamlit as st


# --- PATH SETTINGS ---


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Charishma Ambati"
PAGE_ICON = ":wave:"

PROJECTS = {
    "🏆 Google Generative AI learning path Certificate.",
    "🏆 IBM Data Science Professional Certificate",
    "🏆 Infosys Certified Software Programmer",
    "🏆 Professional Certificate in Artificial Intelligence and Emerging Technologies",
    "🏆 Young promising Engineer of Batch 2016-2020, BVRIT Hyderabad College of Engineering for Women"
}

Education = {
    "🎓 Master of Science -  Data Science" : "The University of Texas (2022 - 2023)",
    "🎓 Bachelor of Science - Electronics and Communications Engineering" : "BVRIT Hyderabad College of Engineering For Women - Hyderabad (2016 - 2020)"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("*Technical Resume*")
st.write("---")


# --- SKILLS ---
st.write('\n')
st.subheader("*Technical Skills*")
st.write(
    """
- ✔️ Languages: Java 17, Python 3.10
- ✔️  Technologies: HTML5, CSS3, JavaScript, JSON, React
- ✔️  Frameworks: Spring Boot, FastAPI, Pytorch, Tensorflow, sci-kit-learn,
- ✔️  Gen AI Cloud Technologies: Azure Databricks, AWS Cloud Watch, AWS Cloud Formation
- ✔️  Databases: My-SQL, Mangodb, Snowflake
- ✔️  Data Analysis: Exploratory Data Analysis, Feature Selection, pandas
- ✔️  Data Visualization: Matplotlib, Power BI
- ✔️ Application/Web Servers: Apache Tomcat Build and Configuration: Tools Maven, Jenkins
- ✔️  Version Control Tools: Git, Bitbucket
- ✔️ Project Management Tools: Jira, Apple Radar Hardware and software installation, Solutions deployment, Technical Writing Operational analysis, Build releases, Agile Engineering standards
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1

st.write("🚧", "**Software Engineer Rotational | Staples, Texas**")
st.write("2023 - Present")
st.write(
    """
- ► Developed machine learning solutions for Pricing, e-commerce, and cross-functional teams using Python and Azure Data bricks
- ► Collaborate within a 15-member Agile team, driving innovation through Machine Learning technologies
- ► Worked with NLP model to remove human interference by 80%.
- ► Implemented Transformer-based models for NLP tasks, enhancing text analysis capabilities for pricing strategies
- ► Constructed pipeline for clustering and analysis, contributing to customer product recommendations
- ► Established best practices for pragmatic programming and separation of concerns
- ► Worked on automating data from multiple formats into CSV files to unify the process using Bert-based transformers
- ► Worked on a project with e-commerce teams to include ML the current subscriptions pipelines and enhance the improve the user experience by 30%.
- ► Created a Restful Service using Fast Api and Python 3.10
- ► Technologies: Python 3.10, Azure Databricks, Snowflake, Flask, NLP, computer vision, Agile, SQL, CI/CD.

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Full Stack Developer - Systems Engineer | Apple, India**")
st.write("2020 - 2021")
st.write(
    """
- ► Engineered microservices using Java and Spring Boot, enhancing the efficiency of application components
- ► Worked with customer faced teams and worked with 70% on enhancing backend, 20 % with the front end technologies and 10% on-call support.
- ► Utilized Splunk and Radar for debugging and ticketing systems
- ► Collaborated in Agile/Scrum framework, utilizing AWS, Docker, and Git for streamlined development
- ► Used a Microservice architecture, and developed RESTFUL web services using Spring Boot framework
- ► Used Amazon Web Services (AWS) for promoting code in various Environments
- ► Used continuous build using Jenkins and supported the Application for production deployment and postproduction
- ► Technologies: Java, Spring, Spring Boot, CSS, Jenkins, REST APIs, AWS, GIT, JUnit, Radar, Splunk, Agile.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Full stack Associate Developer | TCS, India**")
st.write("2019 - 2020")
st.write(
    """
- ► I was part of the Software Development Life Cycle - SDLC in Developing a Supply Chain Application.
- ► Python 3.7 back end, incorporating machine learning techniques for vehicle routing and time series analysis
- ► Implemented Flask API and integrated React 16 for the front end, creating a seamless user experience
- ► Leveraged AWS services for cloud-based deployment and Git for source code management
- ► I worked with Professors from IIT Chennai to bring practical algorithms to the production environment
- ► Revised, and modularized old code bases to modern development standards and improved functionality
- ► Followed Agile methodology for efficient project execution
- ► Technologies: Python 3.7, Flask, HTML, CSS, Github, Eclipse, AWS and Windows, React.


"""
)

st.write('\n')
st.write("🚧", "**Full stack Trainee Developer | Talent Sprint, India**")
st.write("2017 - 2018")
st.write(
    """
- ► Deep diving into nearly 6-7 Machine Learning Algorithms.
- ► A Machine Learning model was developed to predict the class of the given aptitude question.
- ► Written self-developed code for vectorizers and ensemble algorithms. Tried applying Neural Networks like RNN, and CNN. The algorithm was 98 % percent accurate.
- ► I worked with Git for code collaboration in an Agile environment.
- ► Technologies: Python 3.4, Git, Jupyter Notebooks, AWS, and Mac.

"""
)

# --- Education ---
st.write('\n')
st.subheader("Education")
st.write("---")
for edu, place in Education.items():

    st.write(f"{edu}")
    st.write(f":blue[{place}]")

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project in PROJECTS:
    st.write(f"{project}")
