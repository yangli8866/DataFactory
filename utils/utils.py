import streamlit as st
import json

class Utils:

    # 显示表单
    @staticmethod
    def display_form():
        # 环境下拉框
        environment = st.selectbox("环境", ["dev", "qa", "sit"])
        # 参数输入框
        parameters = st.text_area("参数", value="{}")
        # 提交按钮
        if st.button("提交"):
            try:
                # 尝试将输入内容解析为 JSON
                json_params = json.loads(parameters)
                result = f"选择的环境: {environment}, 输入的参数: {json_params}"
                st.text_area("返回信息", value=result)
            except json.JSONDecodeError:
                st.error("输入的内容不是有效的 JSON 格式，请检查。")

if __name__=='__main__':


    print(d)