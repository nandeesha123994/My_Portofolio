from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from Base.models import Contact, Project
from Base.forms import ContactForm 
# Create your views here.


def contact(request):
    recruiter_mode = request.session.get('recruiter_mode', False)
    
    if recruiter_mode:
        projects = Project.objects.filter(title__in=["Digital Bus Pass", "My Portfolio"])
        # Fallback
        if not projects.exists():
             projects = Project.objects.all()[:2]
    else:
        projects = Project.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for reaching out! Your message has been sent successfully. I’ll get back to you soon.")
            return render(request, 'home.html', {'form': ContactForm(), 'projects': projects, 'recruiter_mode': recruiter_mode}) 
        else:
            for field, errors in form.errors.items():
                for error in errors:
                     messages.error(request, f"{field}: {error}")
            return render(request, 'home.html', {'form': form, 'projects': projects, 'recruiter_mode': recruiter_mode})
            
    return render(request, 'home.html', {'form': ContactForm(), 'projects': projects, 'recruiter_mode': recruiter_mode})

def toggle_recruiter_mode(request):
    request.session['recruiter_mode'] = not request.session.get('recruiter_mode', False)
    return redirect('contact')

def project_case_study(request, slug):
    project = get_object_or_404(Project, slug=slug)
    tech_tags = [tech.strip() for tech in project.tech_used.split(',')] if project.tech_used else []
    return render(request, 'project_detail.html', {'project': project, 'tech_tags': tech_tags})



      


