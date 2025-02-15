import streamlit as st
import json
from utils.utils import Utils



def page_api_creat_user_service():
    st.title("api业务")
    st.write("api原子操作-创建得物用户")
    Utils.display_form("api_creat_user_service")

def page_api_create_order_service():
    st.title("api业务")
    st.write("api原子操作-得物用户下单")
    st.write("入参格式为：\
    {\
        \"userid\": ${userid},\
        \"count\": ${count},\
        \"item\": ${item}\
    }\
    其中userid为用户id，count为借款金额，item为借款期限\
             ")
    Utils.display_form("api_creat_user_service")