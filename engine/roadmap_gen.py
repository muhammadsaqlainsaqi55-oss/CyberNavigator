"""
Roadmap Generator Module
Creates personalized 6-month learning roadmaps for cyber security domains.
Uses AI (Gemini/OpenAI) to generate detailed, structured learning paths.
"""

import os
import json
from typing import Dict, Optional
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@st.cache_data(ttl=3600)
def _generate_with_gemini(domain: str, market_data: Dict, prompt_template: str) -> str:
    """
    Generate roadmap using Google Gemini API.
    Cached for 1 hour to reduce API calls.
    
    Args:
        domain: The cyber security domain
        market_data: Market intelligence data (trending skills and certifications)
        prompt_template: The prompt template to use
    
    Returns:
        Generated roadmap in markdown format
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    
    # Extract skills and certifications from market_data
    skills_list = market_data['trending_skills']['Trending Skill'].tolist() if hasattr(market_data['trending_skills'], 'tolist') else market_data['trending_skills']
    certs_list = market_data['certifications']['Certification'].tolist() if hasattr(market_data['certifications'], 'tolist') else market_data['certifications']
    
    # Format skills and certs for prompt
    skills_text = "\n".join([f"- {skill}" for skill in skills_list[:10]])
    certs_text = "\n".join([f"- {cert}" for cert in certs_list[:8]])
    
    # Build the prompt
    prompt = prompt_template.format(
        domain=domain,
        skills=skills_text,
        certifications=certs_text
    )
    
    # Call Gemini API (using gemini-1.5-flash or gemini-pro)
    model = "gemini-1.5-flash"  # Can be changed to gemini-pro for better quality
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    
    payload = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 3000
        }
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=60)
        response.raise_for_status()
        
        result = response.json()
        
        if 'candidates' in result and len(result['candidates']) > 0:
            if 'content' in result['candidates'][0] and 'parts' in result['candidates'][0]['content']:
                return result['candidates'][0]['content']['parts'][0]['text']
            else:
                raise ValueError("Unexpected response format from Gemini API")
        else:
            error_msg = result.get('error', {}).get('message', 'Unknown error')
            raise ValueError(f"Gemini API error: {error_msg}")
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error calling Gemini API: {str(e)}")


def _generate_with_openai(domain: str, market_data: Dict, prompt_template: str) -> str:
    """
    Generate roadmap using OpenAI API.
    
    Args:
        domain: The cyber security domain
        market_data: Market intelligence data (trending skills and certifications)
        prompt_template: The prompt template to use
    
    Returns:
        Generated roadmap in markdown format
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    # Extract skills and certifications from market_data
    skills_list = market_data['trending_skills']['Trending Skill'].tolist() if hasattr(market_data['trending_skills'], 'tolist') else market_data['trending_skills']
    certs_list = market_data['certifications']['Certification'].tolist() if hasattr(market_data['certifications'], 'tolist') else market_data['certifications']
    
    # Format skills and certs for prompt
    skills_text = "\n".join([f"- {skill}" for skill in skills_list[:10]])
    certs_text = "\n".join([f"- {cert}" for cert in certs_list[:8]])
    
    # Build the prompt
    prompt = prompt_template.format(
        domain=domain,
        skills=skills_text,
        certifications=certs_text
    )
    
    # Call OpenAI API
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-4",
        "messages": [
            {
                "role": "system",
                "content": "You are an expert cyber security career advisor who creates detailed, actionable learning roadmaps."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 3000
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content']
        else:
            raise ValueError("Unexpected response format from OpenAI API")
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error calling OpenAI API: {str(e)}")


def _get_red_team_prompt_template() -> str:
    """Get the specialized prompt template for Red Team roadmap."""
    return """Create a highly detailed 6-month offensive security (Red Team) learning roadmap for 2026.

The roadmap must be structured as follows:

**Month 1-2: Foundation & Core Skills**
- Linux/Networking mastery (detailed topics, hands-on labs, resources)
- Python for Exploits (specific libraries, projects, practice exercises)
- Command line proficiency
- Network protocols and security fundamentals

**Month 3: Web Application Penetration Testing**
- OWASP Top 10 2026 (detailed coverage of each vulnerability)
- Burp Suite Professional (installation, configuration, advanced features)
- Web application security testing methodology
- Hands-on practice on vulnerable applications (DVWA, WebGoat, etc.)

**Month 4: 2026 Emerging Skills**
- AI Red Teaming (testing AI systems for vulnerabilities)
- Prompt Injection attacks and defenses
- LLM Jailbreaking techniques
- AI/ML model adversarial attacks
- Practical labs and exercises

**Month 5: Certifications & Validation**
- Focus on key certifications:
  * CompTIA Security+ (SY0-701) preparation
  * OSCP (Offensive Security Certified Professional) study plan
  * CEH AI (Certified Ethical Hacker - AI Edition) preparation
- Practice exams and study resources
- Exam strategies and tips

**Month 6: Portfolio Development**
- Building a GitHub Portfolio of custom-coded security tools
- Project ideas and implementation guidance
- Code quality and documentation standards
- Contributing to open-source security projects
- Creating write-ups and blog posts

For each month, include:
- Specific learning objectives
- Recommended resources (books, courses, platforms)
- Hands-on practice exercises
- Milestones and checkpoints
- Time estimates for each topic

Format the output in clean Markdown with proper headers, bullet points, and code blocks where appropriate.

Trending Skills to incorporate:
{skills}

Top Certifications to consider:
{certifications}

Make the roadmap actionable, detailed, and professional."""


def _get_generic_prompt_template() -> str:
    """Get the generic prompt template for other domains."""
    return """Create a highly detailed 6-month cyber security learning roadmap for the {domain} domain in 2026.

Structure the roadmap across 6 months with progressive learning:

**Month 1-2: Foundation & Fundamentals**
- Core concepts and fundamentals
- Essential tools and technologies
- Hands-on practice and labs

**Month 3-4: Intermediate Skills & Specialization**
- Domain-specific advanced topics
- Practical applications
- Real-world scenarios

**Month 5: Certifications & Professional Development**
- Relevant certification preparation
- Study plans and resources
- Professional networking

**Month 6: Portfolio & Career Readiness**
- Building a professional portfolio
- Practical projects
- Career preparation

For each month, include:
- Specific learning objectives
- Recommended resources (books, courses, platforms)
- Hands-on practice exercises
- Milestones and checkpoints
- Time estimates for each topic

Format the output in clean Markdown with proper headers, bullet points, and code blocks where appropriate.

Trending Skills to incorporate:
{skills}

Top Certifications to consider:
{certifications}

Make the roadmap actionable, detailed, and professional."""


def generate_roadmap(domain: str, market_data: Dict) -> str:
    """
    Generate a personalized 6-month learning roadmap for a cyber security domain.
    
    Uses AI (Gemini or OpenAI) to create detailed, structured learning paths based on
    market intelligence data and domain-specific requirements.
    
    Args:
        domain: The cyber security domain (Red Team, Blue Team, AppSec, GRC, Cloud Security)
        market_data: Dictionary containing 'trending_skills' and 'certifications' DataFrames
                    from fetch_market_trends()
    
    Returns:
        str: Detailed roadmap in Markdown format, ready for display in Streamlit
    
    Raises:
        ValueError: If API keys are not configured
        Exception: If API call fails
    
    Example:
        >>> from engine.market_intel import fetch_market_trends
        >>> market_data = fetch_market_trends("Red Team")
        >>> roadmap = generate_roadmap("Red Team", market_data)
        >>> print(roadmap)
    """
    # Select prompt template based on domain
    if domain == "Red Team":
        prompt_template = _get_red_team_prompt_template()
    else:
        prompt_template = _get_generic_prompt_template()
    
    # Try Gemini first, then fallback to OpenAI
    try:
        if os.getenv("GEMINI_API_KEY"):
            return _generate_with_gemini(domain, market_data, prompt_template)
        elif os.getenv("OPENAI_API_KEY"):
            return _generate_with_openai(domain, market_data, prompt_template)
        else:
            # Fallback to template-based generation if no API keys
            return _generate_fallback_roadmap(domain, market_data)
    except Exception as e:
        # If API fails, use fallback
        try:
            return _generate_fallback_roadmap(domain, market_data)
        except Exception:
            raise Exception(f"Failed to generate roadmap: {str(e)}")


def _generate_fallback_roadmap(domain: str, market_data: Dict) -> str:
    """
    Generate a roadmap using template-based approach when API is unavailable.
    
    Args:
        domain: The cyber security domain
        market_data: Market intelligence data
    
    Returns:
        str: Roadmap in Markdown format
    """
    # Extract data
    if isinstance(market_data['trending_skills'], dict):
        skills = list(market_data['trending_skills'].values())[0] if market_data['trending_skills'] else []
    else:
        skills = market_data['trending_skills']['Trending Skill'].tolist()[:10]
    
    if isinstance(market_data['certifications'], dict):
        certs = list(market_data['certifications'].values())[0] if market_data['certifications'] else []
    else:
        certs = market_data['certifications']['Certification'].tolist()[:8]
    
    if domain == "Red Team":
        roadmap = f"""# 6-Month Offensive Security (Red Team) Roadmap

## Month 1-2: Foundation & Core Skills

### Linux/Networking Mastery
- **Linux Fundamentals**: Command line, file systems, permissions, process management
- **Networking**: TCP/IP, DNS, HTTP/HTTPS, network protocols, packet analysis with Wireshark
- **Hands-on Labs**: Set up Kali Linux, practice with TryHackMe Linux fundamentals
- **Resources**: Linux Command Line book, Network+ study materials

### Python for Exploits
- **Core Python**: Data structures, functions, classes, modules
- **Security Libraries**: Requests, Scapy, pwntools, paramiko
- **Projects**: Build a port scanner, create a simple exploit script
- **Practice**: Complete Python security challenges on HackTheBox

**Milestone**: Build a custom network scanner in Python

---

## Month 3: Web Application Penetration Testing

### OWASP Top 10 2026
- **A01: Broken Access Control**: IDOR, privilege escalation, JWT vulnerabilities
- **A02: Cryptographic Failures**: Weak encryption, improper key management
- **A03: Injection**: SQL injection, NoSQL injection, command injection
- **A04: Insecure Design**: Security misconfigurations, design flaws
- **A05: Security Misconfiguration**: Default credentials, exposed debug info
- **A06: Vulnerable Components**: Dependency vulnerabilities, outdated libraries
- **A07: Authentication Failures**: Weak passwords, session management issues
- **A08: Software and Data Integrity**: Supply chain attacks, CI/CD vulnerabilities
- **A09: Logging and Monitoring Failures**: Insufficient logging, alert fatigue
- **A10: Server-Side Request Forgery (SSRF)**: Internal network access, cloud metadata attacks

### Burp Suite Professional
- Installation and configuration
- Proxy, Repeater, Intruder, Decoder modules
- Extensions and automation
- Advanced scanning techniques

### Practice Platforms
- DVWA (Damn Vulnerable Web Application)
- WebGoat
- PortSwigger Web Security Academy
- TryHackMe Web Application Security rooms

**Milestone**: Complete 5 web application penetration tests and write reports

---

## Month 4: 2026 Emerging Skills

### AI Red Teaming
- Testing AI systems for vulnerabilities
- Adversarial machine learning
- Model poisoning and evasion attacks

### Prompt Injection & LLM Security
- **Prompt Injection**: Direct and indirect injection techniques
- **LLM Jailbreaking**: Bypassing safety filters, role-playing attacks
- **AI Model Adversarial Attacks**: Input manipulation, output manipulation
- **Practical Labs**: 
  - Test open-source LLMs for vulnerabilities
  - Create proof-of-concept prompt injection attacks
  - Practice on platforms like PromptInject, LLM Security

### Resources
- OWASP LLM Top 10
- AI Security research papers
- Hands-on practice with local LLM deployments

**Milestone**: Successfully demonstrate AI red teaming techniques on a test environment

---

## Month 5: Certifications & Validation

### CompTIA Security+ (SY0-701)
- **Study Plan**: 4-6 weeks
- **Resources**: CompTIA official study guide, Professor Messer videos, practice exams
- **Focus Areas**: Network security, threats and vulnerabilities, identity management

### OSCP Preparation
- **Prerequisites**: Strong Linux, networking, and web app security knowledge
- **Study Materials**: PWK course, HackTheBox, TryHackMe
- **Practice**: Complete 30+ machines on HackTheBox
- **Exam Strategy**: Time management, note-taking, report writing

### CEH AI (Certified Ethical Hacker - AI Edition)
- **Focus**: AI-specific ethical hacking techniques
- **Study Resources**: EC-Council materials, AI security courses
- **Practice**: AI red teaming labs and scenarios

**Milestone**: Pass at least one certification exam

---

## Month 6: Building a GitHub Portfolio

### Custom Security Tools Development
- **Tool Ideas**:
  - Network reconnaissance scanner
  - Web vulnerability scanner
  - Password strength analyzer
  - AI prompt injection tester
  - Custom exploit framework

### Portfolio Best Practices
- Clean, well-documented code
- README files with installation and usage instructions
- Contributing guidelines
- License information
- Demo videos or screenshots

### Open Source Contributions
- Contribute to security tools (Metasploit, Burp Suite extensions, etc.)
- Report vulnerabilities responsibly
- Write security blog posts and write-ups

### Professional Development
- Create a personal website/portfolio
- Write technical blog posts
- Participate in bug bounty programs
- Network on LinkedIn and Twitter/X

**Final Milestone**: Publish 3+ security tools on GitHub with 100+ stars combined

---

## Trending Skills to Master
{chr(10).join([f"- {skill}" for skill in skills[:10]])}

## Recommended Certifications
{chr(10).join([f"- {cert}" for cert in certs[:8]])}

---

*This roadmap is a guide. Adjust based on your learning pace and career goals. Consistency and hands-on practice are key to success in offensive security.*
"""
    else:
        # Generic roadmap for other domains
        roadmap = f"""# 6-Month {domain} Learning Roadmap

## Month 1-2: Foundation & Fundamentals
- Core concepts and fundamentals for {domain}
- Essential tools and technologies
- Hands-on practice and labs

## Month 3-4: Intermediate Skills & Specialization
- Domain-specific advanced topics
- Practical applications
- Real-world scenarios

## Month 5: Certifications & Professional Development
- Relevant certification preparation
- Study plans and resources
- Professional networking

## Month 6: Portfolio & Career Readiness
- Building a professional portfolio
- Practical projects
- Career preparation

## Trending Skills
{chr(10).join([f"- {skill}" for skill in skills[:10]])}

## Recommended Certifications
{chr(10).join([f"- {cert}" for cert in certs[:8]])}
"""
    
    return roadmap
