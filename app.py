"""
CyberNavigator - Career DNA Quiz Application
Main Streamlit interface for the cyber security career assessment quiz.
"""

import streamlit as st
import plotly.graph_objects as go
from dotenv import load_dotenv
from engine.assessor import QUIZ_QUESTIONS, get_cyber_domain
from engine.market_intel import fetch_market_trends
from engine.roadmap_gen import generate_roadmap

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="CyberNavigator - Career DNA Quiz",
    page_icon="🔒",
    layout="wide"
)

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 1

if 'responses' not in st.session_state:
    st.session_state.responses = [None] * 10

if 'quiz_complete' not in st.session_state:
    st.session_state.quiz_complete = False

if 'results' not in st.session_state:
    st.session_state.results = None

if 'market_data' not in st.session_state:
    st.session_state.market_data = None

if 'roadmap' not in st.session_state:
    st.session_state.roadmap = None

if 'roadmap_generated' not in st.session_state:
    st.session_state.roadmap_generated = False

if 'selected_page' not in st.session_state:
    st.session_state.selected_page = 'Career Navigator'


def display_question(question_num):
    """Display a single quiz question with options."""
    question_data = QUIZ_QUESTIONS[question_num]
    
    st.subheader(f"Question {question_num} of 10")
    st.markdown(f"### {question_data['question']}")
    st.markdown("---")
    
    # Display options as radio buttons
    options = list(question_data['options'].keys())
    option_labels = {opt: question_data['options'][opt] for opt in options}
    
    # Get current selection if exists
    current_selection = st.session_state.responses[question_num - 1]
    selected_index = options.index(current_selection) if current_selection in options else 0
    
    selected = st.radio(
        "Select your answer:",
        options=options,
        format_func=lambda x: f"{x}: {option_labels[x]}",
        index=selected_index if current_selection in options else None,
        key=f"question_{question_num}"
    )
    
    # Store the response
    st.session_state.responses[question_num - 1] = selected
    
    return selected


def create_radar_chart(scores):
    """Create a Plotly radar chart for domain scores."""
    categories = list(scores.keys())
    values = list(scores.values())
    
    # Create radar chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Your Scores',
        line_color='rgb(32, 201, 151)',
        fillcolor='rgba(32, 201, 151, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(values) + 5] if max(values) > 0 else [0, 10]
            )),
        showlegend=True,
        title="Career Domain Score Breakdown",
        font=dict(size=14),
        height=500
    )
    
    return fig


def display_results():
    """Display quiz results with radar chart."""
    if st.session_state.results is None:
        return
    
    results = st.session_state.results
    
    st.markdown("---")
    st.markdown("# 🎯 Your Career DNA Results")
    st.markdown("---")
    
    # Display primary domain
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"### Your Primary Domain: **{results['full_name']}**")
        st.markdown(f"**Confidence:** {results['confidence']}%")
        
        # Domain descriptions
        domain_descriptions = {
            "Red Team (Offensive)": "You're drawn to offensive security! Red Team professionals simulate attacks, find vulnerabilities, and think like adversaries. Perfect for penetration testing, ethical hacking, and security research.",
            "Blue Team (Defensive)": "You excel at defensive security! Blue Team professionals build and maintain security infrastructure, monitor threats, and respond to incidents. Ideal for SOC analysts, security engineers, and incident responders.",
            "Application Security": "You're passionate about secure code! AppSec professionals review code, find vulnerabilities, and ensure applications are built securely. Great for security engineers, code reviewers, and DevSecOps roles.",
            "GRC (Governance, Risk & Compliance)": "You understand the big picture! GRC professionals ensure organizations meet compliance standards, manage risk, and develop security policies. Perfect for compliance officers, risk analysts, and security auditors.",
            "Cloud Security": "You're focused on cloud infrastructure! Cloud Security professionals secure cloud environments, configure security controls, and manage cloud-based security solutions. Ideal for cloud security engineers and architects."
        }
        
        st.info(domain_descriptions.get(results['full_name'], "Explore this domain to learn more about your career path!"))
    
    with col2:
        st.metric("Total Questions", "10")
        st.metric("Completed", "✅")
    
    # Display radar chart
    st.markdown("### 📊 Domain Score Breakdown")
    radar_fig = create_radar_chart(results['scores'])
    st.plotly_chart(radar_fig, use_container_width=True)
    
    # Display all scores in a table
    st.markdown("### 📈 Detailed Scores")
    score_data = {
        "Domain": list(results['scores'].keys()),
        "Score": list(results['scores'].values())
    }
    st.dataframe(score_data, use_container_width=True, hide_index=True)


