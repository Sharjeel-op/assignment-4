import streamlit as st

# Configure the page to use the full width of the screen
st.set_page_config(
    page_title="Responsive Streamlit App",
    page_icon="🌐",
    layout="wide",
)

# Inject CSS for better visual appearance
st.markdown("""
    <style>
        body {
            margin: 0;
            padding: 0;
        }
        .block-container {
            padding: 2rem 5rem;
        }
        .stTextInput>div>div>input {
            border-radius: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🌐 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "ℹ️ About", "📞 Contact"])

# ---------- HOME PAGE ----------
if page == "🏠 Home":
    st.markdown("## 🏡 Welcome to the Home Page")
    st.write("This app is fully responsive and beautiful, built with **Streamlit + CSS**.")

    with st.container():
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image("https://source.unsplash.com/800x500/?nature,water", caption="Stunning Views", use_column_width=True)
        with col2:
            st.subheader("🌟 Interactive Welcome Form")
            name = st.text_input("Your Name")
            hobby = st.selectbox("Favorite Hobby", ["Reading", "Traveling", "Coding", "Gaming"])
            if name:
                st.success(f"Hello **{name}** 👋! It's awesome that you love **{hobby}**.")

# ---------- ABOUT PAGE ----------
elif page == "ℹ️ About":
    st.markdown("## ℹ️ About This App")
    st.write("""
        This web app is built using [Streamlit](https://streamlit.io/). It demonstrates how you can
        build beautiful multi-page responsive layouts quickly.
    """)
    st.markdown("### 🔧 Tech Stack")
    st.markdown("""
    - Python 🐍
    - Streamlit 🚀
    - Custom CSS 🎨
    """)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://source.unsplash.com/400x400/?tech,code", use_column_width=True)
    with col2:
        st.info("Want to learn Streamlit? Check out [Streamlit Docs](https://docs.streamlit.io/)")

# ---------- CONTACT PAGE ----------
elif page == "📞 Contact":
    st.markdown("## 📞 Get in Touch")
    st.write("We'd love to hear from you. Fill out the form below 👇")

    with st.form(key='contact_form'):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name")
            email = st.text_input("Email")
        with col2:
            topic = st.selectbox("Topic", ["Feedback", "Support", "General Inquiry"])
            urgency = st.radio("Urgency", ["Low", "Medium", "High"])

        message = st.text_area("Your Message", height=150)
        submit = st.form_submit_button(label="📨 Send Message")

        if submit:
            st.success(f"Thanks, {name}! Your message about **{topic}** was sent. We'll get back to you soon!")

# ---------- FOOTER ----------
st.markdown("""---""")
st.markdown("<center>Made with ❤️ using Streamlit | © 2025</center>", unsafe_allow_html=True)
