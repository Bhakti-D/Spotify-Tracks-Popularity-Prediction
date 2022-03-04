import streamlit as st
import streamlit.components.v1 as components
import pickle

# load the saved model
pickle_in = open("deploy.pkl",'rb')
RFC_Model=pickle.load(pickle_in)


def predict_popularity(duration_ms, explicit, danceability,
    key, loudness, mode, speechiness, acousticness,
    instrumentalness, liveness, valence, tempo, time_signature,year):
    """
    this method is for prediction process
    takes all the Audio characteristics thtat we used for modelling and returns the prediction
    """
    prediction = RFC_Model.predict([[duration_ms, explicit, danceability,
    key, loudness, mode, speechiness, acousticness,
   instrumentalness, liveness, valence, tempo, time_signature,year]])
    print(prediction)
    return prediction


def main():
    st.title("Spotify Tracks Popularity Prediction")

    html_temp2 = """
		<div style="background-color:green;padding:5px;border-radius:5px">
		<h2 style="color:white;text-align:center;">Please enter required features</h2>
        
		</div>
		"""
    # a simple html code for heading which is in green color
    components.html(html_temp2)

    # now lets get the text input from the user by web app
    # for this we can use "st.text_input()" which allows us to get the input from the user

    duration_ms = st.text_input("duration_ms")
    explicit = st.text_input("explicit")
    danceability = st.text_input("danceability")
    key = st.text_input("key")
    loudness = st.text_input("loudness")
    mode = st.text_input("mode")
    speechiness = st.text_input("speechiness")
    acousticness = st.text_input("acousticness")
    instrumentalness = st.text_input("instrumentalness")
    liveness = st.text_input("liveness")
    valence = st.text_input("valence")
    tempo = st.text_input("tempo")
    time_signature = st.text_input("time_signature")
    year = st.text_input("year")
    result = ""


    # Done we got all the user inputs to predict and we need a button like a predict button - "st.button()"
    # After hitting the button the prediction process will go on and then we print the success message by "st.success()"
    if st.button("Predict"):
        result = predict_popularity(duration_ms, explicit, danceability,
        key, loudness, mode, speechiness, acousticness,
            instrumentalness, liveness, valence, tempo, time_signature,year)
    st.success('The Popularity of this track is {}'.format(result))



if __name__ == '__main__':
    main()