import streamlit as st

from rag_engine import get_answer
from claim_checker import check_claim

st.set_page_config(
    page_title="Policy & Claims",
    page_icon="🩺",
    layout="wide"
)

st.markdown("""
<style>

.main{
    background:#f5f7fb;
}

.stButton>button{
    width:100%;
    background:#0066ff;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
}

</style>
""",unsafe_allow_html=True)

st.title("🏥 Policy & Claims Copilot")

tab1,tab2=st.tabs(
    [
        "Policy Assistant",
        "Claim Pre-Check"
    ]
)

with tab1:

    st.subheader("Ask Policy Questions")

    question=st.text_area(
        "Enter Question"
    )

    if st.button("Get Answer"):

        result=get_answer(question)

        st.success("Response Generated")

        st.markdown(result["answer"])

        st.info(
            f"Sources: {', '.join(result['sources'])}"
        )

with tab2:

    st.subheader("Claim Eligibility Checker")

    illness=st.text_input(
        "Disease / Treatment"
    )

    months=st.number_input(
        "Policy Active (Months)",
        min_value=0,
        value=12
    )

    if st.button("Check Claim"):

        result=check_claim(
            illness,
            months
        )

        st.markdown(result["answer"])

        st.info(
            f"Sources: {', '.join(result['sources'])}"
        )