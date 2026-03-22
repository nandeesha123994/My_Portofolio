from django.shortcuts import render
from .forms import LogicForm, PasswordForm, BusPassForm
import math
import re

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def calculate_factorial(n):
    if n < 0: return "Undefined for negative numbers"
    if n > 20: return "Too large to display"
    return math.factorial(n)

def check_password_strength(password):
    strength = "Weak"
    messages = []
    
    length = len(password) >= 8
    upper = bool(re.search(r"[A-Z]", password))
    lower = bool(re.search(r"[a-z]", password))
    digit = bool(re.search(r"\d", password))
    special = bool(re.search(r"[!@#$%^&*]", password))
    
    score = sum([length, upper, lower, digit, special])
    
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
        
    if not length: messages.append("Minimum 8 chars")
    if not upper: messages.append("Add uppercase")
    if not lower: messages.append("Add lowercase")
    if not digit: messages.append("Add number")
    if not special: messages.append("Add special char")
    
    return strength, messages

# Dummy Data for Bus Pass
BUS_PASS_DB = {
    "BUS101": {"status": "Active", "route": "City Center - Campus", "valid_until": "2025-12-31"},
    "BUS102": {"status": "Expired", "route": "North Station - Mall", "valid_until": "2024-01-01"},
}

def miniapps_home(request):
    logic_result = None
    pass_result = None
    bus_result = None
    
    logic_form = LogicForm(prefix='logic')
    pass_form = PasswordForm(prefix='pass')
    bus_form = BusPassForm(prefix='bus')

    if request.method == "POST":
        if 'logic_submit' in request.POST:
            logic_form = LogicForm(request.POST, prefix='logic')
            if logic_form.is_valid():
                num = logic_form.cleaned_data['number']
                logic_result = {
                    "number": num,
                    "is_prime": is_prime(num),
                    "is_palindrome": is_palindrome(num),
                    "factorial": calculate_factorial(num)
                }
        
        elif 'pass_submit' in request.POST:
            pass_form = PasswordForm(request.POST, prefix='pass')
            if pass_form.is_valid():
                pwd = pass_form.cleaned_data['password']
                strength, msgs = check_password_strength(pwd)
                pass_result = {"strength": strength, "messages": msgs}

        elif 'bus_submit' in request.POST:
            bus_form = BusPassForm(request.POST, prefix='bus')
            if bus_form.is_valid():
                pid = bus_form.cleaned_data['pass_id']
                data = BUS_PASS_DB.get(pid)
                if data:
                    bus_result = data
                    bus_result['id'] = pid
                else:
                    bus_result = {"status": "Not Found", "message": f"Pass ID {pid} not found."}

    context = {
        'logic_form': logic_form,
        'logic_result': logic_result,
        'pass_form': pass_form,
        'pass_result': pass_result,
        'bus_form': bus_form,
        'bus_result': bus_result,
    }
    return render(request, 'miniapps/index.html', context)
