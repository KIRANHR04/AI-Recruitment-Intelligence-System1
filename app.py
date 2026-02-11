import streamlit as st
from embeddings import get_embedding
from endee_client import insert_vector, search_vector
from pdf_utils import extract_text_from_pdf

st.set_page_config(page_title="AI Recruitment Intelligence System")

st.title("AI Recruitment Intelligence System")

tab1, tab2 = st.tabs(["Add Job", "Match Resume"])

# ---------------- ADD JOB ----------------
with tab1:
    st.header("Add Job")

    job_id = st.text_input("Job ID")
    title = st.text_input("Job Title")
    description = st.text_area("Job Description")

    if st.button("Add Job"):
        if job_id and title and description:
            with st.spinner("Generating embedding..."):
                embedding = get_embedding(description)

            status, response = insert_vector(
                job_id,
                title,
                description,
                embedding
            )

            if status == 200:
                st.success("Job added successfully!")
            else:
                st.error(f"Error: {response}")
        else:
            st.warning("Please fill all fields.")


# ---------------- MATCH RESUME ----------------
with tab2:
    st.header("Match Resume")

    uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

    if uploaded_file is not None:
        with st.spinner("Processing resume..."):
            text = extract_text_from_pdf(uploaded_file)
            embedding = get_embedding(text)

            status, results = search_vector(embedding)

            if status == 200:
                st.success("Matching Results")

                matches = results.get("matches", [])

                if matches:
                    for match in matches:
                        metadata = match.get("metadata", {})
                        score = match.get("score", 0)

                        st.subheader(metadata.get("title", "No Title"))
                        st.write(metadata.get("description", "No Description"))
                        st.write(f"Similarity Score: {round(score * 100, 2)}%")
                        st.divider()
                else:
                    st.info("No matching jobs found.")
            else:
                st.error(f"Search failed: {results}")
