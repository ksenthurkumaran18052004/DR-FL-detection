# DR-FL-Detection 🩺🔍
A **Federated Learning-based Diabetic Retinopathy Detection System** using a **MobileNetV2 Teacher–Student architecture**.  

This project combines **Federated Learning (FL)** with a **Streamlit Web App**, allowing authenticated users to upload retinal images and get predictions while keeping medical data private.  

Built with **TensorFlow | Streamlit | Auth0 Authentication | Docker Ready | Cloud Deployable**.

---

## 🚀 Features
- Upload Retinal Fundus Images.
- Classifies into 5 DR categories:
  - No_DR  
  - Mild  
  - Moderate  
  - Severe  
  - Proliferative_DR  
- **Federated Learning with 5 Clients** (manual FedAvg implementation).
- Streamlit Web Application for easy interaction.
- Authenticated Login with **Auth0 Integration**.
- Client-wise Accuracy & Performance Visualization.
- Upload multiple images in a single batch.
- Metrics Visualization:
  - Confusion Matrix  
  - Class-wise Accuracy  

---

## 📂 Repository Structure
.
├── student_model_2.ipynb # Student model training notebook
├── teacher model.ipynb # Teacher model training notebook
├── student_model_mobilenetv2.h5 # Saved student model weights
├── teacher_model_mobilenetv2.h5 # Saved teacher model weights
├── app.py # Streamlit Web Application
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy code

---

## 🛠️ Tech Stack
- **Python 3.10**
- **TensorFlow / Keras**
- **Streamlit**
- **Auth0 Authentication**
- **Matplotlib, Seaborn**
- **NumPy, Pandas**

---

## ⚙️ Federated Learning Workflow
1. **Data Partitioning** – dataset is split across 5 simulated clients.  
2. **Local Training** – each client trains on its subset of data.  
3. **Federated Averaging (FedAvg)** – central server aggregates model weights.  
4. **Global Update** – averaged global model is distributed back to clients.  
5. **Evaluation** – metrics tracked per client and globally.  

---

## 📊 Results
- Evaluated on **Diabetic Retinopathy datasets** with MobileNetV2.  
- Metrics used: **Accuracy, Precision, Recall, F1-score**.  
- Comparisons between **centralized vs federated** training setups.  

(📌 Add plots/results here once finalized.)

---

## 🔮 Future Work
- Scale to **multi-institutional datasets**.  
- Integrate **blockchain for secure updates**.  
- Deploy on **multi-cloud environments**.  
- Test with **advanced federated optimizers** (e.g., FedProx, Scaffold).  

---

## 🖥️ How to Run Locally

### 1. Clone Repo
```bash
git clone https://github.com/ksenthurkumaran18052004/DR-FL-detection.git
cd DR-FL-detection
2. Create Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
3. Install Requirements
bash
Copy code
pip install -r requirements.txt
4. Run Streamlit App
bash
Copy code
streamlit run app.py
