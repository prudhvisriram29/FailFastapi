import streamlit as st
from groq import Groq

# CONFIGURE GROQ
client = Groq(api_key="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")

st.set_page_config(page_title="FailFast AI", layout="centered")

st.title("🚨 FailFast AI – Product Reality Checker")
st.write("Get brutally honest feedback on your product idea.")

# INPUT FIELDS
idea = st.text_area("Product Idea")
users = st.text_area("Target Users")
revenue = st.text_area("Revenue Model")
features = st.text_area("Core Features")
assumptions = st.text_area("Assumptions")

def analyze(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a brutally honest product analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content

# ANALYZE BUTTON
if st.button("Analyze My Idea"):
    prompt = f"""
You are a brutally honest Product Reality Analyst.

Your job is NOT to encourage ideas.
Your job is to expose why they might fail.

Analyze this product idea based on:

1. User behavior
2. Market competition
3. Business viability
4. UX friction
5. Psychological motivation
6. Real-world constraints

Be critical, realistic, and specific.

Then suggest:
- How to reduce risk
- A better MVP version
- Stronger positioning

Do NOT sugarcoat.

Product Idea: {idea}
Target Users: {users}
Revenue Model: {revenue}
Core Features: {features}
Assumptions: {assumptions}
"""

    result = analyze(prompt)
    
    st.subheader("Reality Check Report")
    st.write(result)
