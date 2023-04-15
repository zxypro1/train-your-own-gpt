import os

import streamlit as st
from train import main

st.set_page_config(page_title="Train your own gpt")


class args():
    def __init__(self, actor_model_size, reward_model_size, train_mode, train_step, actor_zero_step, reward_zero_step):
        self.step = (1, 2, 3) if train_step == 'All' else int(train_step.split(':')[0])
        self.actor_model = actor_model_size
        self.reward_model = reward_model_size
        self.deployment_type = train_mode.split(' ')[0].lower() + '_' + train_mode.split(' ')[1].lower()
        self.output_dir = os.path.abspath('./output')
        self.actor_zero_stage = actor_zero_step
        self.reward_zero_step = reward_zero_step


html_temp = """
                <div style="background-color:{};padding:1px">
                
                </div>
                """

actor_model_size = '1.3b'
reward_model_size = '350m'
train_mode = 'Single GPU'
train_step = 'All'
actor_zero_step = ''
reward_zero_step = ''

with st.sidebar:
    with st.form("my_form"):
        actor_model_size = st.selectbox('Actor Model Size', ('1.3b', '6.7b', '13b', '66b'))
        reward_model_size = st.selectbox('Reward Model Size', ('350m',))
        train_mode = st.radio("Training mode", ('Single GPU', 'Multi Node', 'Single Node'))
        train_step = st.selectbox('Train Step', (
        'All', '1: Supervised Finetuning', '2: Reward model Finetuning', '3: RLHF Finetuning'))
        actor_zero_step = st.selectbox('Actor Model ZeRO step', ('', 0, 1, 2, 3))
        reward_zero_step = st.selectbox('Reward Model ZeRO step', ('', 0, 1, 2, 3))

        args = args(actor_model_size, reward_model_size, train_mode, train_step, actor_zero_step, reward_zero_step)
        if st.form_submit_button("Train!"):
            main(args)

st.markdown("""
    # DeepSpeed-Chat  
    This is a training and chat UI demo of the DeepSpeed-Chat project.  
    Current Status: No model trained. Please click `Train!` button to train a new model!
    """)

tab1, tab2 = st.tabs(["Train", "Chat"])

with tab1:
   st.header("Train")

with tab2:
   st.header("Chat")
   col1, col2 = st.columns(2)

   with col1:
       st.header("A cat")

   with col2:
       st.header("A dog")

hide = """
<style>
footer{
	visibility: hidden;
    position: relative;
}
<style>
"""
st.markdown(hide, unsafe_allow_html=True)
