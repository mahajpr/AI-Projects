
from crewai import Task
from agents import resume_agent, job_agent, match_agent


resume_task = Task(
    description="""
Analyze the resume located at {resume_path}.
Extract key skills, experience, and important information.
""",
    agent=resume_agent,
    expected_output="Summary of candidate skills and experience"
)


job_task = Task(
    description="""
Analyze the following job description and identify
the important skills and requirements.

Job Description:
{job_desc}
""",
    agent=job_agent,
    expected_output="List of key job requirements"
)


match_task = Task(
    description="""
Compare the candidate resume with the job description.
Explain how well the resume matches the job.

Provide:

1. Match score (percentage)
2. Matching skills
3. Missing skills
4. Final recommendation
""",
    agent=match_agent,
    expected_output="Detailed match analysis"
)