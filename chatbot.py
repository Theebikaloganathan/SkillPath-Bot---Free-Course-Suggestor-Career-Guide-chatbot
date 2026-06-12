import time
import random

# KNOWLEDGE BASE - Dictionary (O(1) lookup, not if-elif ladder)

KNOWLEDGE_BASE = {

    # GREETINGS & META
    "hello": "greet",
    "hi": "greet",
    "hey": "greet",
    "good morning": "greet",
    "good evening": "greet",
    "help": "help_menu",
    "menu": "help_menu",
    "what can you do": "help_menu",
    "who are you": "about",
    "about": "about",
    "bye": "exit_chat",
    "exit": "exit_chat",
    "quit": "exit_chat",

    # CAREER PATH EXPLORATION
    "i want to learn ai": "path_ai",
    "ai": "path_ai",
    "artificial intelligence": "path_ai",
    "machine learning": "path_ml",
    "ml": "path_ml",
    "deep learning": "path_dl",
    "data science": "path_ds",
    "ds": "path_ds",
    "data analyst": "path_da",
    "software engineering": "path_se",
    "software developer": "path_se",
    "se": "path_se",
    "web development": "path_web",
    "web dev": "path_web",
    "frontend": "path_web",
    "backend": "path_web",
    "cybersecurity": "path_cyber",
    "cyber": "path_cyber",
    "ethical hacking": "path_cyber",
    "networking": "path_network",
    "network": "path_network",
    "cloud": "path_cloud",
    "devops": "path_devops",
    "it": "path_it",
    "information technology": "path_it",

    # WHERE TO START
    "where to start": "starter_guide",
    "i am a beginner": "starter_guide",
    "beginner": "starter_guide",
    "how to start": "starter_guide",
    "i dont know where to start": "starter_guide",
    "i don't know where to start": "starter_guide",
    "i am confused": "starter_guide",

    # CV / INTERNSHIP
    "cv": "cv_guide",
    "resume": "cv_guide",
    "how to build cv": "cv_guide",
    "internship": "internship_guide",
    "how to get internship": "internship_guide",
    "job": "internship_guide",

    # FREE PLATFORM GUIDES
    "free courses": "free_platforms",
    "platforms": "free_platforms",
    "coursera": "free_platforms",
    "google": "free_platforms",
    "youtube": "free_platforms",
    "kaggle": "path_ml",

    # PYTHON
    "python": "path_python",
    "learn python": "path_python",
}

# RESPONSE ENGINE - All detailed responses

