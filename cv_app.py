from pathlib import Path
import streamlit as st
from streamlit_extras import add_vertical_space as avs

class CV_App():
    def __init__(self, name:str, email:str, des, pfp_image, cv_pdv, number:str):
        self.resume_file =cv_pdv
        self.profile_pic =pfp_image
            
        # --- PERSONAL INFO ---
        self.name = name
        self.page_title = f"Digital CV | {name}"
        self.page_icon = ":computer:"
        self.phone_number = number
        self.description = des
        self.my_email = email

        self.my_socials = None
        self.work_background = None
        self.courses = None
        self.skills = None
        self.workshops = None
        self.languages = None
        self.projects = None

        self.mint = '#8bd8bd'
        self.blue = "#5ba1f2"

    def set_work_background(self, work: dict):
        self.work_background = work

    def set_courses(self, courses: dict):
        self.courses = courses

    def set_skills(self, skills: dict):
        self.skills = skills

    def set_workshops(self, shops: dict):
        self.workshops = shops

    def set_projects(self, projects: dict):
        self.projects = projects

    def set_languages(self, l : dict):
        self.languages = l
    
    def set_socials(self, socials: dict):
        self.my_socials = socials
    
    def text_format(self,txt,color = "#8bd8bd", size = "20" , txt_format = 0):
        if txt_format == 0:
            return f'<b style=" color:{color}; font-size: {size}px;"> {txt}</b>'
        else:
            # centered text
            return f'<div style=" color:{color}; font-size: {size}px;  text-align: center; ">  {txt}   </div>'

    def lines(self, line_type: int, color = "#A2A2A2"):
        if line_type == 0:
            l1, l2, l3 = st.columns(3, gap='large')
            with l1:
                st.markdown(self.text_format("_"*19, color=color), unsafe_allow_html=True)

            with l2:
                st.markdown(" ")

            with l3:
                    st.markdown(self.text_format("_"*19, color=color), unsafe_allow_html=True)
        elif line_type == 1:
            l1, l2, l3 = st.columns(3, gap='small')
            with l1:
                st.markdown(' ')

            with l2:
                st.markdown(self.text_format("_"*22, color=color), unsafe_allow_html=True)

            with l3:
                st.markdown('')
        else:
            st.markdown(self.text_format("_"*72, color=color), unsafe_allow_html=True)


    def show_info(self, info: dict, emojy: str , txt_format = 0, color = 'white', year = True):
        # skip year index [1:]
        for i in info:
            if year:
                st.markdown(emojy+self.text_format(i, color = color, size = "17", txt_format=txt_format)+\
                    self.text_format(' | '+info[i][0], size="15", txt_format=txt_format, color=self.blue), unsafe_allow_html=True)
            else:
                st.markdown(emojy+self.text_format(i, color = color, size = "17", txt_format=txt_format), unsafe_allow_html=True)

            for j in info[i][1:]:
                    st.caption(j)

    def run_app(self):
        # --- HANDLING PDF FILE ---
        with open(self.resume_file, 'rb') as pdf_file:
            PDFbyte = pdf_file.read()
            
        # --- STREAMLIT PAGE ---
        st.set_page_config(page_title=self.page_title,
                        page_icon=self.page_icon,
                        layout="centered",)

        pfp,personal_info = st.columns(2)

        with pfp:
                st.image(self.profile_pic, width=270)


        with personal_info:
            st.markdown(self.text_format(self.name, size = "45", color = "white"), unsafe_allow_html=True)
            st.markdown(self.text_format(self.description, size = "15", color='white'), unsafe_allow_html=True)
            st.markdown(self.text_format("📞 "+self.phone_number, size = "15",color='white'), unsafe_allow_html=True)
            st.markdown(self.text_format(self.my_email, size = "15",color='white'), unsafe_allow_html=True)
            st.download_button(
                label='🔽 Download CV',
                data = PDFbyte,
                file_name=self.resume_file,
                mime='application/octet-stream'
            )

        self.lines(line_type=2, color=self.mint)
        avs.add_vertical_space(2)
        st.markdown(f'*_{self.text_format("WORK BACKGROUND:", size=23)}_*', unsafe_allow_html=True)


        self.show_info(self.work_background, '- ')

        self.lines(0)
        avs.add_vertical_space(1)
        st.markdown(f'*_{self.text_format("COURSES ATTENDED:", size=23)}_*', unsafe_allow_html=True)

        self.show_info(self.courses, '')

        st.markdown(f'*_{self.text_format("WORKSHOPS TAUGHT:", size=23)}_*', unsafe_allow_html=True)

        self.show_info(self.workshops, '- ')

        self.lines(0)
        avs.add_vertical_space(1)
        st.markdown(f'*_{self.text_format("CORE SKILLS:", size=23)}_*', unsafe_allow_html=True)

        skill_left,space, skill_right = st.columns(3, gap='small') 
        with space:
                st.markdown('')
                
        for i, info in enumerate(self.skills):
            if i >= (len(self.skills)//2):
                with skill_right:
                    st.markdown('- '+self.text_format(info, color = "white", size = 17), unsafe_allow_html=True)
                    for j in self.skills[info]:
                                st.caption(j)
            else:
                # go next column
                with skill_left:
                    st.markdown('- '+self.text_format(info, color = "white", size = 17), unsafe_allow_html=True)
                    for j in self.skills[info]:
                                st.caption(j)

        st.markdown(f'*_{self.text_format("LANGUAGES:", size=23)}_*', unsafe_allow_html=True)
        left_lang, space, right_lang = st.columns(3, gap='small')
        with space:
            st.markdown(' ')

        for i, info in enumerate(self.languages):
                if i < (len(self.languages)//2):
                    with left_lang:
                        st.markdown(self.text_format(info, color = "white", size = 17), unsafe_allow_html=True)
                        for j in self.languages[info]:
                                st.caption(j)
                else:
                    # go next column
                    with right_lang:
                        st.markdown(self.text_format(info, color = "white", size = 17), unsafe_allow_html=True)
                        for j in self.languages[info]:
                                st.caption(j)

        self.lines(3, color=self.mint)
        avs.add_vertical_space(2)
        st.markdown(f'{self.text_format("☑️ PERSONAL PROJECTS:", txt_format=0, color="white", size="25")}', unsafe_allow_html=True)
        self.show_info(self.projects, emojy='- ', txt_format=0, year=False)

        
def Asmaa_cv():
    
    app = CV_App('Asmaa Alamzi', 'AsmaaAlazmi907@gmail.com', "Computer Engineer Student at Kuwait University",\
        'i_loading.png', 'CV.pdf', "+965-97756439")

    app.set_courses({"📱 Android app development using Java,  Kuwait Codes":['2022',""],
            "🎮 Game development using Unity-Engine, Unicode course from Coded Kw": ['2022', ""],
            "🤖 Arduino, CPES":["2022", ''], 
            "📱 Flutter app development, Unicode":['2022',''],
            '🖨️ 3D printing, KARS':['2023','']
            })

    app.set_languages({'Arabic': ['🔊 Native speaker'],
            'English':['🔉 Highly proficient in speaking & writing']})

    app.set_projects({
            "Python workshop leaderboard app | [➡️](https://projectcodekw-python-leaderboard-app-lnwjcg.streamlit.app/)": ['2023',""],
            "Grade Calculator | 🔜": ['2023',""],
            'MajorSheety | 🔜':['2023', '']
                })

    app.set_skills({"Python programming" : [''],
            "Flutter app development" : [''],
            "Streamlit data science applications" : [''],
            "Digital art" :  [''],
            "Arduino" :  [''],
            "Unity game development" : [''],
            "Using virtual machines" : [''],
            })

    app.set_work_background({"Mentor for game development course at Coded Kw" : [" 2022", ''],
            "A member of Computer Engineering Society (CPES)" : ['2022',""],
            "Treasurer of Kuwait University AI & Robotics Society (KARS)" : ['2023',""],
            "Creator of Project Code Kw group" : ['2023'," *_Project code is a group of Kuwait university students that aim to help \
                    the programming community in Kuwait.to learn more visit the following:_*",\
                            "> [📸 INSTAGRAM ](https://www.instagram.com/projectcodekw/)",
                            "> [📺 YOUTUBE ](https://www.instagram.com/projectcodekw/)"]
            })
            
    app.set_workshops({
                'Online workshop for KU students regarding OOP course':['2022-2023',''],
                "CPES's Python chatbot workshop":['2023',''],
                "KARS's Python basics workshop":['2023',''],
            })

    return app

def Human_cv():    
    app = CV_App('Human AlHuman', 'Human986@work.com', "Computer Engineer Student at Kuwait University",\
        'random_pfp.png', 'random_cv.pdf', "+965-98545550")

    app.set_courses({"📱 Swift app development using Java,  KARS":['Jan 2022',""],
            "🎮 Game development using Godot-Engine, KARS": ['Jan 2022', ""],
            "🤖 Arduino, KARS":["Feb 2022", ''], 
            "📱 Python app development, KARS":['Feb 2022',''],
            '🖨️ 3D printing, KARS':['March 2023','']
            })

    app.set_languages({'Arabic': ['🔊 Native speaker'],
            'English':['🔉 Highly proficient in speaking & writing']})

    app.set_projects({
            "KARS website creator | [➡️](https://www.google.com)": ['Oct 2023',""],
            "Disord Bot Creator | 🔜": ['',""],
                })

    app.set_skills({"Python programming" : [''],
            "Flutter app development" : [''],
            "Streamlit data science applications" : [''],
            "Arduino" :  [''],
            "Game Animations" : [''],
            "Java Programming" : [''],
            })

    app.set_work_background({"Worked on a research project at Kuwait Universiy for CPE department" : ["Sep 2022", ''],
            "A member of Computer Engineering Society (CPES)" : ['Oct 2022',""],
            "A member of Kuwait Ai and Robotics Society (KARS)" : ['Jan 2023',""],
            "CEO of CodeSociety company " : ['Jan 2023 - ongoing'," *_CodeSociety is a group of programmers that aim to help \
                    the programming community in the Middle East. to learn more visit the following:_*",\
                            "> [🌐 Website ](https://www.google.com)",]
            })
            
    app.set_workshops({
                'Online Java classes for AUM students':['Nov 2022 - Jan 2023',''],
                "KARS's Digital CV workshop ":['March 2023',''],
                "KARS's Web Development workshop":['April 2023',''],
            })

    return app

try:
    app = Human_cv()
    app.run_app()
except NameError:
    st.write('😱😱 NameERROR! somewhere... 😱😱')
    st.header('Please fill all the info (use set funcitons)')
    st.subheader('call the functions in the following order: ')
    st.subheader('to add links use the following format: > [title](https://www.instagram.com/projectcodekw/)')
    st.write('NOTE: if you dont have a cation just add " ", if you dont ave a link dont add a new index to the list ')
    st.write("app.set_work_background({'title':['year','caption', 'links']})")
    st.write("app.set_workshops({'title':['year', 'caption', 'links']})")
    st.write(" app.set_courses({'title':['year', 'caption', 'links']})")
    st.write(" app.set_skills({'title':['caption', 'links']})")
    st.write(" app.set_languages({'title':'caption'})")
    st.write("app.set_projects('title': ['caption', 'links'])")

