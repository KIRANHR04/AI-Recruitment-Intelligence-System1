AI Recruitment Intelligence System
 Project Summary

The AI Recruitment Intelligence System is a semantic search–based recruitment platform that intelligently matches resumes with job descriptions using vector embeddings.

Instead of relying on keyword matching, this system uses transformer-based embeddings and cosine similarity to understand contextual meaning between resumes and job postings.

 Problem Statement

Traditional recruitment systems:

Depend on keyword matching

Fail to understand semantic meaning

Miss relevant candidates due to wording differences

This project solves that by:

Converting text into embeddings

Storing vectors in a vector database

Performing similarity search

Ranking jobs based on contextual similarity

 How The System Works
Step 1 – Add Job

Recruiter enters Job ID, Title, Description

System generates 384-dimensional embedding

Embedding stored in Endee Vector Database

Step 2 – Resume Upload

Candidate uploads PDF resume

Text extracted from resume

Resume converted into embedding

Step 3 – Semantic Matching

Resume embedding compared against stored job embeddings

Cosine similarity used

Top matching jobs returned with similarity score

System Architecture
Streamlit UI
      ↓
Sentence Transformer Model
      ↓
Vector Embedding (384-dim)
      ↓
Endee Vector Database
      ↓
Cosine Similarity Search
      ↓
Matching Results

## Technologies Used
Component	Technology
Frontend	Streamlit
Backend	Python
Embedding Model	sentence-transformers/all-MiniLM-L6-v2
Vector Database	Endee
Containerization	Docker
PDF Parsing	PyPDF2
# Requirements

To run this project locally, the reviewer needs:

 Software Requirements

Python 3.10+

Docker Desktop

Git (optional)

# Setup & Execution Instructions
Step 1 – Install Python Dependencies

From project root:

pip install -r requirements.txt

Step 2 – Start Endee Vector Database

Navigate to the endee folder:

cd endee
docker compose up -d


Verify it is running:

docker ps


The Endee UI will be available at:

http://localhost:8080

Step 3 – Create Vector Index

Inside Endee UI:

Create index with:

Index Name: jobs_index1

Dimension: 384

Space Type: Cosine

Precision: float16

Step 4 – Run Application

From project root:

streamlit run app.py


The app will open at:

http://localhost:8501

# Features Implemented

Add Job Descriptions

Automatic Embedding Generation

Resume Upload (PDF)

Semantic Similarity Matching

Cosine Similarity Scoring

Vector Storage in Endee

 Embedding Configuration

Model: all-MiniLM-L6-v2

Embedding Dimension: 384

Similarity Metric: Cosine

Vector Precision: float16

 Future Improvements

REST API with FastAPI

Authentication System

Recruiter Dashboard

Cloud Deployment

Production-grade Vector DB

Candidate Ranking Analytics

 Project Status

Functional AI Prototype
Core semantic matching implemented
Vector database integrated
Ready for demonstration and evaluation

 Author

Kiran HR
