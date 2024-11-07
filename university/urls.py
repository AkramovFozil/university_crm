from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Faculties
    path('faculties/', views.faculty_list, name='faculties'),
    path('faculty/form/', views.faculty_add, name='faculty_add'),
    path('faculty/update/<int:pk>/', views.faculty_add, name='faculty_update'),

    # Groups
    path('groups/', views.group_list, name='groups'),
    path('group/form/', views.group_add, name='group_add'),
    path('group/update/<int:pk>/', views.group_add, name='group_update'),

    # Departments
    path('departments/', views.department_list, name='departments'),
    path('department/form/', views.department_add, name='department_add'),
    path('department/update/<int:pk>/', views.department_add, name='department_update'),

    # Students
    path('students/', views.student_list, name='students'),
    path('student/form/', views.student_add, name='student_add'),
    path('student/update/<int:pk>/', views.student_add, name='student_update'),

    # Subjects
    path('subjects/', views.subject_list, name='subjects'),
    path('subject/form/', views.subject_add, name='subject_add'),
    path('subject/update/<int:pk>/', views.subject_add, name='subject_update'),

    # Teachers
    path('teachers/', views.teacher_list, name='teachers'),
    path('teacher/form/', views.teacher_add, name='teacher_add'),
    path('teacher/update/<int:pk>/', views.teacher_add, name='teacher_update'),

    # Delete operations
    path('delete/faculty/<int:pk>/', views.del_faculty, name='del_faculty'),
    path('delete/group/<int:pk>/', views.del_group, name='del_group'),
    path('delete/department/<int:pk>/', views.del_department, name='del_department'),
    path('delete/student/<int:pk>/', views.del_student, name='del_student'),
    path('delete/subject/<int:pk>/', views.del_subject, name='del_subject'),
    path('delete/teacher/<int:pk>/', views.del_teacher, name='del_teacher'),
]
