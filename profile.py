import streamlit as st
import math
import streamlit.components.v1 as componentsv1
from components import (
    link_button,
    exp_card,
    render_section_exp,
    _img_to_base64,
    project_card,
    total_pages,
    previous_page,
    next_page,
    generate_hire_cards_html,
    download_button,
    render_section_contact
)
from app_data.tools import tools
from app_data.experiences import (
    experiences, 
    education_br, 
    education_us, 
    cert_courses
)
from app_data.projects import projects
from app_data.hire import css, card_data
from app_data.testimonials import testimonials
from app_data.contacts import contacts

#HEADER

col1, col2 = st.columns(2)

with col1:
    st.title("Hey there! :wave:")
    st.header("I’m Jessyca Moraes a Brazilian Data Analyst")
    st.subheader("and this is my professional journey.")

with col2:
    st.image("assets/images/Perfil Picture.png")

with open("assets/styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------

#BUTTONS

link_button("About me", "👩‍💻", "about", "btn-link-blue")
link_button("Tools", "🛠️", "skills", "btn-link-skyBlue")
link_button("Professional timeline", "⏳", "timeline", "btn-link-purple")
link_button("My Projects", "📂", "projects", "btn-link-green")
link_button("Why hire me?", "💼", "why_hire", "btn-link-orange")
link_button("Testimonials", "💬", "testimonials", "btn-link-magenta")
link_button("Contact", "📬", "contact", "btn-link-red")

#---------------------------------------------------------------------------------------------

#SECTION 1 - ABOUT ME

st.markdown("<div id='about'></div>", unsafe_allow_html = True)
st.markdown("<h2 style='color:#2563EB; margin-top: 15px;'>👩‍💻 About me</h2>", unsafe_allow_html = True)

st.write("""
I'm a data enthusiast with over 4 years of experience turning raw data into meaningful insights.  
My journey has taken me through data engineering, analysis, and collaboration with cross-functional teams to build solutions that are both scalable and impactful.

I specialize in building efficient ETL pipelines, working with Python and SQL, and delivering data that drives decision-making and business growth.  
I enjoy working at the intersection of business and technology — translating complex data into stories that matter.

When I'm not solving data problems, I enjoy exploring new ways to optimize data workflows and experimenting with tools that make data work smarter.

I'm always looking to grow as a data professional — diving deeper into analytics engineering, learning from others, and contributing to data-driven cultures that empower both people and products.

Let’s connect and create something awesome together.
""")

## Subsection
st.markdown("""
    <h4 style='margin-top: 30px;'>Personal Facts</h4>
    <hr style='border: none; height: 1px; background-color: #64748B; margin-top: 1px; margin-bottom: 12px;'/>
""", unsafe_allow_html = True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("🐶 I have two dogs and a cat that make my life fun and full of energy.")
    st.markdown("🌍 I'm originally from Manaus, Amazonas — the heart of the Amazon rainforest.")
    st.markdown("✈️ I went on an exchange program to Arizona in 2014, which helped expand my horizons.")

with col2:
    st.markdown("🇯🇵 I'm passionate about Japanese culture and even studied the language!")
    st.markdown("🇺🇸 I helped a friend from Japan with English translation during their five-day visit to my city.")
    st.markdown("🗾 One of my dreams is to visit Japan one day and experience its culture firsthand!")

#---------------------------------------------------------------------------------------------

#SECTION 2 - SKILLS

st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
st.markdown("<h2 style='color:#60B4FF; margin-top: 15px;'>🛠️ Tools</h2>", unsafe_allow_html=True)

cols = st.columns(3)
for i, tool in enumerate(tools):
    img_base64 = _img_to_base64(tool['url_tool'])
    with cols[i % 3]:
        st.markdown(f"""
            <div class="tool-card">
                <img src="data:image/png;base64,{img_base64}"><br>
                <span>{tool['name_tool']}</span>
            </div>
        """, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------

#SECTION 3 - TIMELINE

st.markdown("<div id='timeline'></div>", unsafe_allow_html = True)
st.markdown("<h2 style='color:#B27EFF; margin-top: 25px;'>⏳ Professional timeline</h2>", unsafe_allow_html = True)

render_section_exp("Work Experience", "💼", experiences)
render_section_exp("Education", "🎓", education_br, "🇧🇷")
render_section_exp("Education", "🎓", education_us, "🇺🇸")
render_section_exp("Certificates/Courses", "🏆", cert_courses)

#---------------------------------------------------------------------------------------------

#SECTION 4 - PROJECTS

st.markdown("<div id='projects'></div>", unsafe_allow_html = True)
st.markdown("<h2 style='color:#3DD56D; margin-top: 25px;'>📂 My Projects</h2>", unsafe_allow_html = True)

## Filter by tags
all_tags = sorted(set(tag for p in projects for tag in [p["tag1"], p["tag2"], p["tag3"]]))
selected_tags = st.multiselect("Filter by tags", all_tags)

## Reset page to 1 whenever selected tags change
if "selected_tags_anterior" not in st.session_state or st.session_state.selected_tags_anterior != selected_tags:
    st.session_state.current_page = 1
    st.session_state.selected_tags_anterior = selected_tags

## Apply filter
filtered_projects = [
    p for p in projects
    if not selected_tags or any(tag in selected_tags for tag in [p["tag1"], p["tag2"], p["tag3"]])
]

## Pagination
projects_per_page = 6
total_pages = total_pages(filtered_projects, projects_per_page)

## Creating a state for the page
if "current_page" not in st.session_state:
    st.session_state.current_page = 1

## Indexes for display
start_idx = (st.session_state.current_page - 1) * projects_per_page
end_idx = start_idx + projects_per_page
paginated_projects = filtered_projects[start_idx:end_idx]

## Layout in columns (3 columns)
cols = st.columns(3)
for idx, project in enumerate(paginated_projects):
    with cols[idx % 3]:
        project_card(
            title = project["title"],
            description = project["description"],
            year = project["year"],
            tag1 = project["tag1"],
            tag2 = project["tag2"],
            tag3 = project["tag3"],
            image_path = project["image_path"],
            link = project["link"]
        )

st.markdown(f"<p style='text-align:center;'>Página {st.session_state.current_page} de {total_pages}</p>", unsafe_allow_html=True)

## Navigation buttons
btn_col1, btn_col2, btn_col3 = st.columns([4, 1, 1])
with btn_col1:
    st.button("⬅️ Anterior", on_click = previous_page)
with btn_col3:
    st.button("Próxima ➡️", on_click = lambda: next_page(filtered_projects, projects_per_page))

#---------------------------------------------------------------------------------------------

#SECTION 5 - HIRE ME

st.markdown("<div id='why_hire'></div>", unsafe_allow_html = True)
st.markdown("### <h2 style='color:#FFBD44; margin-top: -25px;'>💼 Why hire me?</h2>", unsafe_allow_html = True)

st.caption("Hover over the cards to see more ℹ️")

## Cards
hire_cards_html = generate_hire_cards_html(css, card_data)
componentsv1.html(hire_cards_html, height = 1100, scrolling = False)

## Footnote
st.markdown("<div class='footer-message'> Let's build data-driven success together! 🚀</div>", unsafe_allow_html = True)

cv_en_path = "assets/CVs/JessycaMoraesResumeDA25.pdf"
cv_pt_path = "assets/CVs/JessycaMoraesCurriculoAD25.pdf"

## Download buttons
download_link_en = download_button(cv_en_path, "↓ Download CV (EN)")
download_link_pt = download_button(cv_pt_path, "↓ Download CV (PT)")

st.markdown(f'<div class="download-cv-button-container">{download_link_en} {download_link_pt}</div>', unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------

#SECTION 6 - TESTIMONIALS

st.markdown("<div id='testimonials'></div>", unsafe_allow_html = True)
st.markdown("### <h2 style='color:#00BCD4; margin-top: -15px;'>💬 Testimonials</h2>", unsafe_allow_html = True)

for testimonial in testimonials:
    with st.expander(f"👤 **{testimonial['name']}** | *{testimonial['position']}*"):
        st.markdown(f"<h4 style='color: #00BCD4; margin-top: 0;'>{testimonial['name']}</h4>", unsafe_allow_html = True)
        st.write(f"**Relationship**: {testimonial['relationship']}")
        st.write(f"**Date**: {testimonial['date']}")
        st.write(testimonial['text'])

#---------------------------------------------------------------------------------------------

#SECTION 7 - CONTACT

st.markdown("<div id='contact'></div>", unsafe_allow_html = True)
st.markdown("### <h2 style='color:#FF4B4B; margin-top: -35px;'>📬 Contact</h2>", unsafe_allow_html = True)


col1, col2, col3 = st.columns(3)
for i, col in enumerate([col1, col2, col3]):
    with col:
        img_base64 = _img_to_base64(contacts[i]['icon'])
        st.markdown(f"""
            <a href="{contacts[i]['url']}" target="_blank">
                <div class="card-contact">
                    <img src="data:image/png;base64,{img_base64}"/><br><b>{contacts[i]['text']}</b>
                </div>
            </a>
        """, unsafe_allow_html = True)