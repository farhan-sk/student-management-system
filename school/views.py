from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Notification
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, "authentication/login.html")

def dashboard(request):
    unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    unread_notification_count = unread_notification.count()
    return render(request, "students/student-dashboard.html")



def mark_notification_as_read(request):
    if request.method == 'POST':
        notification = Notification.objects.filter(user=request.user, is_read=False)
        notification.update(is_read=True)
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

def clear_all_notification(request):
    if request.method == "POST":
        notification = Notification.objects.filter(user=request.user)
        notification.delete()
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

def admin_dashboard(request):
    return render(request, "Home/index.html")   # admin dashboard

def teacher_dashboard(request):
    return render(request, "Home/teacher-dashboard.html")   # teacher dashboard

def student_dashboard(request):
    return render(request, "students/student-dashboard.html")  # student dashboard


# AI FEATURE 
def ai_assistant(request):

    msg = request.GET.get("message", "").lower()

    # 👉 Simple Language Detection
    hindi_words = ["kya", "kaise", "hai", "karna", "student", "marks", "attendance"]
    hindi_detected = any(word in msg for word in hindi_words)

    # ======================
    # STUDENT DOUBTS
    # ======================
    if "attendance" in msg:
        if hindi_detected:
            reply = "Attendance Students menu me available hai."
        else:
            reply = "Attendance is available inside the Students menu."

    elif "marks" in msg or "result" in msg:
        if hindi_detected:
            reply = "Student dashboard me performance section check kare."
        else:
            reply = "Check the performance section in the student dashboard."

    # ======================
    # TEACHER HELP
    # ======================
    elif "add student" in msg:
        if hindi_detected:
            reply = "Students -> Add Student se new student add kar sakte ho."
        else:
            reply = "You can add a new student from Students → Add Student."

    elif "timetable" in msg:
        if hindi_detected:
            reply = "Timetable Teachers section me manage hota hai."
        else:
            reply = "Timetable is managed inside the Teachers section."

    # ======================
    # ADMIN QUERIES
    # ======================
    elif "fees" in msg:
        if hindi_detected:
            reply = "Fees module Accounts section me available hai."
        else:
            reply = "Fees module is available in the Accounts section."

    elif "exam" in msg:
        if hindi_detected:
            reply = "Exam list dashboard sidebar me milegi."
        else:
            reply = "Exam list is available in the dashboard sidebar."

    else:
        if hindi_detected:
            reply = "Sorry, mujhe samajh nahi aaya."
        else:
            reply = "Sorry, I didn't understand your question."

    return JsonResponse({"reply": reply})


def ai_chat_page(request):
    return render(request,"Home/ai_chat.html")