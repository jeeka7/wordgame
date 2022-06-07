import streamlit as st

import random

P1,P2,P3,YOU = [None, None, None, None]
P1Sc, P2Sc, P3Sc, YOUSc = [0, 0, 0, 0]

if "P1Sc" not in st.session_state:
  st.session_state.P1Sc = 0
if "player" not in st.session_state:
  st.session_state.P2Sc = 0
if "x" not in st.session_state:
  st.session_state.P3Sc = 0
if "y" not in st.session_state:
  st.session_state.YOUSc = 0
cl1, cl2 , cl3 , cl4 = st.columns(4)

with cl1:
  st.metric(label="You", value=st.session_state.YOUSc)
with cl2:
  st.metric(label="Player 1", value=st.session_state.P1Sc)
with cl3:
  st.metric(label="Player 2", value=st.session_state.P2Sc)
with cl4:
  st.metric(label="Player 3", value=st.session_state.P3Sc)



def roll():
    global P1Sc, P2Sc, P3Sc, YOUSc
  
    Suit1 = [ "Raja","Mantri","Chor","Sipahi" ]
    P1 = random.sample(Suit1,1)
    Suit2 = [x for x in Suit1 if x not in P1]
    P2 = random.sample(Suit2,1)
    Suit3 = [x for x in Suit2 if x not in P2]
    P3 = random.sample(Suit3,1)
    Suit4 = [x for x in Suit3 if x not in P3]
    YOU = random.sample(Suit4,1)
    st.write(type(YOU))
    if (P1 == ['Raja']):
        P1Sc = P1Sc + 1000
    elif (P1 == ['Sipahi']):
        P1Sc = P1Sc + 500
    if (P2 == ['Raja']):
        P2Sc = P2Sc + 1000
    elif (P2 == ['Sipahi']):
        P2Sc = P2Sc + 500
    if (P3 == ['Raja']):
        P3Sc = P3Sc + 1000
    elif (P3 == ['Sipahi']):
        P3Sc = P3Sc + 500
    if (YOU == ['Raja']):
        YOUSc = YOUSc + 1000
    elif (YOU == ['Sipahi']):
        YOUSc = YOUSc + 500
    st.write(P1Sc,P1)
    st.write(P2Sc,P2)
    st.write(P3Sc,P3)
    st.write(YOUSc,YOU)
def guessThief():
    if (P1 == ['Mantri'])and (P2 == ['Raja']):
        P1guess = random.sample(["P3","YOU"],1)
        st.write(P1guess)
        st.write(type(P1guess))
    elif(P1 == ['Mantri'])and(P3 == ['Raja']):
        P1guess = random.sample(["P2","YOU"],1)
        st.write(P1guess)
    elif (P1 == ['Mantri'])and(YOU == ['Raja']):
        P1guess = random.sample(["P2","P3"],1)
        st.write(P1guess)
if st.button("Roll"):
  roll()
if st.button("Guess Thief"):
guessThief()
