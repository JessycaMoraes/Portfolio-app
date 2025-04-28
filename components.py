import streamlit as st
import math
import base64

def link_button(label, icon, target_id, css_class):
    st.markdown(f"""
        <form action="#{target_id}">
            <button class="{css_class}" type="submit">
                {icon} <span class="text-link">{label}</span>
            </button>
        </form>
    """, unsafe_allow_html=True)

def exp_card(logo_path, title, subtitle, period, description):
    col1, col2 = st.columns([1, 13])
    with col1:
        st.image(logo_path, width = 40)
    with col2:
        with st.expander(f"*{title}*  \n{subtitle}  \n_{period}_"):
            st.markdown(description)

def render_section_exp(title, emoji, items, flag=""):
    st.markdown(f"<h4 style='margin-top: 20px;'>{emoji} {title} {flag}</h4>", unsafe_allow_html=True)
    for item in items:
        exp_card(item["logo"], item["title"], item["subtitle"], item["period"], item["desc"])

def _img_to_base64(image_path):
    import base64
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return encoded

def project_card(title, description, year, tag1, tag2, tag3, image_path, link):
    st.markdown(f"""
        <div class="project-card">
            <img src="data:image/png;base64,{_img_to_base64(image_path)}" class="project-logo"/>
            <div class="card-project-title">
                <a href="{link}" target="_blank" style="color: #60B4FF;">{title}</a>
            </div>
            <div class="card-project-desc">{description}</div>
            <div class="card-project-year">{year}</div>
            <span class="tag tag-blue">{tag1}</span>
            <span class="tag tag-gold">{tag2}</span>
            <span class="tag tag-green">{tag3}</span>
        </div>
    """, unsafe_allow_html = True)

def total_pages(filtered_projects, projects_per_page):
    return max(1, math.ceil(len(filtered_projects) / projects_per_page))

def previous_page():
    if st.session_state.current_page > 1:
        st.session_state.current_page -= 1

def next_page(filtered_projects, projects_per_page):
    totalPages = total_pages(filtered_projects, projects_per_page)
    if st.session_state.current_page < totalPages:
        st.session_state.current_page += 1

def generate_hire_cards_html(css_string, card_data):
    html = f"""
    <style>
    {css_string}
    </style>
    <div class="cards-hire-container">
    """

    for card in card_data:
        html += f"""
        <div class="card-hire">
            <div class="inner-card-hire">
                <div class="hire-front">
                    <img src="{card['img']}" alt="{card['title']}">
                    <h3>{card['title']}</h3>
                </div>
                <div class="hire-back">
                    {card['back']}
                </div>
            </div>
        </div>
        """

    html += """
    </div>
    """
    return html

def download_button(file_path, button_text):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_path.split("/")[-1]}" class="download-cv-button">{button_text}</a>'
    return href

def create_card_contact(icon_path, text, url):
    img_base64 = _img_to_base64(icon_path)
    return f"""
        <a href="{url}" target="_blank">
            <div class="card-contact">
                <img src="data:image/png;base64,{img_base64}"/><br><b>{text}</b>
            </div>
        </a>
    """

def render_section_contact(contacts):
    col1, col2, col3 = st.columns(3)
    for i, col in enumerate([col1, col2, col3]):
        with col:
            st.markdown(create_card_contact(contacts[i]['icon'], contacts[i]['text'], contacts[i]['url']), unsafe_allow_html = True)