def main():
    """Main application function."""
    # Sidebar navigation
    with st.sidebar:
        st.title("🔒 CyberNavigator")
        st.markdown("---")
        page_options = ["Career Navigator", "Vulnerability Scanner"]
        current_index = 0 if st.session_state.selected_page == 'Career Navigator' else 1
        selected_page = st.selectbox(
            "Navigate",
            page_options,
            index=current_index,
            key="page_selector"
        )
        st.session_state.selected_page = selected_page
        st.markdown("---")
    
    # Only show Career Navigator content when selected
    if st.session_state.selected_page != 'Career Navigator':
        # Placeholder for Vulnerability Scanner
        st.title("🔒 CyberNavigator")
        st.markdown("### Vulnerability Scanner")
        st.info("🚧 Vulnerability Scanner feature coming soon!")
        return
    
    # Career Navigator content
    # Header
    st.title("🔒 CyberNavigator")
    st.markdown("### Discover Your Cyber Security Career Path")
    st.markdown("Take our Career DNA Quiz to find out which cyber security domain aligns best with your interests and skills!")
    st.markdown("---")
    
    # Check if quiz is complete
    if st.session_state.quiz_complete and st.session_state.results:
        # Display results
        display_results()
        
        # Display market intelligence if available
        if st.session_state.market_data:
            st.markdown("---")
            st.markdown("## 📊 Market Intelligence")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🔥 Trending Skills")
                st.dataframe(
                    st.session_state.market_data['trending_skills'],
                    use_container_width=True,
                    hide_index=True
                )
            
            with col2:
                st.markdown("### 🏆 Top Certifications")
                st.dataframe(
                    st.session_state.market_data['certifications'],
                    use_container_width=True,
                    hide_index=True
                )
        
        # Generate Roadmap section
        st.markdown("---")
        
        if not st.session_state.roadmap_generated:
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                if st.button("🗺️ Generate Roadmap", type="primary", use_container_width=True):
                    if st.session_state.results and st.session_state.market_data:
                        try:
                            with st.spinner("🤖 Generating your personalized roadmap... This may take a moment."):
                                roadmap = generate_roadmap(
                                    st.session_state.results['domain'],
                                    st.session_state.market_data
                                )
                                st.session_state.roadmap = roadmap
                                st.session_state.roadmap_generated = True
                                st.rerun()
                        except Exception as e:
                            st.error(f"Error generating roadmap: {str(e)}")
                            st.info("💡 Tip: Make sure you have GEMINI_API_KEY or OPENAI_API_KEY set in your .env file.")
                    else:
                        st.warning("Please complete the quiz first.")
        else:
            # Display the roadmap
            st.markdown("## 🗺️ Your Personalized Learning Roadmap")
            st.markdown("---")
            st.markdown(st.session_state.roadmap)
            
            # User feedback after roadmap display
            st.feedback('thumbs', key="roadmap_feedback")
            
            # Option to regenerate roadmap
            if st.button("🔄 Regenerate Roadmap"):
                st.session_state.roadmap = None
                st.session_state.roadmap_generated = False
                st.rerun()
        
        # Option to retake quiz
        st.markdown("---")
        if st.button("🔄 Retake Quiz"):
            st.session_state.current_question = 1
            st.session_state.responses = [None] * 10
            st.session_state.quiz_complete = False
            st.session_state.results = None
            st.session_state.market_data = None
            st.session_state.roadmap = None
            st.session_state.roadmap_generated = False
            st.rerun()
    
    else:
        # Quiz interface
        current_q = st.session_state.current_question
        
        # Progress bar
        progress = current_q / 10
        st.progress(progress, text=f"Progress: {current_q}/10 questions")
        
        # Display current question
        selected_answer = display_question(current_q)
        
        # Navigation buttons
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        
        with col1:
            if st.button("◀️ Previous", disabled=(current_q == 1)):
                st.session_state.current_question = max(1, current_q - 1)
                st.rerun()
        
        with col4:
            if current_q < 10:
                if st.button("Next ▶️", type="primary"):
                    if selected_answer:
                        st.session_state.current_question = min(10, current_q + 1)
                        st.rerun()
                    else:
                        st.warning("Please select an answer before proceeding.")
            else:
                # Last question - show submit button
                if st.button("✅ Submit Quiz", type="primary"):
                    if selected_answer:
                        # Check if all questions are answered
                        if None in st.session_state.responses:
                            unanswered = [i+1 for i, r in enumerate(st.session_state.responses) if r is None]
                            st.error(f"Please answer all questions. Missing: {unanswered}")
                        else:
                            # Calculate results
                            try:
                                with st.spinner("Analyzing your responses..."):
                                    results = get_cyber_domain(st.session_state.responses)
                                    st.session_state.results = results
                                    
                                    # Fetch market trends based on the domain
                                    with st.spinner("Fetching market intelligence..."):
                                        market_data = fetch_market_trends(results['domain'])
                                        st.session_state.market_data = market_data
                                    
                                    st.session_state.quiz_complete = True
                                    st.rerun()
                            except ValueError as e:
                                st.error(f"Error processing quiz: {str(e)}")
                            except Exception as e:
                                st.error(f"Error fetching market data: {str(e)}")
                    else:
                        st.warning("Please select an answer before submitting.")


if __name__ == "__main__":
    main()
