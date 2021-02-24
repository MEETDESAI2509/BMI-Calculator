import streamlit as st

Title_html = """
    <style>
        .title h1{
          user-select: none;
          font-size: 60px;
          color: black;
        }
        @keyframes slide {
          0%{
            background-position-x: 0%;
          }
          100%{
            background-position-x: 600vw;
          }
        }
    </style> 

    <div class="title">
        <h1>BMI CALCULATOR</h1>
    </div>
    """
img='BMI-Calculator.jpg'
st.sidebar.image(img)
l1=['SI','USC']
metric=st.sidebar.selectbox('Select metric system',l1)
st.markdown(Title_html, unsafe_allow_html=True)  # Title rendering
st.markdown("""<style>body {background-color: #99ddff;}</style>""", unsafe_allow_html=True)
if metric=='SI':
    height=st.sidebar.slider("Select height in metres",0.75,2.3)
    weight=st.sidebar.slider("Select weight in kgs",10,150)
    bmi = weight/(height * height)
    if st.sidebar.button('Done'):
        bmi = round(bmi, 2)
        st.subheader("Your BMI is: " + str(bmi))
else:
    height = st.sidebar.slider("Select height in inches", 29, 91)
    weight = st.sidebar.slider("Select weight in pounds", 10, 330)
    bmi=703*(weight/(height*height))
    if st.sidebar.button('Done'):
        bmi = round(bmi, 2)
        st.subheader("Your BMI is: " + str(bmi))

if bmi>25:
    st.subheader("You are overweight!")
    body_html = """
            <style>
                .title h1{
                  user-select: none;
                  font-size: 47px;
                  color: black;
                }
                @keyframes slide {
                  0%{
                    background-position-x: 0%;
                  }
                  100%{
                    background-position-x: 600vw;
                  }
                }
            </style> 

            Risks associated with being overweight
Being overweight increases the risk of a number of serious diseases and health conditions. Below is a list of said risks, according to the Centers for Disease Control and Prevention (CDC):

High blood pressure
Higher levels of LDL cholesterol, which is widely considered "bad cholesterol," lower levels of HDL cholesterol, considered to be good cholesterol in moderation, and high levels of triglycerides
Type II diabetes
Coronary heart disease
Stroke
Gallbladder disease
Osteoarthritis, a type of joint disease caused by breakdown of joint cartilage
Sleep apnea and breathing problems
Certain cancers (endometrial, breast, colon, kidney, gallbladder, liver)
Low quality of life
Mental illnesses such as clinical depression, anxiety, and others
Body pains and difficulty with certain physical functions
Generally, an increased risk of mortality compared to those with a healthy BMI
            
            """
elif bmi<18.5:
        st.subheader("You are overweight!")
        body_html = """
                        <style>
                            .title h1{
                              user-select: none;
                              font-size: 47px;
                              color: black;
                            }
                            @keyframes slide {
                              0%{
                                background-position-x: 0%;
                              }
                              100%{
                                background-position-x: 600vw;
                              }
                            }
                        </style> 

                        Risks associated with being underweight
Being underweight has its own associated risks, listed below:

Malnutrition, vitamin deficiencies, anemia (lowered ability to carry blood vessels)
Osteoporosis, a disease that causes bone weakness, increasing the risk of breaking a bone
A decrease in immune function
Growth and development issues, particularly in children and teenagers
Possible reproductive issues for women due to hormonal imbalances that can disrupt the menstrual cycle. Underweight women also have a higher chance of miscarriage in the first trimester
Potential complications as a result of surgery
Generally, an increased risk of mortality compared to those with a healthy BMI

                        """
else:
    body_html = """
                                    <style>
                                        .title h1{
                                          user-select: none;
                                          font-size: 90px;
                                          color: black;
                                        }
                                        @keyframes slide {
                                          0%{
                                            background-position-x: 0%;
                                          }
                                          100%{
                                            background-position-x: 600vw;
                                          }
                                        }
                                    </style> 

                                    You have a healthy BMI!

                                    """
info_html = """
                        <style>
                            .title h1{
                              user-select: none;
                              font-size: 47px;
                              color: black;
                            }
                            @keyframes slide {
                              0%{
                                background-position-x: 0%;
                              }
                              100%{
                                background-position-x: 600vw;
                              }
                            }
                        </style> 

                        WHAT IS BMI?
BMI is a measurement of a person's leanness or corpulence based on their height and weight, and is intended to quantify tissue mass. It is widely used as a general indicator of whether a person has a healthy body weight for their height. Specifically, the value obtained from the calculation of BMI is used to categorize whether a person is underweight, normal weight, overweight, or obese depending on what range the value falls between. These ranges of BMI vary based on factors such as region and age, and are sometimes further divided into subcategories such as severely underweight or very severely obese. Being overweight or underweight can have significant health effects, so while BMI is an imperfect measure of healthy body weight, it is a useful indicator of whether any additional testing or action is required. Refer to the table below to see the different categories based on BMI that is used by the calculator.

                        """
st.markdown(body_html, unsafe_allow_html=True)

st.markdown(info_html, unsafe_allow_html=True)


    #st.markdown('<p class="big-font"><a>bmi</a></p>', unsafe_allow_html=True)
    #st.write("""<style>body {background-color: white;}</style>""", unsafe_allow_html=True)
