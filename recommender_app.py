import streamlit as st
import pandas as pd
import time
import backend as backend

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid import GridUpdateMode, DataReturnMode

# Streamlit Configurations
st.set_page_config(
   page_title="Course Recommender System",
   layout="wide",
   initial_sidebar_state="expanded",
)

# ------- Functions ------

# Load datasets with caching
@st.cache_data
def load_ratings():
    return backend.load_ratings()

@st.cache_data
def load_courses():
    return backend.load_courses()

@st.cache_data
def load_course_sims():
    return backend.load_course_sims()

@st.cache_data
def load_profile():
    return backend.load_profile()

@st.cache_data
def load_courses_genre():
    return backend.load_courses_genre()

@st.cache_data
def load_bow():
    return backend.load_bow()

# Initialize app by loading datasets
def init_recommender_app():
    with st.spinner('Loading datasets...'):
        ratings_df = load_ratings()
        sim_df = load_course_sims()
        course_df = load_courses()
        course_bow_df = load_bow()
        profile_df = load_profile()
        course_genre_df = load_courses_genre()

    if course_df is None or course_df.empty:
        st.error("Error: Course dataset is empty or failed to load.")
        return None

    st.success('Datasets loaded successfully!')
    st.markdown("---")
    st.subheader("Select courses that you have audited or completed:")

    # Ensure the required columns exist
    required_columns = ['COURSE_ID', 'TITLE', 'DESCRIPTION']
    missing_columns = [col for col in required_columns if col not in course_df.columns]
    if missing_columns:
        st.error(f"Missing columns in dataset: {missing_columns}")
        return None

    # Build an interactive table for course selection
    gb = GridOptionsBuilder.from_dataframe(course_df)
    gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
    gb.configure_selection(selection_mode="multiple", use_checkbox=True)
    gb.configure_side_bar()
    grid_options = gb.build()

    response = AgGrid(
        course_df,
        gridOptions=grid_options,
        enable_enterprise_modules=True,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
        fit_columns_on_grid_load=True,
    )

    selected_courses = pd.DataFrame(response["selected_rows"], columns=['COURSE_ID', 'TITLE'])
    
    if selected_courses.empty:
        st.warning("Please select at least one course.")

    st.subheader("Your Selected Courses:")
    st.table(selected_courses)

    return selected_courses


# Model Training Function
def train(model_name, params):
    if model_name in backend.models:
        with st.spinner('Training...'):
            time.sleep(0.5)
            backend.train(model_name, params)
        st.success('Training complete!')
    else:
        st.error("Invalid model selected.")


# Prediction Function
def predict(model_name, user_ids, params):
    if not user_ids:
        st.error("No user ID provided for prediction.")
        return None

    with st.spinner('Generating course recommendations...'):
        time.sleep(0.5)
        res = backend.predict(model_name, user_ids, params)

    if res is None or res.empty:
        st.error("No recommendations generated.")
        return None

    st.success('Recommendations generated!')
    return res


# ------ UI ------
st.sidebar.title('📚 Personalized Learning Recommender')

# Initialize the app
selected_courses_df = init_recommender_app()

# Model Selection
st.sidebar.subheader('1️⃣ Select Recommendation Model')
model_selection = st.sidebar.selectbox("Select model:", backend.models)

# Hyper-parameters Configuration
params = {}

st.sidebar.subheader('2️⃣ Tune Hyper-parameters')

if model_selection == backend.models[0]:  # Course Similarity Model
    params['top_courses'] = st.sidebar.slider('Top Courses', 1, 100, 10, 1)
    params['sim_threshold'] = st.sidebar.slider('Course Similarity Threshold (%)', 0, 100, 50, 10)

elif model_selection == backend.models[1]:  # User Profile Model
    params['profile_sim_threshold'] = st.sidebar.slider('User Profile Similarity Threshold (%)', 0, 50, 30, 5)
    params['user_id'] = st.sidebar.text_input("Enter User ID")

elif model_selection == backend.models[2]:  # Clustering Model
    params['cluster_no'] = st.sidebar.slider('Number of Clusters', 1, 50, 20, 1)
    params['user_id'] = st.sidebar.text_input("Enter User ID to find similar users")

# Training
st.sidebar.subheader('3️⃣ Training')
if st.sidebar.button("Train Model"):
    train(model_selection, params)

# Prediction
st.sidebar.subheader('4️⃣ Generate Course Recommendations')
if st.sidebar.button("Recommend New Courses"):
    if selected_courses_df is not None and not selected_courses_df.empty:
        new_id = backend.add_new_ratings(selected_courses_df['COURSE_ID'].values)
        user_ids = [new_id]
        res_df = predict(model_selection, user_ids, params)

        if res_df is not None:
            res_df = res_df[['COURSE_ID', 'SCORE']]
            course_df = load_courses()
            res_df = pd.merge(res_df, course_df, on="COURSE_ID").drop('COURSE_ID', axis=1)
            st.subheader("📌 Recommended Courses")
            st.table(res_df)
    else:
        st.warning("Please select at least one course before generating recommendations.")

