from django.shortcuts import render
import google.generativeai as genai
import os
from dotenv import load_dotenv
# Create your views here.
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")
def home(request):
    timetable=""
    if request.method == "POST":
        wake_time=request.POST.get('wake_time')
        college_time = request.POST.get('college_time')
        subjects=request.POST.get('subjects')
        study_hours= request.POST.get('study_hours')
        prompt= f"""
        You are an expert AI Study Planner.

        Create a clean and productive daily timetable in TABLE FORMAT.

        Student Details:
        - Wake Time: {wake_time} AM
        - College Time: {college_time} AM
        - Subjects: {subjects}
        - Study Hours: {study_hours}

        Rules:
        1. Divide study sessions smartly.
        2. Include short breaks.
        3. Add revision sessions.
        4. Add motivation tips at the end.
        5. Balance coding and theory subjects.
        6. Make the schedule realistic and productive.
        7. Use proper time slots.

I       IMPORTANT:
        Return the output in clean HTML table format.

        Example:

        <table border="1">
        <tr>
        <th>Time</th>
        <th>Task</th>
        </tr>

        <tr>
        <td>6:00 AM</td>
        <td>Wake Up</td>
        </tr>

        </table>

        Do NOT return markdown.
        Only return HTML table.
        """
        try:
            response = model.generate_content(prompt)
            timetable = response.text
        except Exception as e:
            timetable = str(e)
    return render(request,'home.html',{'timetable':timetable})
