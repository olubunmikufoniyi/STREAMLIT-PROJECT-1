import streamlit as st
import pandas as pd
import joblib

# Define the login page
def login_page():
    """Creates a login page with username and password."""
    st.title("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Replace the following placeholder with your actual authentication logic
    if username == "gomycode" and password == "gomycode_1":
        st.session_state["authenticated"] = True
        st.success("You are logged in!")
    else:
        st.error("Invalid username or password")

# Load the pre-trained model (replace with your actual model)
def load_model():
    model_path = "Models.pkl"  # Verify the correct path
    try:
        model = joblib.load("C:\\Users\\Bunmi\\Documents\\Streamlit Project\\model.pkl")
        st.success("Neural network model loaded successfully!")
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

# Define the prediction page
def predict():
    model = load_model()  # Load the model when the user selects the "Prediction" page
    st.title("Churn Prediction")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        # Make predictions
        churn_probabilities = model.predict(df) # Get probability of churn
        # Add churn probabilities as a new column to the DataFrame
        df['Churn_Probability'] = churn_probabilities
        # Display the updated DataFrame
        st.dataframe(df)

        # Save predicted data with churn probability (optional)
        if st.button("Download Results"):
            df.to_csv("churn_predictions.csv", index=False)
            st.success("Prediction results downloaded!")

def main():
    """Main application structure."""
    if "authenticated" not in st.session_state:
        st.title("Expresso Churn Prediction App")
        login_page()
        return

    st.title("Expresso Churn Prediction")
    st.write("A web app to predict customer churn for Expresso, a telecommunications company in Africa.")

    page = st.sidebar.selectbox("Select a page", ["Home", "Prediction"])

    if page == "Home":
        st.header("About Expresso")
        st.write(
            "Expresso provides telecommunication services in Mauritania and Senegal. This web app helps predict customer churn, allowing Expresso to take proactive measures and retain valuable clients."
        )

    if page == "Prediction":
        predict()

if __name__ == "__main__":
    main()
