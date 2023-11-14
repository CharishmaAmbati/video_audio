import streamlit as st
from transformers import pipeline
import altair as alt

import pandas as pd

def load_view():
    st.title('Emotion Detection')
    sentences = [st.text_input("Enter Text:")]
    submit_button = st.button("Process Text")
    if submit_button:
        try:
            with st.spinner("Processing..."):

                classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=5)
                model_outputs = classifier(sentences)
            temp  = (pd.DataFrame(model_outputs[0], columns = ["label", "score"])).sort_values(by = 'score', ascending = False)
            emotion = (temp.iloc[0].label)

            st.write(f"Emotion: {emotion.title()}")

            features = temp['label'].values
            features_importances = temp['score'].values

            chart_data = pd.DataFrame()
            chart_data['features'] = features
            chart_data['feature_importance'] = features_importances

            chart_v1 = alt.Chart(chart_data).mark_bar().encode(
            x='features',
            y='feature_importance').properties(
                width=800,
                height=300
            )
            st.write("", "", chart_v1)
        except Exception as e:
            st.error(f"Error loading image from URL: {e}")


    # Choose input method (File Upload or URL)
    # input_method = st.radio("Choose input method:", ("File Upload", "URL"))
    #
    # if input_method == "File Upload":
    #     # Upload image through Streamlit
    #     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    #
    #     if uploaded_file is not None:
    #         # Convert the uploaded file to an OpenCV image
    #         image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
    #         # Use the object_detect function to display and process the image
    #         object_detect(image)
    # else:
    #     # Input image URL
    #     image_url = st.text_input("Enter image URL:")
    #     if st.button('Process URL'):
    #         try:
    #             # Read the image from the URL
    #             response = urllib.request.urlopen(image_url)
    #             image_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
    #             image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    #             # Use the object_detect function to display and process the image
    #             object_detect(image)
    #         except Exception as e:
    #             st.error(f"Error loading image from URL: {e}")
