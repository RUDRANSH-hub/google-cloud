import pandas as pd
import streamlit as st
from developer import developer
add_selectbox = st.sidebar.selectbox("Details/Developer",("Student Details","Developer")
)
if add_selectbox== "Developer":
    developer()
elif(add_selectbox=="Student Details"):
    
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )


    st.header("Kamla Nehru Institute of Technology")
    def get_info(email,df):

    
        return (df[df["Student Email"]==str(email)])
        
        
        


    new_df = pd.read_csv("Kamla Nehru Institute of Technology, Sultanpur [29 Apr].csv")
    new_df=new_df.set_index("Student Name")
    # new_df=new_df.style.hide_index()
    new_df["mine"]=0

    p=list(new_df["# of Quests Completed"])
    q=list(new_df["# of Skill Badges Completed"])
    for i in range(len(new_df["# of Quests Completed"])):
        if(q[i]==20 and p[i]==40 ):
            new_df["mine"][i]=4
        elif( p[i]>=30 and q[i]>=15 ):
            new_df["mine"][i]=3
        elif( p[i]>=20 and q[i]>=10 ):
            new_df["mine"][i]=2
        elif(p[i]>=10 and q[i]>=5):
            new_df["mine"][i]=1
    
    

    
        
    email=st.text_input("Enter your mail")
    res=get_info(str(email),new_df)
    res=res.drop(columns=["Student Email","Institution","Enrolment Date & Time","Enrolment Status"],axis=1)
    Button=st.button("Get_data")
    if Button :
        st.table(res)
