"""
Career DNA Quiz - Cyber Security Domain Assessment
Maps quiz responses to cyber security career domains.
"""

# Quiz questions dictionary for display in app.py
QUIZ_QUESTIONS = {
    1: {
        "question": "How do you feel about writing code?",
        "options": {
            "A": "I love coding and want to build tools/automation",
            "B": "I'm comfortable with code but prefer analyzing it",
            "C": "I can read code but prefer higher-level concepts",
            "D": "I avoid coding when possible"
        }
    },
    2: {
        "question": "What interests you more about software?",
        "options": {
            "A": "Building secure applications from scratch",
            "B": "Finding vulnerabilities in existing code",
            "C": "Understanding how applications work at a high level",
            "D": "Ensuring applications meet compliance standards"
        }
    },
    3: {
        "question": "How do you feel about rules, regulations, and compliance?",
        "options": {
            "A": "They're necessary but I prefer hands-on technical work",
            "B": "I find them interesting and important for security",
            "C": "I'm passionate about ensuring organizations follow them",
            "D": "I understand them but prefer technical implementation"
        }
    },
    4: {
        "question": "When you see a security policy, what's your first thought?",
        "options": {
            "A": "How can I test if this is actually being enforced?",
            "B": "How can I implement technical controls to support this?",
            "C": "This needs to align with industry standards and regulations",
            "D": "I need to understand the technical implications"
        }
    },
    5: {
        "question": "What excites you more?",
        "options": {
            "A": "Finding creative ways systems can be broken",
            "B": "Building defenses to prevent attacks",
            "C": "Understanding attack patterns to improve security",
            "D": "Ensuring systems meet security standards"
        }
    },
    6: {
        "question": "When you encounter a new system, what's your first instinct?",
        "options": {
            "A": "I wonder how I could exploit it",
            "B": "I think about how to secure it",
            "C": "I analyze its architecture and potential weaknesses",
            "D": "I check if it meets compliance requirements"
        }
    },
    7: {
        "question": "What's your preferred work environment?",
        "options": {
            "A": "Simulating attacks in controlled environments",
            "B": "Building and maintaining security infrastructure",
            "C": "Reviewing code and application security",
            "D": "Auditing and ensuring regulatory compliance"
        }
    },
    8: {
        "question": "How do you prefer to learn about security?",
        "options": {
            "A": "By trying to break things in a lab",
            "B": "By building and configuring security tools",
            "C": "By studying code and application architectures",
            "D": "By studying frameworks and compliance standards"
        }
    },
    9: {
        "question": "What's your ideal project?",
        "options": {
            "A": "Penetration testing a new application",
            "B": "Designing a network security architecture",
            "C": "Conducting a security code review",
            "D": "Performing a compliance audit"
        }
    },
    10: {
        "question": "When a security incident occurs, what role do you want?",
        "options": {
            "A": "Simulating the attack to understand it better",
            "B": "Responding and containing the threat",
            "C": "Analyzing the application vulnerabilities that led to it",
            "D": "Reviewing if policies and controls were adequate"
        }
    }
}

