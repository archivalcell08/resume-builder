import streamlit as st
from jinja2 import Template
import base64

# --- APP CONFIG ---
st.set_page_config(layout="wide", page_title="Aeronautical Engineer Resume Builder")

# --- UI LAYOUT ---
st.title("🛠️ Custom Resume Builder")
st.subheader("Update your details below to refresh your professional profile.")

col1, col2 = st.columns([1, 1.5])

with col1:
    st.header("Resume Content")
    
    # Basic Info
    with st.expander("Personal Details", expanded=True):
        name = st.text_input("Full Name", value="Aaron Sebastian Fabian")
        license = st.text_input("License Info", value="Licensed Aeronautical Engineer (Reg. No. 0004056)")
        email = st.text_input("Email", value="aaron.fabian888@gmail.com")
        phone = st.text_input("Phone", value="+639617469906")
        address = st.text_area("Address", value="Parañaque City, Philippines 1715")

    # Experience
    with st.expander("Experience"):
        st.info("Edit your roles here. Use commas to separate bullet points.")
        # Job 1
        j1_title = st.text_input("Job 1 Role", value="UAV Systems Engineer & Lead Pilot")
        j1_bullets = st.text_area("Job 1 Bullets", value="Systems & Electronics Integration, Control Systems Tuning, Aerodynamic Simulation")
        
        # Job 2
        j2_title = st.text_input("Job 2 Role", value="Intern - Production Planner")
        j2_bullets = st.text_area("Job 2 Bullets", value="Compliance & Quality, Data Management, Workflow Automation")

    # Skills
    with st.expander("Technical Skills"):
        skills = st.text_area("Skills List (comma separated)", 
                             value="UAV Control Systems, Electronics, Simulation & Design, Embedded Platforms, Flight Testing")

# --- RESUME DESIGN (Jinja2 + CSS) ---
resume_template = """
<!DOCTYPE html>
<html>
<head>
<style>
    @page { size: A4; margin: 1cm; }
    body { font-family: 'Helvetica', sans-serif; color: #333; line-height: 1.5; }
    .header { text-align: center; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; margin-bottom: 20px; }
    .header h1 { margin: 0; color: #2c3e50; text-transform: uppercase; letter-spacing: 2px; }
    .contact { font-size: 12px; color: #555; }
    .section-title { font-weight: bold; background: #f4f4f4; padding: 5px 10px; margin-top: 20px; border-left: 5px solid #2c3e50; }
    .job { margin-top: 10px; }
    .job-title { font-weight: bold; color: #2c3e50; }
    ul { margin-top: 5px; }
</style>
</head>
<body>
    <div class="header">
        <h1>{{ name }}</h1>
        <p><strong>{{ license }}</strong></p>
        <div class="contact">{{ address }} | {{ phone }} | {{ email }}</div>
    </div>

    <div class="section-title">PROFESSIONAL EXPERIENCE</div>
    <div class="job">
        <div class="job-title">{{ j1_title }}</div>
        <ul>
            {% for bullet in j1_bullets.split(',') %}
            <li>{{ bullet.strip() }}</li>
            {% endfor %}
        </ul>
    </div>
    
    <div class="job">
        <div class="job-title">{{ j2_title }}</div>
        <ul>
            {% for bullet in j2_bullets.split(',') %}
            <li>{{ bullet.strip() }}</li>
            {% endfor %}
        </ul>
    </div>

    <div class="section-title">TECHNICAL SKILLS</div>
    <p>{{ skills }}</p>
</body>
</html>
"""

# --- PREVIEW RENDER ---
t = Template(resume_template)
html_out = t.render(
    name=name, license=license, email=email, phone=phone, address=address,
    j1_title=j1_title, j1_bullets=j1_bullets,
    j2_title=j2_title, j2_bullets=j2_bullets,
    skills=skills
)

with col2:
    st.header("Live Preview")
    st.components.v1.html(html_out, height=800, scrolling=True)
    
    # Download Button
    b64 = base64.b64encode(html_out.encode()).decode()
    href = f'<a href="data:text/html;base64,{b64}" download="Resume_{name}.html" style="text-decoration:none;"><button style="width:100%; height:50px; background-color:#2c3e50; color:white; border:none; border-radius:5px; cursor:pointer;">Download as HTML (Print to PDF from Browser)</button></a>'
    st.markdown(href, unsafe_base64=True)