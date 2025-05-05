# 🎯 Student Performance Prediction

This project predicts **student performance** based on various **academic and socio-economic factors** using **Machine Learning** techniques. It follows a **modular architecture**, ensuring **scalability** and **maintainability**. The model is deployed on **Railway.app**, making it accessible through a web interface.

---

## 📌 Features
- 📊 **Preprocessing**: Cleans the dataset, handles missing values, and engineers new features.
- 🔍 **Model Training**: Compares multiple machine learning models to achieve high accuracy.
- 🎛 **Hyperparameter Tuning**: Optimizes **CatBoost** parameters using **GridSearchCV**.
- 🏗 **Modular Architecture**: The code is structured into independent components:
  - **Data Ingestion** (Loads data)
  - **Data Transformation** (Processes data)
  - **Model Training** (Builds and tunes models)
- 🌍 **Web Interface**: A user-friendly **Flask** web app with an **HTML/CSS frontend**.
- 🚀 **Deployment on Railway**: Enables **real-time predictions** via an API.
- 📈 **Performance Monitoring**: Tracks model performance over time.

---

## 🛠 Tech Stack

| Category       | Technologies Used |
|---------------|-------------------|
| **Core ML**    | Scikit-learn |
| **Backend**    | Flask, Python |
| **Frontend**   | HTML5, CSS3, JavaScript |
| **Data Processing** | Pandas, NumPy |
| **Data Visualization** | Matplotlib, Seaborn |
| **Deployment** | Railway |
| **Version Control** | Git, GitHub |

---

## 🎯 Model Performance
After extensive training and hyperparameter tuning, the model achieved an **accuracy of 86%** using **CatBoost**, which outperformed other machine learning models.

The **hyperparameter tuning** process fine-tuned parameters like:
- **Learning Rate**
- **Depth of Decision Trees**
- **Number of Iterations**
- **L2 Regularization**

The best parameters were selected using **GridSearchCV**, ensuring optimal model performance.

---

## 📂 Project Structure

```bash
mlproject/
│── artifacts/              
│   ├── data.csv           
│   ├── model.pkl           
│   ├── preprocessor.pkl     
│   ├── train.csv           
│   ├── test.csv             
│
│── catboost_info/           
│
│── Notebook/               
│   ├── EDA_Student_Performance.ipynb  
│   ├── Model_Training.ipynb           
│
│── src/                    
│   ├── Components/         
│   │   ├── data_ingestion.py         
│   │   ├── data_transformation.py     
│   │   ├── model_trainer.py           
│   │   ├── hyperparameter_tuning.py   
│   │
│   ├── Pipeline/           
│   │   ├── exception.py      
│   │   ├── logger.py        
│   │   ├── utils.py          
│── static/                 
│
│── templates/               
│   ├── index.html           
│   ├── home.html            
│
│── venv/                     
│
│── .gitignore               
│── app.py                  
│── requirements.txt         
│── Procfile                  
│── README.md                  
│── setup.py                  

