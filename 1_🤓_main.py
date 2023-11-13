import streamlit as st

st.set_page_config(
    page_title="Charishma Ambati's Profile",
    page_icon="👋",
)

st.title("Charishma Ambati")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)





# import streamlit as st
# import pandas as pd
#
# st.write("""
# # My profile
# """)
#
# df = pd.DataFrame([1, 4, 6, 8, 10, 25, 1000])
#
#
#
# # from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
# # import torch
# # from PIL import Image
# # import requests
# # from io import BytesIO
# #
# # model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
# # feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
# # tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
# #
# # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# # model.to(device)
# #
# #
# #
# # max_length = 16
# # num_beams = 4
# # gen_kwargs = {"max_length": max_length, "num_beams": num_beams}
# # def predict_step(image_paths):
# #     images = []
# #     for image_path in image_paths:
# #         try:
# #             response = requests.get(image_path)
# #             i_image = Image.open(BytesIO(response.content))
# #         except:
# #             i_image = Image.open(image_path)
# #     if i_image.mode != "RGB":
# #         i_image = i_image.convert(mode="RGB")
# #     images.append(i_image)
# #
# #     pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
# #     pixel_values = pixel_values.to(device)
# #
# #     output_ids = model.generate(pixel_values, **gen_kwargs)
# #
# #     preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
# #
# #     preds = [pred.strip() for pred in preds]
# #     return preds
# #
# # print("DOne")
# # print(predict_step(['https://i.pinimg.com/originals/37/8f/fa/378ffa7b4bc07f190ee35f85ed816377.jpg']))
# # print("Done")
# st.button(page="models")
# print("start")
# import cv2
# import matplotlib.pyplot as plt
# from deepface import DeepFace
# import requests
# from io import BytesIO
# import urllib
# import numpy as np
#
#
# import cv2
# from fer import FER
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
#
#
# path = 'https://i.pinimg.com/originals/37/8f/fa/378ffa7b4bc07f190ee35f85ed816377.jpg'
#
# # read image
# try:
#     req = urllib.request.urlopen(path)
#     arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
#     img = cv2.imdecode(arr, -1)
# except:
#     img = cv2.imread(path)
# st.image(img, caption='Sunrise by the mountains')
# emotion_detector = FER(mtcnn=True)
# # result = emotion_detector.detect_emotions(input_image)
# # print(result)
# # print(type(img))
# # plt.imshow(img[:, :, : : -1])
# #
# # # display that image
# # plt.show()
# # result = DeepFace.analyze(img,
# #                           actions = ['emotion'])
# #
# # # print result
# # print(result)
#
# # input_image = img
# # emotion_detector = FER(mtcnn=True)
# # result = emotion_detector.detect_emotions(input_image)
# # st.write(result)
