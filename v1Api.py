## NLP App Theatre Reviews

### Import packages


import streamlit as st
import pandas as pd
import requests as rq


import base64
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

## Init

global page
st.set_page_config(
    page_title="API Hi!Paris", layout="wide", page_icon="hi-paris.png"
)

### methods useful

def load_csv(path):
    data=pd.read_csv(path,encoding='latin1',delimiter=';')
    
    return data
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded



def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)





def item(info,base_url,id_int,cond=None):
  st.header(info['title'][id_int-1])
  st.write('    ')
  st.write(info['field'][id_int-1])
  st.write('size : '+str(info['size'][id_int-1])+' Mo')
  st.write('format : '+info['format'][id_int-1])
  st.write(info['text'][id_int-1])
  st.write('      ')
  url_link=base_url+info['name_url'][id_int-1]
  st.markdown(
        ("[<img src='data:image/png;base64,{}' class='img-fluid' width=40 height=40>]("+url_link+")").format(
            img_to_bytes("Download-Icon.png")
        ),
        unsafe_allow_html=True,
    )
  st.write('    ')
  st.markdown('---')


def header_viz(info,base,id_int):
  if str(info['name_h1'][id_int])!=str(NaN):
    rq.get(base+str(info['name_h1'][id_int]),stream=True)
    r.raw.decode_content = True
    r.raw
    
 
### Main Front

def main():
    def _max_width_():
        max_width_str = f"max-width: 1000px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>
        """,
            unsafe_allow_html=True,
        )
    # Hide the Streamlit header and footer
    def hide_header_footer():
        hide_streamlit_style = """
                    <style>
                    footer {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    # increases the width of the text and tables/figures
    _max_width_()
    # hide the footer
    hide_header_footer()
    HI=Image.open('hi-paris.png')
    st.image(HI,width=400)
    st.markdown("# API Hi!Paris 🔍 🖥")
    st.markdown("     ")


    if 'page' not in st.session_state:
      st.session_state.page=1
    st.sidebar.header("Dashboard")
    st.sidebar.markdown("---")
    if st.sidebar.button('Select all'):
      st.session_state.page=1
    if st.sidebar.button('Select by Type'):
      st.session_state.page=2
    if st.sidebar.button('Select by Field'):
      st.session_state.page=3
    if st.sidebar.button('Submit a dataset'):
      st.session_state.page=4
    page=st.session_state.page


    if page==1 or page==2 or page==3:
      info=load_csv('info.csv')
      base='https://minio.lab.sspcloud.fr/paamiandleroy/'#img_test.zip
      for id_int in info['id']:
        item(info.loc[info['id']==id_int],base,id_int)
    elif page==4:
      st.subheader('Submit your dataset for publication')
      st.write('''
        You can propose a dataset for open source publication. It will be available to your collaborators as well as to anyone who has this link. 
        Please provide some information so that we can process your request. We ask you to fill in a title, a very short description, the field of interest, 
        and some personal information (email, profession, company/university). 
        Please also attach a header (a small part of your dataset) so that we can study it. We will check that this dataset is in accordance with the RGPD laws in force.
        We will contact you as soon as possible to proceed with the sending of the data. ''')
      submit_format=st.selectbox('Format of your data (uncompressed)?',["I don't know",'JSON','csv','txt','video','image','audio','other'])
      if submit_format=='other':
        submit_format=st.text_input('Format of your data ?','')
      submit_zip=st.selectbox('Compression?',["I don't know",'No','Yes, .zip','Yes, .rar','Yes, .gz','Yes, other compression'])
      if submit_zip=='Yes, other compression':
        submit_zip=st.text_input('Compression?','Yes, the compression is')
      submit_field=st.selectbox('Field?',["I don't know",'NLP','Signal Processing','Healt','Economic','Computer Vizion','Game Theory','Finance & Business', 'Machine Learning Theory','other'])
      if submit_field=='other':
        submit_field=st.text_input('Field?','')
      submit_title=st.text_input('Title:','')
      submit_text=st.text_input('Write a short Description','')
      submit_email=st.text_input('Write your email','')
      submit_profession=st.text_input('Write your profession','')
      submit_university=st.text_input('What is your university/business affiliation? ','')
      submit_commentary=st.text_input('If you have other things to say','')
      submit_file=st.file_uploader('Upload a part of your Dataset')
      st.button('Submit')
 
if __name__=='__main__':
    main()



st.markdown(f"####  Link to Project Website [here]({'https://github.com/hi-paris'}) 🚀 ")


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;background - color: white}
     .stApp { bottom: 80px; }
    </style>
    """
    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1,

    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

def footer2():
    myargs = [
        " Made by ",
        link("https://engineeringteam.hi-paris.fr/", "Hi! PARIS Engineering Team"),
        " 👩🏼‍💻 👨🏼‍💻"
    ]
    layout(*myargs)


if __name__ == "__main__":
    footer2()



