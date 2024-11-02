# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Freelancer ,Business1 ,Project,ProposedProject

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role']

class FreelancerForm(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = ['user_name','name', 'age', 'city', 'country', 'mobile', 'email', 'github_id', 'cv_file']



class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business1
        fields = [
            'user_name',
            'businesstype', 'company_name', 'businesstype' , 'headquarters', 
            'email', 'website_link'
        ]
       



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [ 'title', 'category', 'description', 'timeline', 'stipend']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the project here...'}),
            'timeline': forms.NumberInput(attrs={'step': 0.01, 'placeholder': 'e.g., 30.5 days'}),
            'stipend': forms.NumberInput(attrs={'step': 0.01, 'placeholder': 'e.g., 1000.00'}),
        }

class DescriptionForm(forms.ModelForm):
    class Meta:
        model=ProposedProject
        fields =['proposal_description']
        widgets = {
            'proposal_description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your proposal'})
        }
