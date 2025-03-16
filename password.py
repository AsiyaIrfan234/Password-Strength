# import streamlit as st
# import re

# st.set_page_config(page_title="Password Strength Meter",page_icon="🔒")
# st.title("🔒Password Strength Meter")
# st.markdown("""
# ## Welcome to the ultimate Password Strength Meter!
# use this simple tool to check the strength of your password and get suggestion on how to make it
# we will give you helpful tips to create a **Strong Password** 🔒""")

# password = st.text_input("Enter ypur password", type="password")
# feedback = []
# score = 0
# if password:
#     if len(password) >= 8:
#         score += 1
#     else :
#         feedback.append("❌Password should be at least 8 characters long.")

#         if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
#             score += 1
#         else:
#              feedback.append("❌Password should contain both uper and lower case characters.")

#         if re.search(r'\d', password):
#             score += 1
#         else:
#             feedback.append("❌Password should contain at least one digit.")

#         if re.search(r'[!@#$%&*]', password):
#             score += 1
#         else:
#             feedback.append("❌Password should contain at least one special character(!@#$%&*).")
#         if score == 4:
#                 feedback.append('✅Your password is strong!💥')
#         elif score == 3:
#                 feedback.append("Your Password is medium strength. It could be stronger.")
#         else:
#              feedback.append("Your password is weak. Please make it stronger.")
#         if feedback:
#              st.markdown("## Improvement Suggestions")
#              for tip in feedback:
#                   st.write(tip)
#         else:
#              st.info("Please enter your password to get started.")

import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")
st.title("🔒 Password Strength Meter")
st.markdown("""
## Strengthen Your Security with Our Password Strength Meter!  
Worried about how strong your password is? Use this simple yet powerful tool to analyze your password's strength and receive expert suggestions to enhance it.  

🔐 **Why Choose a Strong Password?**  
A strong password is your first defense against online threats. We'll guide you with actionable tips to build an unbreakable password fortress!  

Ready to test your password? Let's go! 🚀  
""")

password = st.text_input("Enter your password", type="password")
feedback = []
score = 0

if password:
    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check for upper and lower case characters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both upper and lower case characters.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%&*).")

    # Overall feedback based on score
    if score == 4:
        feedback.append('✅ Great job! Your password is strong and secure! 💪')
    elif score == 3:
        feedback.append("⚠️ Not bad! Your password is medium strength. Consider enhancing it for better security.")
    else:
        feedback.append("❌ Weak password! Strengthen it with uppercase, digits, and special characters.")

    # Display feedback
    st.markdown("## Suggestions to Improve Your Password")
    for tip in feedback:
        st.write(tip)

else:
    st.info("Start by entering your password above to check its strength and get tips for improvement.")
