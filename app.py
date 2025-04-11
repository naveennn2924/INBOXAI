import streamlit as st
from tools.email_utils import fetch_unread_emails, send_email
from workflow.email_response_flow import email_response_flow
import os
EMAIL = os.getenv("EMAIL_ADDRESS")
st.set_page_config(page_title="📬 AI Email Responder", layout="wide")


st.markdown("""
    <style>
        .stApp {
            background-color: #000000;
            color: white;
        }
        .stButton>button {
            background-color: #007BFF;
            color: white;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .stTextArea>textarea {
            border-radius: 10px;
            border: 1px solid #ddd;
            padding: 10px;
        }
        .expanderHeader {
            font-size: 1.2em;
            font-weight: bold;
        }
        .stSidebar {
            background-color: #2e3b4e;
            color: white;
        }
        .stSidebar .stButton>button {
            background-color: #28a745;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📬 AI Email Responder Dashboard")


if "processed_emails" not in st.session_state:
    st.session_state.processed_emails = []


st.sidebar.markdown("<h3 style='color: white;'>📥 Inbox Actions</h3>", unsafe_allow_html=True)
st.sidebar.markdown("### 🔄 Refresh Inbox")
if st.sidebar.button("Fetch New Emails"):
    with st.spinner('Fetching emails...'):
        emails = fetch_unread_emails()
        st.session_state.processed_emails = []
        for email in emails:
            result = email_response_flow(email)
            st.session_state.processed_emails.append(result)
        st.success("📥 Emails fetched successfully!")

if not st.session_state.processed_emails:
    st.info("Click 'Fetch New Emails' to begin.")
else:
    for idx, entry in enumerate(st.session_state.processed_emails):
        with st.expander(f"📩 {entry['subject']} — from {entry['from']}", expanded=True):
            st.markdown(f"**🧠 Classification:** {entry['classification']}", unsafe_allow_html=True)
            st.text_area("📨 Email Body", entry['body'], height=200, key=f"body_{idx}")
            edited_reply = st.text_area(
                "✍️ AI Suggested Reply", entry['reply'], height=200, key=f"reply_{idx}"
            )

            # Add columns for actions
            col1, col2 = st.columns(2)

            with col1:
                if st.button("✅ Send Reply", key=f"send_{idx}"):
                    send_email(EMAIL, entry["from"], f"Re: {entry['subject']}", edited_reply)
                    st.success("📤 Email sent!")

            with col2:
                if st.button("🗑️ Skip", key=f"skip_{idx}"):
                    st.warning("⏭️ Skipped.")


st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <p style='color: gray;'>Built with ❤️ by Naveen Narasimhappa</p>
        <p><a href="https://github.com/naveennn2924">Check out our GitHub</a></p>
    </div>
""", unsafe_allow_html=True)
