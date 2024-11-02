from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponse
from .models import Business1,Freelancer, UserProfile ,Project ,ProposedProject ,AssignedProject
from .forms import UserRegistrationForm, UserProfileForm, ProjectForm , DescriptionForm
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password']) 
            user.save()
            profile.user = user
            profile.username = user.username
            profile.save()
            if profile.role == 'freelancer':
                group = Group.objects.get(name='freelancer')
            else:
                group = Group.objects.get(name='business')
            user.groups.add(group)
           
            return redirect('loginpage')  # Replace with your home URL
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    return render(request, 'home/register.html', {'user_form': user_form, 'profile_form': profile_form})
    

 


def home(request):
    context = { }
    if request.user.is_authenticated:
        context['user_name']=request.user.username
    else:
        context['user_name']= "Null"

    print(context)
    return  render(request,'home/index.html',context)



def logininto(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('homepage')  # Replace with your home URL
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'home/login.html')


# @login_required
def setup_freelancer(request):
    
    if request.method == 'POST':

        name = request.POST['name']
        age = request.POST['age']
        city = request.POST['city']
        country = request.POST['country']
        mobile = request.POST['mobile']
        email = request.POST['email']
        github = request.POST.get('github', '')
        cv_file = request.FILES['cv_file']

        Freelancer.objects.create(
            user_name = request.user.username,
            user=request.user,
            name=name, age=age, city=city,
            country=country, mobile=mobile,
            email=email, github_id=github,
            cv_file=cv_file
        )
        messages.success(request, "Freelancer account setup successfully.")
        # return redirect('profile', username=request.user.username)
        return redirect('homepage')

    return render(request, 'home/setupfreelancer.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('loginpage')



def business(request):
    businesses = Business1.objects.all()
    context ={
        'businesses' : businesses
    }
    return render(request,'home/business.html',context)

def project(request):
    x=request.user.id
    userx= UserProfile.objects.get(user_id=x)
    tits=userx.user_id
    projects = Project.objects.all()
    context = {'user': userx }
    context['projects']=projects
    if userx.role == 'freelancer':
        freelancer = get_object_or_404(Freelancer, user_id=x)  # Get the freelancer object
        
        applied_project_ids = ProposedProject.objects.filter(freelancer=freelancer).values_list('project_id', flat=True)
          # Get IDs o
        context['applied_project_ids']=applied_project_ids
        
    
    return render(request, 'home/project.html', context )

def create_project(request):
    x=request.user.id
    business = Business1.objects.get(user_id = x)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        
        print("hi")
        
        if form.is_valid():
            form2 =form.save(commit = False) 
            form2.business_id=business.id
            form2.save()
             # Save the form data to the Project model
            return redirect('homepage')  # Redirect to a list page after saving
    else:
        form = ProjectForm()
    
    return render(request, 'home/addproject.html', {'form': form})

def setup_corporate(request):
    if request.method == 'POST':

        company_name = request.POST['company_name']
        businesstype = request.POST['businesstype']
        hq_location = request.POST['hq_location']

        email = request.POST['email']
        website = request.POST.get('website', '')

        Business1.objects.create(
            user_name = request.user.username,
            user=request.user,
            company_name=company_name,
            businesstype=businesstype,
            headquarters=hq_location,
            email=email, website_link=website
        )
        messages.success(request, "Corporate account setup successfully.")
        return redirect('homepage')

    return render(request, 'home/setup_corporate.html')


@login_required
def profile(request , user_name):
    user_id =request.user.id
    
    userx= UserProfile.objects.get(username=user_name)
     
    context = {'user': userx }
    context['realuser']=request.user.username
    total_assigned_projects= AssignedProject.objects.all()
    context['total_assigned_projects']=total_assigned_projects
    context['In progress']="In progress"
   
    if userx.role == 'freelancer':
        freelancer = Freelancer.objects.get(user_name=user_name)
        applied_project_ids = ProposedProject.objects.filter(freelancer=freelancer, approved=False).values_list('project_id', flat=True)
        offered_project_ids = ProposedProject.objects.filter(approved=True, freelancer=freelancer).values_list('project_id', flat=True)
        
        projects = Project.objects.all()
        context['applied_project_ids']=applied_project_ids
        context['projects']=projects
        context['freelancer2']=freelancer
        context['offered_projects']=offered_project_ids 
                
        
    elif userx.role == 'business':
        business = Business1.objects.get(user_name=user_name)
        project = Project.objects.filter(business=business)
        offered_project_ids = ProposedProject.objects.filter(approved=True).values_list('project_id', flat=True)
        context['business'] = business
        context['projects'] =project
        context['offered_projects']=offered_project_ids

    print(context)
    return render(request, 'home/profile.html', context)




@login_required
def apply_to_project(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        project = get_object_or_404(Project, pk=project_id)
        freelancer = Freelancer.objects.get(user_id=request.user.id)
        
        form = DescriptionForm(request.POST)
        if form.is_valid():
            ProposedProject.objects.create(
                project=project,
                freelancer=freelancer,
                proposal_description=form.cleaned_data['proposal_description']
            )
            return redirect(reverse('profile',kwargs={'user_name' : request.user.username }))  # Redirect after successful proposal submission

    return redirect('projects')  # Redirect to projects if not POST or form is invalid

def myprojectsinfo(request, project_id):
    project =get_object_or_404(Project, pk=project_id)
    applied_freelancer_ids = ProposedProject.objects.filter(project=project).values_list('freelancer_id', flat=True)
    freelancer=Freelancer.objects.all()
    context ={ 
        'project' : project,
        'req_ids' : applied_freelancer_ids,
        'total_ids' : freelancer,
        'project_id' : project_id
    }
    xn =Freelancer.objects.get(id=applied_freelancer_ids[0])
    print(xn.name)
    return render(request , 'home/proposals.html',context)

    
def offer(request,project_id,freelancer_id):

    project =get_object_or_404(Project, pk=project_id)
    applied_freelancer = ProposedProject.objects.get(project_id=project_id,freelancer_id=freelancer_id)
    applied_freelancer.approved=True
    applied_freelancer.save()
    return redirect(reverse('profile',kwargs={'user_name' : request.user.username}))

def accept(request, project_id):
    # Retrieve the proposed project
    proposal = get_object_or_404(Project, id=project_id)
    # freelancer = Freelancer.objects.get(user_name=request.user.username)
    # Create a new assigned project based on the accepted proposal details
    assigned_project = AssignedProject.objects.create(
        business=proposal.business,
        title=proposal.title,
        category=proposal.category,
        description=proposal.description,
        timeline=proposal.timeline,  # Assumes Project model has a timeline field
        stipend=proposal.stipend,
        # freelancer=freelancer,
        freelancer_id=1,
    )
    
    proposal.delete()
    return redirect(reverse('profile',kwargs={'user_name' : request.user.username}))

def complete(request, project_id):
    project=get_object_or_404(AssignedProject, id=project_id)
    project.Inprogress=False
    project.completed_at = timezone.now()
    project.save()
    return redirect(reverse('profile',kwargs={'user_name' : request.user.username}))

