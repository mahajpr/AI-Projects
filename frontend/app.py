import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="AI Resume Agent", page_icon="🤖")

st.title("🤖 Agentic AI Resume Matcher")

st.write("Upload your resume and let the AI agent analyze how well it matches the job description.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_desc = st.text_area("Enter Job Description")

if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.warning("Please upload a resume")

    elif job_desc.strip() == "":
        st.warning("Please enter a job description")

    else:
        files = {
            "file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")
        }

        upload_response = requests.post(
            f"{BACKEND_URL}/upload-resume",
            files=files
        )

        if upload_response.status_code != 200:
            st.error("Resume upload failed")
        else:
            file_name = upload_response.json()["file_name"]

            st.success("Resume uploaded successfully")

            with st.spinner("AI Agents analyzing your resume..."):

                response = requests.post(
                    f"{BACKEND_URL}/match-resume-agent",
                    params={"file_name": file_name},
                    json={"query": job_desc}
                )

                if response.status_code == 200:

                    result = response.json()

                    st.subheader("📊 AI Analysis")

                    st.write(result["result"])

                else:
                    st.error("Agent analysis failed")