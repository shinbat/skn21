import streamlit as st

pages = {
    "네비게이션1": [
        st.Page("01_write.py", title="01_write"),
        st.Page("02_table_metric.py", title="02_table_metric"),
        st.Page("03_input_widget.py", title="03_input_widget"),
        st.Page("04_layout_cache.py", title="04_layout_cache"),
    ],
    "네비게이션2": [
        st.Page("05_sidebar.py", title="05_sidebar"),
        st.Page("06_paging.py", title="06_paging"),
        st.Page("pages/page4.py", title="page4"),
     ],
}

pg = st.navigation(pages)
pg.run()