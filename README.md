
# 🎯 Course Recommendation System

A machine learning-powered course recommender that suggests personalized course options to users based on their preferences and past data. It uses content-based filtering and similarity measures to find relevant matches.

---

## 📁 Project Structure

```
Course_Recommendation_System/
├── backend.py
├── recommender_app.py
├── requirements.txt
├── course_genre.csv
├── course_processed.csv
├── courses_bows.csv
├── ratings.csv
├── sim.csv
├── user_profile.csv
├── LICENSE
└── README.md
```

---

## ✨ Features

* ✅ Recommends courses based on user preferences
* ✅ Uses cosine similarity and TF-IDF-based content filtering
* ✅ Pythonic backend logic with `pandas`, `sklearn`, and more
* ✅ Cleaned and structured datasets (`CSV`) for model input
* ✅ Modularized design (`backend.py` for logic, `recommender_app.py` as app entry)

---

## 🛠 Technologies Used

* 🐍 **Python 3**
* 📊 **pandas**, **numpy**
* 🤖 **scikit-learn** (TF-IDF, cosine similarity)
* 🗂️ **CSV** datasets (processed externally from original Excel)
* 📦 **requirements.txt** for environment setup

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/amanantuley/Course_Recommendation_System.git

# 2. Navigate to the project directory
cd Course_Recommendation_System

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
# To run the recommendation script
python recommender_app.py
```

Make sure `user_profile.csv`, `sim.csv`, and other relevant data files are in place.

---

## 🧾 Datasets

| File Name              | Description                              |
| ---------------------- | ---------------------------------------- |
| `course_genre.csv`     | Raw genres associated with each course   |
| `course_processed.csv` | Cleaned course data used in processing   |
| `courses_bows.csv`     | Bag-of-words representations             |
| `ratings.csv`          | User ratings of various courses          |
| `sim.csv`              | Similarity matrix between course vectors |
| `user_profile.csv`     | Stores user preferences and profiles     |

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---

## 🙋‍♂️ Contact

* 📧 **Email**: [amanantuley@gmail.com](mailto:amanantuley@gmail.com)
* 🐦 **Twitter**: [@amanantuley](https://twitter.com/amanantuley)
* 🔗 **LinkedIn**: [amanantuley](https://linkedin.com/in/amanantuley)
