import streamlit as st

# Create input fields for user input
st.title("FLIGHT CANCELLATION PREDICTION PROJECT APP")

# Create input fields for user input
DEP_HOUR = st.sidebar.slider("Departure Hour", 0, 23, step=1)
DISTANCE = st.sidebar.number_input("Distance (miles)")
LATITUDE = st.sidebar.slider("Latitude", 18.0, 64.0, step=1.0)
LONGITUDE = st.sidebar.slider("Longitude", -150.0, -50.0, step=1.0)
TEMPERATURE = st.sidebar.slider("Temperature", -20.0, 42.0, step=1.0)
DEW_POINT = st.sidebar.slider("Dew point", -20.0, 30.0, step=1.0)
REL_HUMIDITY = st.sidebar.slider("Relative humidity", 2.0, 100.0, step=1.0)
LOWEST_CLOUD_LAYER = st.sidebar.slider("Lowest Cloud Layer", 0.0, 33000.0, step=100.0)
MONTH = st.sidebar.slider("Month", 1, 12, step=1)
WIND_SPD = st.sidebar.slider("Wind Speed", 0.0, 32.0, step=1.0)
WIND_GUST = st.sidebar.slider("Wind Gust", 0.0, 55.0, step=1.0)
VISIBILITY = st.sidebar.slider("Visibility", 0.0, 10.0, step=1.0)
ALTIMETER = st.sidebar.slider("Atmospheric Pressure", 25.0, 31.0, step=0.1)
ICAO_TYPE = st.sidebar.selectbox("ICAO Type", ['A321', 'B39M', 'E75L', 'B737',
                                               'A320', 'A319', 'B38M', 'B738', 'CRJ2', 'A20N', 'CRJ7',
                                               'B712', 'E145', 'CRJ9', 'B739', 'B77W', 'A21N',
                                               'B752', 'B764', 'E170', 'E190', 'BCS3', 'B772', 'BCS1',
                                               'B789', 'DH8D', 'A332', 'B753', 'B763', 'B78X', 'A333',
                                               'B788', 'A339', 'A359'])
ORIGIN_STATE_NAME = st.sidebar.selectbox("Origin State Name", ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California',
                                                              'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
                                                              'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana',
                                                              'Kansas', 'Kentucky', 'Louisiana', 'Massachusetts',
                                                              'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri',
                                                              'Mississippi', 'Montana', 'North Carolina', 'North Dakota',
                                                              'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico',
                                                              'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon',
                                                              'Pennsylvania', 'Puerto Rico', 'Rhode Island',
                                                              'South Carolina', 'South Dakota', 'Tennessee',
                                                              'U.S. Pacific Trust Territories and Possessions', 'Texas',
                                                              'Utah', 'Virginia', 'U.S. Virgin Islands', 'Vermont',
                                                              'Washington', 'Wisconsin', 'West Virginia', 'Wyoming'])
RANGE = st.sidebar.selectbox("Range", ["Short Range", "Medium Range", "Long Range"])
WIDTH = st.sidebar.selectbox("Width", ["Narrow-body", "Wide-body"])
ACTIVE_WEATHER = st.sidebar.select_slider("Active Weather", [0.0, 1.0, 2.0])
CLOUD_COVER = st.sidebar.select_slider("Cloud Cover", [1.0, 2.0, 3.0, 4.0, 0.0])
N_CLOUD_LAYER = st.sidebar.select_slider("N_Cloud Layer", [1.0, 3.0, 0.0, 2.0, 4.0])

# Define a function to make predictions based on user input
def predict_cancellation(DEP_HOUR, ACTIVE_WEATHER):
    if DEP_HOUR == 0 and ACTIVE_WEATHER == 2.0:
        prediction = 'Weather Cancellation'
        image_path = "Weather_cancelled_image.jpg"
    elif DEP_HOUR == 0 and ACTIVE_WEATHER == 1.0:
        prediction = 'Carrier Cancellation'
        image_path = "Weather_cancelled_image.jpg"
    else:
        prediction = 'Flight not Cancelled'
        image_path = "not_cancelled_image.jpg"
    
    return prediction, image_path

# Create a prediction button
prediction_button = st.sidebar.button("Predict Cancellation")

# Perform prediction when the button is clicked
if prediction_button:
    prediction, image_path = predict_cancellation(DEP_HOUR, ACTIVE_WEATHER)
    st.write(f'Prediction: {prediction}', font=('Arial', 24, 'bold'))
    st.image(image_path)
