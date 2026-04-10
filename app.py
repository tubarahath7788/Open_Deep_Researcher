import streamlit as st
import sys
import os

# ✅ Project root path add karo
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from graph.workflow import app as research_app

# 🎨 UI Title
st.set_page_config(page_title="AI Research Assistant", layout="centered")

st.title("🤖 AI Research Assistant")
st.write("Enter any research topic and get a structured report instantly.")

# 📝 Input box
query = st.text_area("Enter your research topic:")

# 🚀 Button
if st.button("Generate Report"):
    if query.strip() == "":
        st.warning("Please enter a topic!")
    else:
        with st.spinner("Researching... ⏳"):
            result = research_app.invoke({
                "query": query
            })

            st.success("Done!")

            # 📄 Output
            st.subheader("📄 Research Report")
            st.write(result["report"])

            # 📥 Download Button (NEW 🔥)
            st.download_button(
                label="📥 Download Report",
                data=result["report"],
                file_name="research_report.txt",
                mime="text/plain"
            )