RESPONSES = {

    "greet": lambda: """
Hey there! Welcome to SkillPath Bot
Your FREE Career & Course Guide

I help you find 100% FREE courses to build real skills,
improve your CV, and land internships.

Type 'menu' to see what I can guide you on!
""",

    "about": lambda: """
I am SkillPath Bot - a rule-based AI chatbot that guides you toward:
- FREE online courses
- Career roadmaps
- CV-building strategies
- Internship tips

Paths I cover: AI, ML, DS, SE, Web, Cyber, Network, Cloud, IT

Type 'menu' to explore!
""",

    "help_menu": lambda: """
SKILLPATH BOT - MAIN MENU

Type any of these to get started:

AI / Machine Learning / Deep Learning
Data Science / Data Analyst
Software Engineering / Web Dev
Cybersecurity / Ethical Hacking
Networking / Cloud / DevOps
IT / Information Technology
Python (foundation for all paths)

CV         - How to build a strong CV
Internship - How to land one
Beginner   - Don't know where to start?
Free Courses - Best free platforms

Type 'bye' to exit
""",

    "path_ai": lambda: """
AI ENGINEER ROADMAP

STEP 1 - Learn Python first (type 'python')
STEP 2 - Learn Math basics (Linear Algebra, Stats)
STEP 3 - Machine Learning fundamentals
STEP 4 - Deep Learning & Neural Networks
STEP 5 - Build real projects + GitHub portfolio

FREE COURSES:
- Google ML Crash Course (FREE)
  https://developers.google.com/machine-learning/crash-course

- fast.ai - Practical Deep Learning (FREE)
  https://www.fast.ai

- Andrew Ng - ML Specialization (Audit FREE)
  https://www.coursera.org/specializations/machine-learning-introduction

- CS50 AI - Harvard (FREE)
  https://cs50.harvard.edu/ai

- Kaggle Learn - AI/ML (FREE)
  https://www.kaggle.com/learn

CV SKILLS TO ADD: Python, TensorFlow, PyTorch,
Scikit-learn, NumPy, Pandas, Jupyter

Type 'ml' for Machine Learning details
Type 'dl' for Deep Learning details
""",

    "path_ml": lambda: """
MACHINE LEARNING ROADMAP

STEP 1 - Python + NumPy + Pandas
STEP 2 - Statistics & Probability basics
STEP 3 - Supervised & Unsupervised Learning
STEP 4 - Scikit-learn projects
STEP 5 - Kaggle competitions for practice

FREE COURSES:
- Kaggle ML Course (FREE, fastest way)
  https://www.kaggle.com/learn/intro-to-machine-learning

- StatQuest YouTube (FREE)
  https://www.youtube.com/@statquest

- Google ML Crash Course (FREE)
  https://developers.google.com/machine-learning/crash-course

- Scikit-learn Official Docs + Tutorials (FREE)
  https://scikit-learn.org/stable/tutorial

CV SKILLS: Scikit-learn, XGBoost, LightGBM,
Feature Engineering, Model Evaluation

Type 'data science' for the full DS path
""",

    "path_dl": lambda: """
DEEP LEARNING ROADMAP

STEP 1 - Strong Python + ML basics first
STEP 2 - Neural Networks fundamentals
STEP 3 - CNN (Images) / RNN (Sequences)
STEP 4 - PyTorch or TensorFlow
STEP 5 - Transformers & LLMs (advanced)

FREE COURSES:
- fast.ai - Practical Deep Learning (FREE)
  https://course.fast.ai

- Deep Learning Specialization - Andrew Ng (Audit FREE on Coursera)
  https://www.coursera.org/specializations/deep-learning

- MIT 6.S191 Deep Learning (FREE)
  http://introtodeeplearning.com

- PyTorch Tutorials Official (FREE)
  https://pytorch.org/tutorials

CV SKILLS: PyTorch, TensorFlow, Keras,
CNN, RNN, Transfer Learning, Transformers
""",

    "path_ds": lambda: """
DATA SCIENCE ROADMAP

STEP 1 - Python + Pandas + NumPy
STEP 2 - Data Visualization (Matplotlib, Seaborn)
STEP 3 - SQL for data querying
STEP 4 - Statistics & EDA (Exploratory Data Analysis)
STEP 5 - ML models + Deployment basics

FREE COURSES:
- IBM Data Science (Audit FREE - Coursera)
  https://www.coursera.org/professional-certificates/ibm-data-science

- Kaggle - Python, Pandas, Data Viz (FREE)
  https://www.kaggle.com/learn

- freeCodeCamp Data Analysis (FREE)
  https://www.freecodecamp.org/learn/data-analysis-with-python

- SQL for Data Science - UC Davis (Audit FREE)
  https://www.coursera.org/learn/sql-for-data-science

CV SKILLS: Python, SQL, Tableau/PowerBI,
Pandas, NumPy, Matplotlib, Seaborn, EDA
""",

    "path_da": lambda: """
DATA ANALYST ROADMAP

STEP 1 - Excel / Google Sheets basics
STEP 2 - SQL (most important skill!)
STEP 3 - Python or R for analysis
STEP 4 - Tableau or Power BI (visualization)
STEP 5 - Build 3 portfolio projects

FREE COURSES:
- Google Data Analytics (Audit FREE)
  https://www.coursera.org/professional-certificates/google-data-analytics

- SQLZoo - Interactive SQL (FREE)
  https://sqlzoo.net

- Tableau Public Training (FREE)
  https://www.tableau.com/learn/training

- W3Schools SQL (FREE)
  https://www.w3schools.com/sql

CV SKILLS: SQL, Excel, Python, Tableau,
Power BI, Data Cleaning, Dashboard Design
""",

    "path_se": lambda: """
SOFTWARE ENGINEERING ROADMAP

STEP 1 - Pick a language: Python / Java / C++
STEP 2 - Data Structures & Algorithms (DSA)
STEP 3 - OOP Principles
STEP 4 - Git & GitHub (essential!)
STEP 5 - Build projects + open source contributions

FREE COURSES:
- CS50x - Harvard (FREE, best intro ever)
  https://cs50.harvard.edu/x

- The Odin Project (FREE, full SE path)
  https://www.theodinproject.com

- MIT OCW 6.0001 Python (FREE)
  https://ocw.mit.edu/courses/6-0001

- LeetCode DSA Practice (FREE tier)
  https://leetcode.com

- Git & GitHub - freeCodeCamp (FREE)
  https://www.freecodecamp.org

CV SKILLS: Java/Python/C++, Git, GitHub,
DSA, OOP, REST APIs, Docker basics
""",

    "path_web": lambda: """
WEB DEVELOPMENT ROADMAP

STEP 1 - HTML + CSS (structure & styling)
STEP 2 - JavaScript (make it interactive)
STEP 3 - React or Vue (Frontend framework)
STEP 4 - Node.js or Python/Flask (Backend)
STEP 5 - Deploy a live project (Vercel/Netlify FREE)

FREE COURSES:
- freeCodeCamp Web Dev (FREE, full path)
  https://www.freecodecamp.org

- The Odin Project (FREE, project-based)
  https://www.theodinproject.com

- CS50 Web - Harvard (FREE)
  https://cs50.harvard.edu/web

- MDN Web Docs (FREE reference)
  https://developer.mozilla.org

CV SKILLS: HTML, CSS, JavaScript, React,
Node.js, REST API, Git, Responsive Design
""",

    "path_cyber": lambda: """
CYBERSECURITY ROADMAP

STEP 1 - Networking basics (type 'networking')
STEP 2 - Linux fundamentals
STEP 3 - Security fundamentals (CIA Triad, threats)
STEP 4 - Ethical Hacking tools (Kali Linux, Nmap)
STEP 5 - CTF challenges (practice hacking legally!)

FREE COURSES:
- TryHackMe - Beginner paths (FREE tier)
  https://tryhackme.com

- Cybrary - Security Fundamentals (FREE)
  https://www.cybrary.it

- Google Cybersecurity Cert (Audit FREE)
  https://www.coursera.org/professional-certificates/google-cybersecurity

- Hack The Box Academy (FREE tier)
  https://academy.hackthebox.com

- OverTheWire - CTF Wargames (FREE)
  https://overthewire.org

CV SKILLS: Linux, Kali, Wireshark, Nmap,
OWASP, Network Security, CTF Experience
CERT TO TARGET: CompTIA Security+
""",

    "path_network": lambda: """
NETWORKING ROADMAP

STEP 1 - OSI Model & TCP/IP
STEP 2 - IP addressing, Subnetting, DNS, DHCP
STEP 3 - Cisco Packet Tracer (free lab simulator)
STEP 4 - Network security basics
STEP 5 - Target CCNA certification

FREE COURSES:
- Cisco Networking Basics (FREE)
  https://skillsforall.com

- Professor Messer CompTIA Network+ (FREE)
  https://www.professormesser.com

- Packet Tracer Download (FREE from Cisco)
  https://skillsforall.com/course/getting-started-cisco-packet-tracer

- NetworkChuck YouTube (FREE)
  https://www.youtube.com/@NetworkChuck

CV SKILLS: TCP/IP, DNS, DHCP, Subnetting,
Wireshark, Cisco Packet Tracer, Firewalls
CERT TO TARGET: CCNA (career-defining)
""",

    "path_cloud": lambda: """
CLOUD COMPUTING ROADMAP

STEP 1 - Networking basics first
STEP 2 - Linux fundamentals
STEP 3 - Pick one cloud: AWS / GCP / Azure
STEP 4 - Infrastructure as Code (Terraform basics)
STEP 5 - Deploy real projects on cloud (free tiers!)

FREE COURSES:
- AWS Cloud Practitioner Essentials (FREE)
  https://explore.skillbuilder.aws

- Google Cloud Skills Boost (FREE tier)
  https://cloudskillsboost.google

- Microsoft Azure Fundamentals (FREE)
  https://learn.microsoft.com/azure

- freeCodeCamp Cloud Computing (YouTube FREE)
  https://www.youtube.com/@freecodecamp

CV SKILLS: AWS/GCP/Azure, Docker, Kubernetes,
Terraform, CI/CD, Linux, S3, EC2
""",

    "path_devops": lambda: """
DEVOPS ROADMAP

STEP 1 - Linux + Bash scripting
STEP 2 - Git & GitHub (version control)
STEP 3 - Docker (containerization)
STEP 4 - CI/CD pipelines (GitHub Actions FREE)
STEP 5 - Cloud + Kubernetes

FREE COURSES:
- TechWorld with Nana - DevOps (YouTube FREE)
  https://www.youtube.com/@TechWorldwithNana

- Docker Official Get Started (FREE)
  https://docs.docker.com/get-started

- GitHub Actions Docs (FREE)
  https://docs.github.com/actions

- Linux Foundation Free Courses (FREE)
  https://training.linuxfoundation.org

CV SKILLS: Docker, Kubernetes, GitHub Actions,
Linux, Bash, Terraform, Jenkins, AWS/GCP
""",

    "path_it": lambda: """
IT / INFORMATION TECHNOLOGY ROADMAP

STEP 1 - Computer Hardware & OS basics
STEP 2 - Networking fundamentals
STEP 3 - Linux + Windows administration
STEP 4 - IT Support & Troubleshooting
STEP 5 - Specialize (Cloud / Cyber / Network)

FREE COURSES:
- Google IT Support Cert (Audit FREE)
  https://www.coursera.org/professional-certificates/google-it-support

- Cisco Skills for All (FREE)
  https://skillsforall.com

- Professor Messer CompTIA A+ (FREE)
  https://www.professormesser.com

- Microsoft Learn IT Fundamentals (FREE)
  https://learn.microsoft.com

CV SKILLS: Networking, Linux, Windows Server,
Active Directory, Troubleshooting, Cloud basics
CERT TO TARGET: CompTIA A+ (entry-level gold)
""",

    "path_python": lambda: """
PYTHON - THE FOUNDATION OF EVERYTHING

Why Python first? It unlocks: AI, ML, DS,
Web Dev (Flask/Django), Automation, DevOps

STEP 1 - Variables, loops, functions
STEP 2 - Lists, dicts, OOP
STEP 3 - File handling + APIs
STEP 4 - Libraries: NumPy, Pandas, Requests
STEP 5 - Build 3 small projects

FREE COURSES:
- CS50P - Python by Harvard (FREE, best)
  https://cs50.harvard.edu/python

- Kaggle Python Course (FREE, 5hrs)
  https://www.kaggle.com/learn/python

- Python.org Official Tutorial (FREE)
  https://docs.python.org/3/tutorial

- Automate the Boring Stuff (FREE book+course)
  https://automatetheboringstuff.com

- freeCodeCamp Python (YouTube FREE, 4hrs)
  https://www.youtube.com/@freecodecamp

CV SKILLS: Python, OOP, NumPy, Pandas,
API calls, Scripting, Jupyter Notebooks
""",

    "starter_guide": lambda: """
BEGINNER? START HERE.

Don't know where to start? Everyone starts confused.
Here's the universal first step for ANY tech path:

WEEK 1-2  - Learn Python basics
           https://cs50.harvard.edu/python (FREE)

WEEK 3-4  - Pick your path:
           - AI/ML? type 'ai'
           - Web Dev? type 'web dev'
           - Cybersecurity? type 'cybersecurity'
           - Data Science? type 'data science'
           - Networking? type 'networking'

MONTH 2   - Do 1 project using what you learned
MONTH 3   - Put it on GitHub + update your CV

GOLDEN RULE: Learn > Build > Show
Don't spend months just watching tutorials.
Build something small after every 2 weeks.

Type your chosen path above to get the full roadmap!
""",

    "cv_guide": lambda: """
HOW TO BUILD A CV THAT GETS YOU HIRED

SECTIONS EVERY TECH CV NEEDS:
1. Name + GitHub link + LinkedIn + Email
2. Skills (languages, tools, frameworks)
3. Projects (2-3 real ones with GitHub links)
4. Education
5. Certifications (even free ones count!)
6. Internship/Experience (if any)

WHAT STANDS OUT:
- Real GitHub projects (not just coursework)
- Free certifications: Google, IBM, Kaggle, AWS
- Kaggle competitions (shows ML ability)
- Open source contributions
- Personal projects solving a real problem

FREE CV BUILDERS:
- Overleaf LaTeX CV Templates (FREE)
  https://www.overleaf.com/latex/templates

- Canva CV Templates (FREE)
  https://www.canva.com/resumes

- GitHub Profile README (FREE, impressive)
  https://github.com

TIP: 1 strong project > 10 listed courses.
Recruiters want proof, not just certificates.
""",

    "internship_guide": lambda: """
HOW TO LAND AN INTERNSHIP

STEP 1 - Build 2-3 GitHub projects in your field
STEP 2 - Get 1-2 free certifications
STEP 3 - Set up LinkedIn properly
STEP 4 - Apply on these platforms:

WHERE TO APPLY:
- LinkedIn Jobs   - linkedin.com/jobs
- Internshala     - internshala.com
- AngelList       - wellfound.com
- GitHub Jobs     - jobs.github.com
- Google          - careers.google.com
- MLH Fellowship  - fellowship.mlh.io

COLD OUTREACH WORKS:
Find an engineer on LinkedIn and message them:
"Hi, I'm learning [X], built [project].
Do you have any internship openings?"
50% of internships are never posted publicly.

MINIMUM TO APPLY:
- 1 GitHub project in the relevant field
- Basic skills in 1 language
- A clean 1-page CV
""",

    "free_platforms": lambda: """
BEST FREE LEARNING PLATFORMS

- CS50 (Harvard)        - cs50.harvard.edu
  Best: CS, Python, Web, AI, Cybersecurity

- Kaggle Learn          - kaggle.com/learn
  Best: Python, ML, DS, SQL, AI

- freeCodeCamp          - freecodecamp.org
  Best: Web Dev, Python, DS, ML

- Google Digital Garage - learndigital.withgoogle.com
  Best: AI, Data, Digital Marketing

- Microsoft Learn       - learn.microsoft.com
  Best: Azure, .NET, AI, DevOps

- IBM SkillsBuild       - skillsbuild.org
  Best: AI, Data Science, Cybersecurity

- fast.ai               - fast.ai
  Best: Deep Learning, practical ML

- The Odin Project      - theodinproject.com
  Best: Full-stack Web Development

TIP: Audit courses on Coursera = FREE content,
no certificate. Worth it for the knowledge!
""",

    "exit_chat": lambda: """
Great session! Remember:

- Pick ONE path and start today
- Learn > Build > Show on GitHub
- Every expert was once a beginner

Good luck on your journey!
- SkillPath Bot
""",
}

