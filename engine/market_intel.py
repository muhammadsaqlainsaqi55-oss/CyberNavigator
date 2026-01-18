"""
Market Intelligence Module
Fetches trending skills and certifications for cyber security domains.
Simulates scraping job boards and threat intelligence feeds for 2026 trends.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from typing import Dict, List


def _simulate_scraping(domain: str) -> Dict[str, List[str]]:
    """
    Simulates scraping job boards and threat intelligence feeds.
    Returns domain-specific market trends for 2026.
    
    Args:
        domain: The cyber security domain (Red Team, Blue Team, AppSec, GRC, Cloud Security)
    
    Returns:
        Dictionary with 'trending_skills' and 'certifications' lists
    """
    # Simulate making HTTP requests to job boards and threat intel feeds
    # In a production environment, this would scrape actual sites like:
    # - LinkedIn Jobs, Indeed, CyberSeek
    # - Threat intelligence feeds
    # - Certification provider websites
    
    # Simulate network delay
    time.sleep(0.1)
    
    # In real implementation, would do:
    # try:
    #     headers = {'User-Agent': 'Mozilla/5.0...'}
    #     response = requests.get(f"https://job-board.com/cybersecurity/{domain.lower()}", 
    #                             headers=headers, timeout=10)
    #     soup = BeautifulSoup(response.content, 'html.parser')
    #     # Extract skills and certifications from parsed HTML
    #     skills = [skill.text for skill in soup.find_all('div', class_='skill-item')]
    #     certs = [cert.text for cert in soup.find_all('span', class_='certification')]
    # except Exception as e:
    #     # Fallback to curated data
    #     pass
    
    # Domain-specific market intelligence data for 2026
    market_data = {
        "Red Team": {
            "trending_skills": [
                "AI-driven social engineering",
                "EDR evasion techniques",
                "Autonomous SOC bypass",
                "Cloud infrastructure penetration testing",
                "API security exploitation",
                "Container escape techniques",
                "Zero-day discovery and exploitation",
                "Advanced persistent threat (APT) simulation",
                "AI/ML model adversarial attacks",
                "Supply chain attack vectors"
            ],
            "certifications": [
                "CompTIA Security+ (SY0-701)",
                "CEH AI (Certified Ethical Hacker - AI Edition)",
                "OSCP (Offensive Security Certified Professional)",
                "OSEP (Offensive Security Experienced Penetration Tester)",
                "GPEN (GIAC Penetration Tester)",
                "GXPN (GIAC Exploit Researcher and Advanced Penetration Tester)",
                "CRTP (Certified Red Team Professional)",
                "CRTE (Certified Red Team Expert)"
            ]
        },
        "Blue Team": {
            "trending_skills": [
                "AI-powered threat detection",
                "SOAR (Security Orchestration, Automation, and Response)",
                "Extended Detection and Response (XDR)",
                "Zero Trust architecture implementation",
                "Threat hunting with ML models",
                "Cloud security monitoring",
                "Container security operations",
                "Incident response automation",
                "Behavioral analytics",
                "Security information and event management (SIEM) optimization"
            ],
            "certifications": [
                "CompTIA Security+ (SY0-701)",
                "GCIH (GIAC Certified Incident Handler)",
                "GSEC (GIAC Security Essentials)",
                "GCFA (GIAC Certified Forensic Analyst)",
                "SANS SEC503 (Intrusion Detection In-Depth)",
                "CISSP (Certified Information Systems Security Professional)",
                "CySA+ (CompTIA Cybersecurity Analyst)",
                "SSCP (Systems Security Certified Practitioner)"
            ]
        },
        "AppSec": {
            "trending_skills": [
                "Secure coding practices (OWASP Top 10 2026)",
                "API security testing and hardening",
                "DevSecOps pipeline integration",
                "Container and Kubernetes security",
                "AI/ML application security",
                "Software composition analysis (SCA)",
                "Static and dynamic application security testing (SAST/DAST)",
                "Infrastructure as Code (IaC) security",
                "Mobile application security",
                "Serverless security architecture"
            ],
            "certifications": [
                "CompTIA Security+ (SY0-701)",
                "GWEB (GIAC Web Application Penetration Tester)",
                "GMOB (GIAC Mobile Device Security Analyst)",
                "CSSLP (Certified Secure Software Lifecycle Professional)",
                "CEH AI (Certified Ethical Hacker - AI Edition)",
                "OWASP certifications",
                "SANS SEC542 (Web App Penetration Testing)",
                "CASS (Certified Application Security Specialist)"
            ]
        },
        "GRC": {
            "trending_skills": [
                "AI governance and compliance",
                "Zero Trust compliance frameworks",
                "Cloud compliance (SOC 2, ISO 27001, FedRAMP)",
                "Privacy regulations (GDPR, CCPA, emerging 2026 standards)",
                "Risk quantification and modeling",
                "Third-party risk management",
                "Security audit automation",
                "Regulatory technology (RegTech)",
                "ESG (Environmental, Social, Governance) security compliance",
                "Quantum computing risk assessment"
            ],
            "certifications": [
                "CompTIA Security+ (SY0-701)",
                "CISSP (Certified Information Systems Security Professional)",
                "CISM (Certified Information Security Manager)",
                "CISA (Certified Information Systems Auditor)",
                "CRISC (Certified in Risk and Information Systems Control)",
                "CGEIT (Certified in the Governance of Enterprise IT)",
                "ISO 27001 Lead Auditor",
                "GRCP (Governance, Risk, and Compliance Professional)"
            ]
        },
        "Cloud Security": {
            "trending_skills": [
                "Multi-cloud security architecture",
                "Cloud-native security (Kubernetes, containers)",
                "Serverless security",
                "Cloud security posture management (CSPM)",
                "Identity and access management (IAM) for cloud",
                "Cloud workload protection",
                "Infrastructure as Code (IaC) security scanning",
                "Cloud data loss prevention (DLP)",
                "Zero Trust cloud implementation",
                "AI/ML cloud security monitoring"
            ],
            "certifications": [
                "CompTIA Security+ (SY0-701)",
                "AWS Certified Security - Specialty",
                "Microsoft Certified: Azure Security Engineer Associate",
                "Google Cloud Professional Cloud Security Engineer",
                "CCSP (Certified Cloud Security Professional)",
                "CISSP (Certified Information Systems Security Professional)",
                "SANS GCSA (GIAC Cloud Security Automation)",
                "Cloud Security Alliance (CSA) certifications"
            ]
        }
    }
    
    # Return data for the specified domain, or default if domain not found
    return market_data.get(domain, {
        "trending_skills": ["General cybersecurity skills", "Threat analysis", "Security fundamentals"],
        "certifications": ["CompTIA Security+ (SY0-701)", "CISSP", "General security certifications"]
    })


def fetch_market_trends(domain: str) -> Dict[str, pd.DataFrame]:
    """
    Fetches market trends and certifications for a given cyber security domain.
    Simulates scraping job boards and threat intelligence feeds for 2026 data.
    
    Args:
        domain: The cyber security domain (Red Team, Blue Team, AppSec, GRC, Cloud Security)
    
    Returns:
        Dictionary containing:
            - 'trending_skills': pandas DataFrame with trending skills
            - 'certifications': pandas DataFrame with top certifications
    
    Example:
        >>> trends = fetch_market_trends("Red Team")
        >>> print(trends['trending_skills'])
        >>> print(trends['certifications'])
    """
    # Simulate scraping process
    try:
        # Simulate making a request (in real implementation, this would scrape actual sites)
        # For demonstration, we'll use mock data
        response_data = _simulate_scraping(domain)
        
        # Create DataFrames for clean display in Streamlit
        trending_skills_df = pd.DataFrame({
            'Rank': range(1, len(response_data['trending_skills']) + 1),
            'Trending Skill': response_data['trending_skills'],
            'Category': '2026 Market Trend'
        })
        
        certifications_df = pd.DataFrame({
            'Rank': range(1, len(response_data['certifications']) + 1),
            'Certification': response_data['certifications'],
            'Year': '2026 Standard'
        })
        
        return {
            'trending_skills': trending_skills_df,
            'certifications': certifications_df
        }
    
    except Exception as e:
        # Fallback in case of errors
        return {
            'trending_skills': pd.DataFrame({
                'Rank': [1, 2, 3],
                'Trending Skill': ['General Security Skills', 'Threat Analysis', 'Security Fundamentals'],
                'Category': ['2026 Market Trend'] * 3
            }),
            'certifications': pd.DataFrame({
                'Rank': [1, 2, 3],
                'Certification': ['CompTIA Security+ (SY0-701)', 'CISSP', 'General Security Certifications'],
                'Year': ['2026 Standard'] * 3
            })
        }
