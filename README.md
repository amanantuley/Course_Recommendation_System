# Course-Recommendation-System
The provided code is a course recommendation system implemented using Streamlit, a Python framework for building interactive web applications. The system allows users to select courses they have audited or completed and provides personalized recommendations based on different recommendation models.

The code consists of several functions and components:

1. Data Loading: The system loads various datasets such as ratings, course similarities, user profiles, course genre information, and bag-of-words representation of courses.

2. App Initialization: The init__recommender_app() function initializes the recommender app by loading the datasets and allowing users to select courses they have audited or completed using an interactive table.

3. Training: The system supports training different recommendation models. Currently, it includes the "Course Similarity," "User Profile," and "Clustering" models. The train() function is responsible for training the selected model with the specified hyperparameters.

4. Prediction: Once the model is trained, the system generates course recommendations based on the selected model and user inputs. The predict() function takes the model name, user IDs, and additional parameters as input and returns the recommended courses.

5. User Interface: The system's user interface is built using Streamlit. It includes a sidebar that allows users to select the recommendation model, tune hyperparameters, train the model, and generate course recommendations. The selected courses, model parameters, and recommendations are displayed in the main content area.

The code provides a basic implementation of the course recommendation system and can be extended with additional models and functionalities. It demonstrates the integration of Streamlit for building interactive web applications and the usage of different recommendation techniques such as course similarity, user profiling, and clustering.