# Scoring matrix: maps question number -> answer option -> category scores
# Categories: Red Team, Blue Team, AppSec, GRC, Cloud Security
SCORING_MATRIX = {
    1: {  # Coding interest
        "A": {"Red Team": 2, "Blue Team": 3, "AppSec": 5, "GRC": 0, "Cloud Security": 4},
        "B": {"Red Team": 4, "Blue Team": 4, "AppSec": 4, "GRC": 1, "Cloud Security": 3},
        "C": {"Red Team": 3, "Blue Team": 3, "AppSec": 2, "GRC": 3, "Cloud Security": 2},
        "D": {"Red Team": 1, "Blue Team": 2, "AppSec": 0, "GRC": 5, "Cloud Security": 1}
    },
    2: {  # Software interest
        "A": {"Red Team": 1, "Blue Team": 2, "AppSec": 5, "GRC": 1, "Cloud Security": 4},
        "B": {"Red Team": 5, "Blue Team": 2, "AppSec": 4, "GRC": 1, "Cloud Security": 2},
        "C": {"Red Team": 2, "Blue Team": 3, "AppSec": 2, "GRC": 3, "Cloud Security": 3},
        "D": {"Red Team": 0, "Blue Team": 1, "AppSec": 1, "GRC": 5, "Cloud Security": 1}
    },
    3: {  # Rules/regulations interest
        "A": {"Red Team": 4, "Blue Team": 3, "AppSec": 3, "GRC": 1, "Cloud Security": 2},
        "B": {"Red Team": 2, "Blue Team": 4, "AppSec": 2, "GRC": 3, "Cloud Security": 3},
        "C": {"Red Team": 0, "Blue Team": 1, "AppSec": 1, "GRC": 5, "Cloud Security": 1},
        "D": {"Red Team": 3, "Blue Team": 3, "AppSec": 4, "GRC": 2, "Cloud Security": 4}
    },
    4: {  # Security policy perspective
        "A": {"Red Team": 5, "Blue Team": 2, "AppSec": 2, "GRC": 1, "Cloud Security": 2},
        "B": {"Red Team": 1, "Blue Team": 5, "AppSec": 3, "GRC": 2, "Cloud Security": 4},
        "C": {"Red Team": 0, "Blue Team": 1, "AppSec": 1, "GRC": 5, "Cloud Security": 1},
        "D": {"Red Team": 2, "Blue Team": 3, "AppSec": 4, "GRC": 3, "Cloud Security": 3}
    },
    5: {  # Excitement preference
        "A": {"Red Team": 5, "Blue Team": 1, "AppSec": 3, "GRC": 0, "Cloud Security": 2},
        "B": {"Red Team": 1, "Blue Team": 5, "AppSec": 2, "GRC": 2, "Cloud Security": 4},
        "C": {"Red Team": 3, "Blue Team": 3, "AppSec": 4, "GRC": 2, "Cloud Security": 3},
        "D": {"Red Team": 0, "Blue Team": 2, "AppSec": 1, "GRC": 5, "Cloud Security": 1}
    },
    6: {  # System encounter instinct
        "A": {"Red Team": 5, "Blue Team": 1, "AppSec": 3, "GRC": 0, "Cloud Security": 2},
        "B": {"Red Team": 1, "Blue Team": 5, "AppSec": 2, "GRC": 2, "Cloud Security": 4},
        "C": {"Red Team": 3, "Blue Team": 3, "AppSec": 4, "GRC": 2, "Cloud Security": 3},
        "D": {"Red Team": 0, "Blue Team": 2, "AppSec": 1, "GRC": 5, "Cloud Security": 1}
    },
    7: {  # Preferred work environment
        "A": {"Red Team": 5, "Blue Team": 2, "AppSec": 3, "GRC": 0, "Cloud Security": 1},
        "B": {"Red Team": 1, "Blue Team": 5, "AppSec": 1, "GRC": 1, "Cloud Security": 4},
        "C": {"Red Team": 2, "Blue Team": 2, "AppSec": 5, "GRC": 1, "Cloud Security": 2},
        "D": {"Red Team": 0, "Blue Team": 1, "AppSec": 1, "GRC": 5, "Cloud Security": 1}
    },
    8: {  # Learning preference
        "A": {"Red Team": 5, "Blue Team": 2, "AppSec": 3, "GRC": 0, "Cloud Security": 2},
        "B": {"Red Team": 1, "Blue Team": 5, "AppSec": 1, "GRC": 1, "Cloud Security": 4},
        "C": {"Red Team": 2, "Blue Team": 2, "AppSec": 5, "GRC": 1, "Cloud Security": 2},
        "D": {"Red Team": 0, "Blue Team": 1, "AppSec": 1, "GRC": 5, "Cloud Security": 1}
    },
    9: {  # Ideal project
        "A": {"Red Team": 5, "Blue Team": 1, "AppSec": 2, "GRC": 0, "Cloud Security": 1},
        "B": {"Red Team": 1, "Blue Team": 5, "AppSec": 1, "GRC": 1, "Cloud Security": 4},
        "C": {"Red Team": 2, "Blue Team": 2, "AppSec": 5, "GRC": 1, "Cloud Security": 2},
        "D": {"Red Team": 0, "Blue Team": 1, "AppSec": 1, "GRC": 5, "Cloud Security": 1}
    },
    10: {  # Incident response role preference
        "A": {"Red Team": 5, "Blue Team": 1, "AppSec": 2, "GRC": 0, "Cloud Security": 1},
        "B": {"Red Team": 1, "Blue Team": 5, "AppSec": 1, "GRC": 1, "Cloud Security": 3},
        "C": {"Red Team": 2, "Blue Team": 2, "AppSec": 5, "GRC": 1, "Cloud Security": 2},
        "D": {"Red Team": 0, "Blue Team": 1, "AppSec": 1, "GRC": 5, "Cloud Security": 1}
    }
}

# Category display names
CATEGORY_NAMES = {
    "Red Team": "Red Team (Offensive)",
    "Blue Team": "Blue Team (Defensive)",
    "AppSec": "Application Security",
    "GRC": "GRC (Governance, Risk & Compliance)",
    "Cloud Security": "Cloud Security"
}


def get_cyber_domain(responses):
    """
    Analyzes quiz responses and returns the most suitable cyber security domain.
    
    Args:
        responses (list): List of 10 answer choices (A, B, C, or D) corresponding to questions 1-10.
                         Can be uppercase or lowercase.
    
    Returns:
        dict: A dictionary containing:
            - 'domain': The primary recommended domain (str)
            - 'full_name': Full display name of the domain (str)
            - 'scores': Dictionary of all category scores (dict)
            - 'confidence': Confidence percentage based on score difference (float)
    
    Raises:
        ValueError: If responses list doesn't have exactly 10 answers or contains invalid choices.
    """
    # Validate input
    if len(responses) != 10:
        raise ValueError(f"Expected 10 responses, got {len(responses)}")
    
    # Initialize scores for all categories
    scores = {
        "Red Team": 0,
        "Blue Team": 0,
        "AppSec": 0,
        "GRC": 0,
        "Cloud Security": 0
    }
    
    # Process each response
    for question_num, answer in enumerate(responses, start=1):
        # Normalize answer to uppercase
        answer = answer.upper().strip()
        
        # Validate answer choice
        if answer not in ["A", "B", "C", "D"]:
            raise ValueError(f"Invalid answer '{answer}' for question {question_num}. Must be A, B, C, or D.")
        
        # Get scores for this answer
        if question_num in SCORING_MATRIX and answer in SCORING_MATRIX[question_num]:
            answer_scores = SCORING_MATRIX[question_num][answer]
            for category, points in answer_scores.items():
                scores[category] += points
    
    # Find the domain with the highest score
    max_score = max(scores.values())
    primary_domain = max(scores, key=scores.get)
    
    # Calculate confidence based on score difference
    # Get second highest score
    sorted_scores = sorted(scores.values(), reverse=True)
    if len(sorted_scores) > 1:
        score_difference = sorted_scores[0] - sorted_scores[1]
        max_possible_difference = 50  # Rough estimate based on max possible scores
        confidence = min(100, 50 + (score_difference / max_possible_difference * 50))
    else:
        confidence = 100.0
    
    return {
        "domain": primary_domain,
        "full_name": CATEGORY_NAMES[primary_domain],
        "scores": scores,
        "confidence": round(confidence, 1)
    }
