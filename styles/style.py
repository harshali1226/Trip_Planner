"""
Custom styling for AI Travel Planner chatbot
Inspired by USMLE-RAG chatbot design
"""

def get_custom_css():
    """Returns custom CSS for the travel planner chatbot"""
    return """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Container */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2c5f7c 0%, #1a3a4d 100%);
        padding: 2rem 1rem;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: transparent;
    }
    
    /* Sidebar Text */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: #ffffff !important;
    }
    
    /* Logo Container */
    .logo-container {
        background: linear-gradient(135deg, #4a90e2 0%, #2c5f7c 100%);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .logo-text {
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .logo-subtitle {
        color: #e0e0e0;
        font-size: 0.9rem;
        margin-top: 0.5rem;
        font-weight: 400;
    }
    
    /* About Section */
    .about-section {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        backdrop-filter: blur(10px);
    }
    
    .about-title {
        color: #ffffff;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .about-text {
        color: #e0e0e0;
        font-size: 0.9rem;
        line-height: 1.6;
    }
    
    /* Chat Container */
    .chat-container {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem auto;
        max-width: 1200px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
    }
    
    /* Chat Header */
    .chat-header {
        text-align: center;
        margin-bottom: 2rem;
        padding-bottom: 1.5rem;
        border-bottom: 2px solid #f0f0f0;
    }
    
    .chat-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .chat-subtitle {
        color: #666;
        font-size: 1.1rem;
        font-weight: 400;
    }
    
    /* Question Box */
    .question-box {
        background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 100%);
        border-left: 4px solid #667eea;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    
    .question-label {
        color: #667eea;
        font-weight: 600;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .question-text {
        color: #333;
        font-size: 1rem;
        line-height: 1.6;
        margin: 0;
    }
    
    /* Answer Box */
    .answer-box {
        background: linear-gradient(135deg, #f0f9ff 0%, #f8f9fa 100%);
        border-left: 4px solid #10b981;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    
    .answer-label {
        color: #10b981;
        font-weight: 600;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .answer-content {
        color: #333;
        font-size: 1rem;
        line-height: 1.8;
    }
    
    /* Input Styling */
    .stTextInput > div > div > input {
        border-radius: 25px;
        border: 2px solid #e0e0e0;
        padding: 0.75rem 1.5rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Clear Chat Button */
    .clear-button > button {
        background: rgba(255, 255, 255, 0.2);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 10px;
        padding: 0.5rem 1rem;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .clear-button > button:hover {
        background: rgba(255, 255, 255, 0.3);
        border-color: rgba(255, 255, 255, 0.5);
    }
    
    /* Spinner */
    .stSpinner > div {
        border-color: #667eea;
    }
    
    /* Markdown Content in Answer */
    .answer-content h1,
    .answer-content h2,
    .answer-content h3 {
        color: #333;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .answer-content ul,
    .answer-content ol {
        margin-left: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .answer-content li {
        margin-bottom: 0.5rem;
    }
    
    .answer-content strong {
        color: #667eea;
        font-weight: 600;
    }
    
    .answer-content hr {
        border: none;
        border-top: 2px solid #f0f0f0;
        margin: 1.5rem 0;
    }
    
    /* Timestamp */
    .timestamp {
        color: #999;
        font-size: 0.85rem;
        font-style: italic;
        margin-top: 1rem;
        text-align: right;
    }
    
    /* Error/Success Messages */
    .stAlert {
        border-radius: 10px;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .chat-title {
            font-size: 2rem;
        }
        
        .chat-container {
            padding: 1rem;
            margin: 1rem;
        }
    }
    </style>
    """


def render_logo():
    """Renders the sidebar logo section"""
    return """
    <div class="logo-container">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🌍</div>
        <p class="logo-text">AI TRAVEL</p>
        <p class="logo-text">PLANNER</p>
    </div>
    """


def render_about_section():
    """Renders the about section in sidebar"""
    return """
    <div class="about-section">
        <div class="about-title">
            🧳 About
        </div>
        <p class="about-text">
            Plan your perfect trip with AI assistance. Get personalized itineraries, 
            destination recommendations, travel tips, and more – all powered by 
            advanced AI technology.
        </p>
    </div>
    """


def render_question_box(question_text):
    """Renders a styled question box"""
    return f"""
    <div class="question-box">
        <div class="question-label">
            👤 Your Travel Query:
        </div>
        <p class="question-text">{question_text}</p>
    </div>
    """


def render_answer_box(answer_text, timestamp):
    """Renders a styled answer box"""
    return f"""
    <div class="answer-box">
        <div class="answer-label">
            🤖 AI Travel Assistant:
        </div>
        <div class="answer-content">
            {answer_text}
        </div>
        <div class="timestamp">Generated on {timestamp}</div>
    </div>
    """