# FALLBACK RESPONSES - Rotates to feel less robotic

FALLBACKS = [
    "I didn't catch that. Type 'menu' to see what I can help with.",
    "Not sure about that one. Try typing a path like 'ai', 'cyber', or 'web dev'.",
    "I specialize in free courses & career guidance. Type 'menu' to explore!",
    "Hmm, I don't have that. Try: 'ai', 'data science', 'cybersecurity', 'networking', or 'beginner'",
]

# CORE ENGINE

def sanitize(raw: str) -> str:
    """Phase 1 - Input Sanitization (lowercase + strip whitespace)"""
    return raw.lower().strip()


def get_intent(clean_input: str) -> str:
    """Phase 2 - Intent Matching via Dictionary (O(1) lookup)"""
    return KNOWLEDGE_BASE.get(clean_input, None)


def generate_response(intent: str) -> str:
    """Phase 3 - Response Generation"""
    if intent is None:
        return random.choice(FALLBACKS)
    if intent == "exit_chat":
        return RESPONSES["exit_chat"]()
    response_fn = RESPONSES.get(intent)
    if response_fn:
        return response_fn()
    return random.choice(FALLBACKS)


# MAIN LOOP - The Heartbeat

def main():
    print("=" * 50)
    print("  SkillPath Bot | Free Course & Career Guide")
    print("  Type 'menu' to get started | 'bye' to exit")
    print("=" * 50)
    time.sleep(0.3)
    print(RESPONSES["greet"]())

    while True:
        try:
            raw = input("You: ")

            # Phase 1: Sanitize
            clean = sanitize(raw)

            # Empty input guard
            if not clean:
                print("Bot: Please type something. Try 'menu' to see options.\n")
                continue

            # Phase 2: Match intent
            intent = get_intent(clean)

            # Phase 3: Generate response
            reply = generate_response(intent)

            print(f"\nBot: {reply}")

            # Exit condition
            if intent == "exit_chat":
                break

        except KeyboardInterrupt:
            print("\n\nBot: Session interrupted. Goodbye!")
            break


if __name__ == "__main__":
    main()