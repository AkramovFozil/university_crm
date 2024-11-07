from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FacultyForm, GroupForm, DepartmentForm, StudentForm, SubjectForm, TeacherForm
from .models import Faculty, Group, Department, Student, Subject, Teacher

def dashboard(request):
    faculties = Faculty.objects.all()
    groups = Group.objects.all()
    departments = Department.objects.all()
    students = Student.objects.all()
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()

    return render(request, 'dashboard.html',
                  {
                      'faculties': faculties, 'groups': groups, 'departments': departments,
                      'students': students, 'subjects': subjects, 'teachers': teachers
                  })

def faculty_add(request, pk=None):
    if pk:
        faculty = get_object_or_404(Faculty, pk=pk)
    else:
        faculty = None

    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculties')
        else:
            return HttpResponse("Form is invalid.")
    else:
        form = FacultyForm(instance=faculty)

    ctx = {'faculty': form, 'g404': faculty}
    return render(request, 'forms/faculty_form.html', ctx)

def group_add(request, pk=None):
    if pk:
        group = get_object_or_404(Group, pk=pk)
    else:
        group = None

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('groups')
        else:
            return HttpResponse('Form is invalid.')
    else:
        form = GroupForm(instance=group)

    ctx = {'group': form, 'g404': group}
    return render(request, 'forms/group_form.html', ctx)

def department_add(request, pk=None):
    if pk:
        department = get_object_or_404(Department, pk=pk)
    else:
        department = None

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('departments')
        else:
            return HttpResponse('Form is invalid.')
    else:
        form = DepartmentForm(instance=department)

    ctx = {'department': form, 'g404': department}
    return render(request, 'forms/department_form.html', ctx)

def student_add(request, pk=None):
    if pk:
        student = get_object_or_404(Student, pk=pk)
    else:
        student = None

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
        else:
            return HttpResponse("Form is invalid.")
    else:
        form = StudentForm(instance=student)

    ctx = {'student': form, 'g404': student}
    return render(request, 'forms/student_form.html', ctx)

def subject_add(request, pk=None):
    if pk:
        subject = get_object_or_404(Subject, pk=pk)
    else:
        subject = None

    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subjects')
        else:
            return HttpResponse("Form is invalid.")
    else:
        form = SubjectForm(instance=subject)

    ctx = {'subject': form, 'g404': subject}
    return render(request, 'forms/subject_form.html', ctx)

def teacher_add(request, pk=None):
    if pk:
        teacher = get_object_or_404(Teacher, pk=pk)
    else:
        teacher = None

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')
        else:
            return HttpResponse("Form is invalid.")
    else:
        form = TeacherForm(instance=teacher)

    ctx = {'teacher': form, 'g404': teacher}
    return render(request, 'forms/teacher_form.html', ctx)

def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'lists/faculty_list.html', {'faculties': faculties})

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'lists/group_list.html', {'groups': groups})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'lists/department_list.html', {'departments': departments})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'lists/student_list.html', {'students': students})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'lists/subject_list.html', {'subjects': subjects})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'lists/teacher_list.html', {'teachers': teachers})


def del_faculty(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        faculty.delete()
        return redirect('faculties')

    return render(request, 'confirms/confirm_faculty.html', {'faculty': faculty})


def del_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('groups')

    return render(request, 'confirms/confirm_group.html', {'group': group})


def del_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('departments')

    return render(request, 'confirms/confirm_department.html', {'department': department})


def del_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students')

    return render(request, 'confirms/confirm_student.html', {'student': student})


def del_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subjects')

    return render(request, 'confirms/confirm_subject.html', {'subject': subject})


def del_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers')

    return render(request, 'confirms/confirm_teacher.html', {'teacher': teacher})
