import streamlit as st
import joblib
import pandas as pd

teams=['Rajasthan Royals',
 'Royal Challengers Bangalore',
 'Sunrisers Hyderabad',
 'Delhi Capitals',
 'Chennai Super Kings',
 'Gujarat Titans',
 'Lucknow Super Giants',
 'Kolkata Knight Riders',
 'Mumbai Indians',
 'Kings XI Punjab']

cities=['Ahmedabad', 'Kolkata', 'Mumbai', 'Navi Mumbai', 'Pune', 'Dubai',
       'Sharjah', 'Abu Dhabi', 'Delhi', 'Chennai', 'Hyderabad',
       'Visakhapatnam', 'Chandigarh', 'Bengaluru', 'Jaipur', 'Indore',
       'Bangalore', 'Raipur', 'Ranchi', 'Cuttack', 'Dharamsala',
       'Johannesburg', 'Centurion', 'Durban', 'Bloemfontein',
       'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town']

pipe = joblib.load('pipe1.joblib')

st.title('IPL Win Predictor')

col1, col2=st.columns(2)

with col1:
    Batting_Team=st.selectbox('Select the Batting Team', sorted(teams))
with col2:
    Bowling_Team=st.selectbox('Select the Bowling Team',sorted(teams))
    
City=st.selectbox('Select the stadium',sorted(cities))

target=st.number_input('Target')

col3,col4,col5=st.columns(3)

with col3:
    score=st.number_input('Score')
with col4:
    overs=st.number_input('Overs Completed')
with col5:
    wickets=st.number_input('Wickets')
    
if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left
    input_df = pd.DataFrame({'BattingTeam': [Batting_Team], 'BowlingTeam': [Bowling_Team], 'City': [City],
                  'runs_left': [runs_left], 'balls_left': [balls_left],
                  'wickets_left': [wickets_left], 'total_run_x': [target], 'crr': [crr], 'rrr': [rrr]})
    result = pipe.predict_proba(input_df)
    loss=result[0][0]
    win=result[0][1]
    st.header(Batting_Team+"-"+str(round(win*100))+"%")
    st.header(Bowling_Team+"-"+str(round(loss*100))+"%")