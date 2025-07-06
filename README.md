# DR-FL-detection 🩺🔍
A Federated Learning-based Diabetic Retinopathy Detection System using MobileNetV2 student-teacher architecture.

Built with TensorFlow | Streamlit | Auth0 Authentication | Docker Ready | Cloud Deployable.

---

## Features:
- Upload Retinal Images
- Classifies into:
  - No_DR
  - Mild
  - Moderate
  - Severe
  - Proliferate_DR
- Federated Learning with 5 Clients
- Streamlit Web App
- Authenticated Login (Auth0 Integrated)
- Client-wise Accuracy & Visualization
- Upload Multiple Images
- Metrics Visualization (Confusion Matrix, Class-wise Accuracy)

---

## Tech Stack:
- Python 3.10
- TensorFlow / Keras
- Streamlit
- Auth0 Authentication
- Matplotlib, Seaborn
- Pandas, NumPy

---

## How to Run Locally:

> 1. Clone Repo:


git clone https://github.com/ksenthurkumaran18052004/DR-FL-detection.git
cd DR-FL-detection
Create Virtual Environment:

python -m venv venv
venv\Scripts\activate  # Windows
Install Requirements:


pip install -r requirements.txt
Run Streamlit App:


streamlit run app.py

