import streamlit as st
import requests
import datetime
import subprocess
import time
from styles.style import (
    get_custom_css,
    render_logo,
    render_about_section,
    render_question_box,
    render_answer_box
)

# Start backend server
subprocess.Popen([
    "uv", "run", "uvicorn",
    "main:app",
    "--host", "0.0.0.0",
    "--port", "8000"
])
time.sleep(2)

BASE_URL = "http://127.0.0.1:8000"

# Page Configuration
st.set_page_config(
    page_title="🌍 AI Travel Planner",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply Custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    # Logo
    st.markdown(render_logo(), unsafe_allow_html=True)
    
    # About Section
    st.markdown(render_about_section(), unsafe_allow_html=True)
    
    # Features Section
    st.markdown("""
    <div class="about-section">
        <div class="about-title">
            ✨ Features
        </div>
        <p class="about-text">
            • Personalized itineraries<br>
            • Destination recommendations<br>
            • Budget planning<br>
            • Local attractions & activities<br>
            • Travel tips & advice<br>
            • Real-time suggestions
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Clear Chat Button
    st.markdown('<div class="clear-button">', unsafe_allow_html=True)
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.2);">
        <p style="color: #e0e0e0; font-size: 0.75rem; text-align: center;">
            Powered by Harshali Vasant Gaikwad<br>
            © 2026 AI Travel Planner
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==================== MAIN CONTENT ====================

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat Container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Header
st.markdown("""
<div class="chat-header">
    <h1 class="chat-title">AI Travel Planner</h1>
    <p class="chat-subtitle">✈️ Where would you like to go? Let's plan your perfect trip together!</p>
</div>
""", unsafe_allow_html=True)

# Display Chat History
if st.session_state.messages:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(render_question_box(message["content"]), unsafe_allow_html=True)
        else:
            st.markdown(
                render_answer_box(message["content"], message["timestamp"]),
                unsafe_allow_html=True
            )
else:
    # Welcome message when no chat history
    st.markdown("""
    <div style="text-align: center; padding: 1rem 1rem; color: #666;">
        <div style="font-size: 6rem; margin-bottom: 1rem;">🗺️</div>
        <h3 style="color: #667eea; margin-bottom: 1rem;">Ready to Plan Your Adventure?</h3>
        <p style="font-size: 1.1rem; line-height: 1.6; max-width: 600px; margin: 0 auto;">
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ==================== INPUT SECTION ====================
st.markdown('<div style="margin-top: 2rem;">', unsafe_allow_html=True)

# Chat input form
with st.form(key="query_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    
    with col1:
        user_input = st.text_input(
            "Your travel question",
            placeholder="e.g., Plan a 5-day trip to Paris with a budget of $2000",
            label_visibility="collapsed"
        )
    
    with col2:
        submit_button = st.form_submit_button("Send", use_container_width=True)

# Handle form submission
if submit_button and user_input.strip():
    try:
        # Add user message to chat history
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.datetime.now().strftime('%Y-%m-%d at %H:%M')
        })
        
        # Show thinking spinner
        with st.spinner("🤔 Planning your perfect trip..."):
            payload = {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload, timeout=60)
        
        if response.status_code == 200:
            answer = response.json().get("answer", "No answer returned.")
            
            # Add bot response to chat history
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "timestamp": datetime.datetime.now().strftime('%Y-%m-%d at %H:%M')
            })
            
            # Rerun to display new messages
            st.rerun()
        else:
            st.error(f"❌ Failed to get response: {response.text}")
    
    except requests.exceptions.Timeout:
        st.error("⏱️ Request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        st.error("🔌 Could not connect to the backend server. Please ensure it's running.")
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")

st.markdown('</div>', unsafe_allow_html=True)

# ==================== EXAMPLE QUERIES ====================
if not st.session_state.messages:
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <h4 style="color: #667eea; margin-bottom: 1rem;">💡 Try These Example Queries</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏖️ Beach vacation in Florida", use_container_width=True):
            st.session_state.example_query = "Plan a 5-day beach vacation in Florida"
            st.rerun()
    
    with col2:
        if st.button("⛰️ Mountain trek in Himalayas", use_container_width=True):
            st.session_state.example_query = "Plan a 7-day mountain trekking trip in Himalayas"
            st.rerun()
    
    with col3:
        if st.button("🏛️ Historical tour of Paris", use_container_width=True):
            st.session_state.example_query = "Plan a 10-day historical tour for Paris"
            st.rerun()
    
    # Handle example query click
    if "example_query" in st.session_state:
        user_input = st.session_state.example_query
        del st.session_state.example_query
        
        # Process the example query
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.datetime.now().strftime('%Y-%m-%d at %H:%M')
        })
        
        with st.spinner("🤔 Planning your perfect trip..."):
            try:
                payload = {"question": user_input}
                response = requests.post(f"{BASE_URL}/query", json=payload, timeout=60)
                
                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer returned.")
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer,
                        "timestamp": datetime.datetime.now().strftime('%Y-%m-%d at %H:%M')
                    })
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
        
        st.rerun()