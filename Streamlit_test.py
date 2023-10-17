import time
import streamlit as st
import numpy as np
import pandas as pd
import time

st.write("Here we do some Magic!!!")

df1 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

my_table = st.table(df1)

df2 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

my_table.add_rows(df2)

my_chart = st.line_chart(df1)
my_chart.add_rows(df2)


# def get_user_name():
#     return 'John'

# with st.echo():
#     # Everything inside this block will be both printed to the screen
#     # and executed.

#     def get_punctuation():
#         return '!!!'

#     greeting = "Hi there, "
#     value = get_user_name()
#     punctuation = get_punctuation()

#     # st.write(greeting, value, punctuation)

# # And now we're back to _not_ printing to the screen
# foo = 'bar'
# st.write('Done!')

# with st.form("my_form"):
#     st.write("Inside the form")
#     slider_val = st.slider("Form slider")
#     checkbox_val = st.checkbox("Form checkbox")

#     # Every form must have a submit button.
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.write("slider", slider_val, "checkbox", checkbox_val)

# st.write("Outside the form")

# st.info('This is a purely informational message', icon="ℹ️")
# st.success('This is a success message!', icon="✅")
# e = RuntimeError('This is an exception of type RuntimeError')
# st.exception(e)

# st.balloons()
# time.sleep(1)
# with st.form(key='my_form'):
#     username=st.text_input("Enter Your Name:")
#     submit=st.form_submit_button("Submit")
#     if submit:
#         st.snow()
#         time.sleep(1)
#     else:
#         st.stop()
# st.error('This is an error', icon="🚨")


# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     # Update the progress bar with each iteration.
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i + 1)
#     time.sleep(0.01)

# '...and now we\'re done!'

# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"])
#     st.write(f"You are in {chosen} house!")


# Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })

# option = st.selectbox(
#     'Which number do you like best?',
#     df['first column'])

# 'You selected: ', option


# if st.checkbox('Show data frame: '):
#      chart_data = pd.DataFrame(
#           np.random.randn(10,3),
#           columns=['A','B','C']
#      )
#      chart_data

# st.text_input("Your name: ",key="name")
# st.session_state.name

# x = st.slider(f'x\u00b2')  # 👈 this is a widget
# st.write(x, '\u00b2 is:', x * x)
