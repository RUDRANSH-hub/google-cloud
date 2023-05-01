import pandas as pd
import streamlit as st
from developer import developer


    

# link is the column with hyperlinks

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

#         df.to_html(escape=False, index=False), unsafe_allow_html=True
        df['Student Email']=(href="{email}">{email}</a>')
        return (df[df["Student Email"]==str(email)])
        
        
        


    new_df = pd.read_csv("data.csv")
    new_df=new_df.set_index("Student Name")
    # new_df=new_df.style.hide_index()
    new_df["MileStone1"]="NO"
    new_df["MileStone2"]="NO"
    new_df["MileStone3"]="NO"
    new_df["MileStone4"]="NO"

    p=list(new_df["# of Quests Completed"])
    q=list(new_df["# of Skill Badges Completed"])
    for i in range(len(new_df["# of Quests Completed"])):
        if(q[i]==20 and p[i]==40 ):
            new_df["MileStone4"][i]="YES"
            new_df["MileStone3"][i]="YES"
            new_df["MileStone2"][i]="YES"
            new_df["MileStone1"][i]="YES"
        elif( p[i]>=30 and q[i]>=15 ):
            new_df["MileStone3"][i]="YES"
            new_df["MileStone2"][i]="YES"
            new_df["MileStone1"][i]="YES"
        elif( p[i]>=20 and q[i]>=10 ):
            new_df["MileStone2"][i]="YES"
            new_df["MileStone1"][i]="YES"
        elif(p[i]>=10 and q[i]>=5):
            new_df["MileStone1"][i]="YES"
    
    

    
        
    email=st.text_input("Enter your mail")
    res=get_info(str(email),new_df)
    res=res.drop(columns=["Student Email","Google Cloud Skills Boost Profile URL","Institution","Enrolment Date & Time","Enrolment Status"],axis=1)
    Button=st.button("Get_data")
    if Button :
        st.table(res)
