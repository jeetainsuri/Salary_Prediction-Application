import joblib   ## this library is used to read the model file.
import streamlit as st   ## used to make this model in form of webpage. Go to its website and see its docs to learn about it more.
st.set_page_config(page_title="My Salary Prediction Model", page_icon = "😎")   ## page_title is title of the page and page_icon is used to give page an icon.
st.title("Machine learning Model Deployment")   ## st.title used for giving heading.
st.write ("""My *Salary prediction* model VS Experience""")   ## This is used to write any text. The text between the stars will appear italic, but the text between double star will                                                                                                                     ## appear bold.
mymodel = joblib.load('salary.pkl')   ## Now what to do if we want to get the input from the user, we can use text column but we are using silder. Everything is in documentation.
exp = st.sidebar.slider("Experience (in Years)",1.0,50.0,2.0)   ## 1.0 is min value, 50.0 is max value and 2.0 is default value.
                                                                                        ## exp = float(input("Enter Years:")), this the code before webpage, but now the value selected from the slider will be input to exp.
salary = mymodel.predict([[exp]])
st.write(f"Experience -",exp)   ## At first this was the code = print(salary), now this code will give output with respect to the exp.
st.write(f"Salary -",round(float(salary)))   ## This salary is an array data so that we are getting it in form of table, so we convert it into float. But now we are getting a very large decimal value so we would use round function to roundoff. 

## We have made a web page but only i can use it, so in orer to make others use it, we will deploy it on heroku server.
## The git folder which is hidden will store all the updates related to the application.