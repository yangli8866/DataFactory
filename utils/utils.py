import streamlit as st
import json


class Utils:

    # 显示表单
    @staticmethod
    def display_form(method):
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
                # 这里写调用对应api方法，返回值为res
                # from api.pay_api import PayApi
                # func = getattr(PayApi, method, None)
                # res = func()
                res = "返回信息"
                st.text_area(res, value=result)
            except json.JSONDecodeError:
                st.error("输入的内容不是有效的 JSON 格式，请检查。")
