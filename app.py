import streamlit as st
import json

# 定义不同页面的内容函数
from page.api_page import page_api_creat_user_service, page_api_create_order_service


def page_home():
    st.title("主页")
    st.write("欢迎来到主页！这里是应用的起始页面。")
    st.write("在要执行的操作的页面，输入场景所需的参数后，调用对应的造数方法，完成数据构造功能")


# 定义菜单结构
menu = {
    "主页": page_home,
    "api": {
        "api原子操作-得物用户下单": page_api_create_order_service,
        "api原子操作-创建得物用户": page_api_creat_user_service
    }
}

# with open("/Users/liyang/PycharmProjects/DataFactory/static/tables.json") as f:
#     menu = json.load(f)

# 初始化会话状态
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = page_home

# 创建侧边栏
with st.sidebar:
    for key, value in menu.items():
        if isinstance(value, dict):
            # 如果是二级菜单的父菜单（一级菜单）
            with st.expander(key):
                for sub_key, sub_value in value.items():
                    if st.button(sub_key):
                        st.session_state.selected_page = sub_value
        else:
            # 如果是普通的一级菜单
            if st.button(key):
                st.session_state.selected_page = value

# 显示选中的页面
st.session_state.selected_page()