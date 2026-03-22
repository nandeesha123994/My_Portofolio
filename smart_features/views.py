from django.shortcuts import render
from .forms import ResumeForm, ChatForm, RecommenderForm

# --- 1. Resume Analyzer Logic ---
REQUIRED_SKILLS = {
    'python', 'django', 'sql', 'html', 'css', 'javascript', 
    'react', 'aws', 'docker', 'git', 'rest api'
}

def analyze_resume(text):
    text_lower = text.lower()
    found_skills = {skill for skill in REQUIRED_SKILLS if skill in text_lower}
    missing_skills = REQUIRED_SKILLS - found_skills
    score = int((len(found_skills) / len(REQUIRED_SKILLS)) * 100)
    
    return {
        'score': score,
        'found': sorted(list(found_skills)),
        'missing': sorted(list(missing_skills)),
        'suggestion': "Great start! Try adding more projects." if score > 50 else "Consider learning more core technologies."
    }

# --- 2. Chatbot Logic ---
FAQ_DATA = {
    'who are you': "I am Nandeesha M, a passionate Python Full Stack Developer.",
    'projects': "I have worked on a Digital Bus Pass System, a Portfolio, and several mini-apps.",
    'tech': "I specialize in Python, Django, MySQL, HTML, CSS, and JavaScript.",
    'work': "Yes! I am currently open to new opportunities. Feel free to contact me.",
    'contact': "You can reach me via the 'Let's Talk' button on the home page."
}

def get_chat_response(query):
    query = query.lower()
    # Simple keyword matching
    for key, answer in FAQ_DATA.items():
        if key in query:
            return answer
    return "I'm meant to answer questions about my professional background. Try asking about my projects or skills!"

# --- 3. Project Recommender Logic ---
PROJECT_MAP = {
    'python': ['Digital Bus Pass', 'Logic Demo', 'Automation Scripts'],
    'django': ['Digital Bus Pass', 'Portfolio Website', 'Task Manager'],
    'sql': ['Digital Bus Pass', 'Inventory System', 'User Auth Module'],
    'javascript': ['Interactive Skills', 'Form Validation', 'Dynamic UI'],
    'html': ['Portfolio V1', 'Landing Page', 'Email Templates'],
    'react': ['Task Dashboard', 'Weather App']
}

def recommend_projects(skill):
    return PROJECT_MAP.get(skill, [])

# --- Main View ---
def smart_home(request):
    # Initialize Context
    context = {
        'resume_form': ResumeForm(prefix='resume'),
        'chat_form': ChatForm(prefix='chat'),
        'rec_form': RecommenderForm(prefix='rec'),
        'active_tab': 'resume' # Default tab
    }

    if request.method == 'POST':
        # 1. Handle Resume Submission
        if 'resume_submit' in request.POST:
            resume_form = ResumeForm(request.POST, prefix='resume')
            if resume_form.is_valid():
                text = resume_form.cleaned_data['resume_text']
                context['resume_result'] = analyze_resume(text)
                context['resume_form'] = resume_form # Retain data
                context['active_tab'] = 'resume'
        
        # 2. Handle Chat Submission
        elif 'chat_submit' in request.POST:
            chat_form = ChatForm(request.POST, prefix='chat')
            if chat_form.is_valid():
                query = chat_form.cleaned_data['query']
                context['chat_response'] = get_chat_response(query)
                context['chat_form'] = chat_form
                context['active_tab'] = 'chat'

        # 3. Handle Recommender Submission
        elif 'rec_submit' in request.POST:
            rec_form = RecommenderForm(request.POST, prefix='rec')
            if rec_form.is_valid():
                skill = rec_form.cleaned_data['skill']
                context['rec_projects'] = recommend_projects(skill)
                context['rec_skill'] = skill
                context['rec_form'] = rec_form
                context['active_tab'] = 'recommender'

    return render(request, 'smart_features/index.html', context)
