from django import forms

class ResumeForm(forms.Form):
    resume_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': 'Paste your resume text here...',
            'rows': 6
        }),
        label="Paste Resume Text"
    )

class ChatForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Ask me anything (e.g., "Who are you?")'
        }),
        label="Ask a Question"
    )

SKILL_CHOICES = [
    ('python', 'Python'),
    ('django', 'Django'),
    ('sql', 'SQL'),
    ('html', 'HTML/CSS'),
    ('javascript', 'JavaScript'),
    ('react', 'React'),
]

class RecommenderForm(forms.Form):
    skill = forms.ChoiceField(
        choices=SKILL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Select a Skill"
    )
