import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1

st.title('Happy First Monthiversary My Baachhhaaa... 😘 😘 😘')

def set_step(value):
    st.session_state.step = value

if st.session_state.step == 1:
    st.button('Show me the gift', key='step_1_button', on_click=set_step, args=(2,))

elif st.session_state.step == 2:
    st.write('''
    Hello Babbyyy... 😘 😘 😘,''')
    st.write('''    This is a Simple Little Gift for My Cuttieee Piee, I hope you like it. I hope this little gift can make you smile and feel loved. You are the most important person in my life and I want to make you happy. I love you so much and I will always be here for you. *Happy First Monthiversary! 😋 😋 😘 😘 ❤️ ❤️*''')
    st.write('''I have designed a Little Code as a gift, Hope You Like It... 😋 😘''')

    st.button('Show me the next question', key='step_2_button', on_click=set_step, args=(3,))

elif st.session_state.step == 3:
    st.write('''
    I have a question for you, Do You Love Me? 😘''')
    st.button('Yes, I Do! ❤️', key='step_3_button_yes', on_click=set_step, args=(4,))
    st.button('No, I Don\'t! 😢', key='step_3_button_no', on_click=set_step, args=(5,))
    st.button('Maybe? 😐', key='step_3_button_maybe', on_click=set_step, args=(6,))

elif st.session_state.step == 4:
    st.write('Awwww... I Love You Morree My Baachhhaaa... 😘 😘 😘')
    st.button('Next Step Please! 😋', key='step_4_button', on_click=set_step, args=(8,))

elif st.session_state.step == 5:
    st.write('Happ Bad Gurll... Jhooth Bolti ho... 😏 😏 😁')
    op1 = st.button('I Love You Yrrr... 😋 😁 ❤️', key='step_3_button_no_yes', on_click=set_step, args=(4,))
    op2 = st.button('I Don\'t Love You... 😤', key='step_3_button_no_no', on_click=set_step, args=(7,))

elif st.session_state.step == 6:
    st.write('What Maybe??? 😑 😑 😑')
    st.button('I Love You More! ❤️', key='step_3_button_maybe_yes', on_click=set_step, args=(4,))
    st.button('I Don\'t Love You! 😢', key='step_3_button_maybe_no', on_click=set_step, args=(7,))

elif st.session_state.step == 7:
    st.write('Nhi Karni Mujhee Baat ab... 🤧 🤧 🤧')
    st.write('This is the end of the app.')
    st.stop()

elif st.session_state.step == 8:
    st.write('When did we first talk to each other on IG? 😘')
    st.write('(Write the date in this format: DD MMM YYYY, e.g., 01 Jan 2020)')
    op1 = st.text_input('Enter your answer here...', key='step_8_input')
    chances = 0
    if op1:
        if op1.strip().lower() == '04 Jan 2026'.lower():
            st.write('Correct Answer! 😘 😘 😘')
            st.button('Next Step Please! 😋', key='step_8_button', on_click=set_step, args=(9,))
        else:
            st.write('Wrong Answer! Try Again... 😢')
            chances += 1
            if chances >= 3:
                st.write('You have used all your chances! The correct answer was 04 Jan 2026. 😢')
                st.button('Next Step Please! 😋', key='step_8_button_fail', on_click=set_step, args=(9,))

elif st.session_state.step == 9:
    st.write('When did I Propose You? 😘')
    st.write('(Write the date in this format: DD MMM YYYY, e.g., 01 Jan 2020)')
    op1 = st.text_input('Enter your answer here...', key='step_9_input')
    chances = 0
    if op1:
        if op1.strip().lower() == '15 Mar 2026'.lower():
            st.write('Correct Answer! 😘 😘 😘')
            st.button('Next Step Please! 😋', key='step_9_button', on_click=set_step, args=(10,))
        else:
            st.write('Wrong Answer! Try Again... 😢')
            chances += 1
            if chances >= 3:
                st.write('You have used all your chances! The correct answer was 15 Mar 2026. 😢')
                st.button('Next Step Please! 😋', key='step_9_button_fail', on_click=set_step, args=(10,))
                
elif st.session_state.step == 10:
    st.write('When did I first show you My Dihh... 🙈 🙈 🙈')
    st.write('(Write the date in this format: DD MMM YYYY, e.g., 01 Jan 2020)')
    op1 = st.text_input('Enter your answer here...', key='step_10_input')
    chances = 0
    if op1:
        if op1.strip().lower() == '03 Apr 2026'.lower():
            st.write('Correct Answer! 🫣 🫣 🫣')
            st.button('Finish! 😋', key='step_10_button', on_click=set_step, args=(11,))
        else:
            st.write('Wrong Answer! Try Again... 😢')
            chances += 1
            if chances >= 3:
                st.write('You have used all your chances! The correct answer was 20 Apr 2026. 😢')
                st.button('Finish! 😋', key='step_10_button_fail', on_click=set_step, args=(11,))

elif st.session_state.step == 11:
    st.write('Awwwwww... Merraa Bachhaaa... I hope this sweet surprise made you smile... 😘 😘 😘')
    st.write('(More cute gifts may come later... 😋 😋 😋)')
    st.button('End The App...', key='step_11_button', on_click=set_step, args=(12,))

elif st.session_state.step == 12:
    st.write('Thank you, my love. This is now ending Of This App. 😘 😘 😘')
    st.stop()
