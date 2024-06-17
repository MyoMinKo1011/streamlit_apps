import streamlit as st

st.title("English File (4th Edition) - Elementary")
st.subheader("Developed by Myo Min Ko")

units = ['Unit_1', 'Unit_2', 'Unit_3', 'Unit_3', 'Unit_4', 'Unit_5', 'Unit_6', 'Unit_7', 'Unit_8', 'Unit_9', 'Unit_10', 'Unit_11', 'Unit_12']

unit1_files = []
for x in range(2, 46):
    unit1_files.append(f"EF4e_ElemSB_1.{x}.mp3")

unit2_files = []
for x in range(1, 18):
    unit2_files.append(f"EF4e_ElemSB_2.{x}.mp3")
    
unit3_files = []
for x in range(1, 27):
    unit3_files.append(f"EF4e_ElemSB_3.{x}.mp3")

unit4_files = []
for x in range(1, 23):
    unit4_files.append(f"EF4e_ElemSB_4.{x}.mp3")

unit5_files = []
for x in range(1, 22):
    unit5_files.append(f"EF4e_ElemSB_5.{x}.mp3")

unit6_files = []
for x in range(1, 25):
    unit6_files.append(f"EF4e_ElemSB_6.{x}.mp3")

unit7_files = []
for x in range(1, 19):
    unit7_files.append(f"EF4e_ElemSB_7.{x}.mp3")

unit8_files = []
for x in range(1, 25):
    unit8_files.append(f"EF4e_ElemSB_8.{x}.mp3")

unit9_files = []
for x in range(1, 21):
    unit9_files.append(f"EF4e_ElemSB_9.{x}.mp3")

unit10_files = []
for x in range(1, 21):
    unit10_files.append(f"EF4e_ElemSB_10.{x}.mp3")

unit11_files = []
for x in range(1, 14):
    unit11_files.append(f"EF4e_ElemSB_11.{x}.mp3")

unit12_files = []
for x in range(1, 14):
    unit12_files.append(f"EF4e_ElemSB_12.{x}.mp3")

audios = {
    'Unit_1' : unit1_files,
    'Unit_2' : unit2_files,
    'Unit_3' : unit3_files,
    'Unit_4' : unit4_files,
    'Unit_5' : unit5_files,
    'Unit_6' : unit6_files,
    'Unit_7' : unit7_files,
    'Unit_8' : unit8_files,
    'Unit_9' : unit9_files,
    'Unit_10' : unit10_files,
    'Unit_11' : unit11_files,
    'Unit_12' : unit12_files,
}

selected_units = st.selectbox("Select a Unit", units)

if selected_units:
    for file in audios[selected_units]:
        st.subheader(f"{file}")
        st.audio(f"./Audio/{selected_units}/{file}", format='audio/mp3')

