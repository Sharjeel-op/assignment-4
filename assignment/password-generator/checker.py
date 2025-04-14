import streamlit as st
import re
import random
import string

def generate_strong_password(length=12):
    """Generate a strong password of specified length"""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*"
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    remaining_length = length - len(password)
    all_chars = lowercase + uppercase + digits + special_chars
    password.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    random.shuffle(password)
    return ''.join(password)

def check_password_strength(password):
    """Check password strength and return score and feedback"""
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9)")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*)")
    
    # Common password check
    common_passwords = {"password123", "12345678", "qwerty123", "admin123"}
    if password.lower() in common_passwords:
        score = 0
        feedback.append("❌ This is a commonly used password. Please choose something more unique")
    
    return score, feedback

def get_strength_label(score):
    """Convert score to strength label"""
    if score == 4:
        return "Strong", "✅"
    elif score == 3:
        return "Moderate", "⚠️"
    else:
        return "Weak", "❌"

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

st.title("🔐 Password Strength Meter")
st.write("Check how strong your password is or generate a new secure password!")

# Tabs for different functions
tab1, tab2 = st.tabs(["Check Password", "Generate Password"])

# Password Checker Tab
with tab1:
    password = st.text_input("Enter your password:", type="password")
    if st.button("Check Strength"):
        if password:
            score, feedback = check_password_strength(password)
            strength, icon = get_strength_label(score)
            
            # Display result with appropriate color
            if strength == "Strong":
                st.success(f"{icon} Password Strength: {strength}")
                st.success("Excellent! Your password meets all security criteria!")
            elif strength == "Moderate":
                st.warning(f"{icon} Password Strength: {strength}")
            else:
                st.error(f"{icon} Password Strength: {strength}")
            
            # Show feedback if any
            if feedback:
                st.write("### Improvement Suggestions:")
                for suggestion in feedback:
                    st.write(suggestion)
        else:
            st.warning("Please enter a password to check")

# Password Generator Tab
with tab2:
    col1, col2 = st.columns([3, 1])
    with col1:
        password_length = st.slider("Password Length", min_value=8, max_value=32, value=12)
    with col2:
        st.write("")
        st.write("")
        if st.button("Generate"):
            generated_password = generate_strong_password(password_length)
            st.code(generated_password)
            st.success("✨ Strong password generated! Make sure to save it securely!")

# Add some spacing
st.write("")

# Information section
with st.expander("Password Security Tips 💡"):
    st.write("""
    ### Strong Password Guidelines:
    - At least 8 characters long
    - Mix of uppercase and lowercase letters
    - Include numbers (0-9)
    - Use special characters (!@#$%^&*)
    - Avoid common words and patterns
    - Don't use personal information
    """)