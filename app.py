import streamlit as st
from auth import auth_login
from tensorflow.keras.models import load_model
from utils.preprocess import preprocess_image
from PIL import Image
import numpy as np

# Authentication
if 'user' not in st.session_state:
    if not auth_login():
        st.stop()

st.sidebar.success(f"Welcome {st.session_state['user']['name']} 👋")

st.title("Diabetic Retinopathy Detection Web App")

model = load_model('model/vidamuyarchi_student_model.h5')
class_names = ['Mild', 'Moderate', 'No_DR', 'Proliferate_DR', 'Severe']

uploaded_files = st.file_uploader("Upload Eye Images", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="file_uploader")

# Clear All Button
if st.button("Clear All Files", type="primary"):
    # Clear uploaded file input and reset session
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()

if uploaded_files:
    cols = st.columns(3)
    for idx, uploaded_file in enumerate(uploaded_files):
        col = cols[idx % 3]
        with col:
            image = Image.open(uploaded_file)
            st.image(image, caption=uploaded_file.name, width=250)

            img_array = preprocess_image(image)
            pred = model.predict(np.expand_dims(img_array, axis=0))[0]
            predicted_class = class_names[np.argmax(pred)]
            confidence = np.max(pred) * 100

            st.markdown(f"#### Prediction: :green[{predicted_class}]")
            st.markdown(f"Confidence: :blue[{confidence:.2f}%]")

            for i, prob in enumerate(pred):
                st.write(f"{class_names[i]} : {prob*100:.2f}%")

        if (idx + 1) % 3 == 0:
            st.markdown("---")
