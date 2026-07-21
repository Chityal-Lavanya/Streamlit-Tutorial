import streamlit as st

# Title
st.title("Student Result Management Dashboard")

# Header
st.header("Student Information")
student = {
    "Name": "Lavanya Chityal",
    "Roll No": 101,
    "Department": "Computer Science",
    "Semester": 5
}
st.write(student)

# Subheader
st.subheader(" Subject Marks")
marks = {
    "Python": 90,
    "Java": 85,
    "Database": 88,
    "Operating System": 80,
    "Computer Network": 92
}
st.write(marks)

# Percentage Calculation
total = sum(marks.values())
percentage = total / len(marks)
st.subheader(" Result Summary")
st.write("Total Marks :", total)
st.write("Percentage :", round(percentage, 2), "%")

# Grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "Fail"
st.write("Grade :", grade)

# Plain Text
st.text("Result generated successfully.")

# Markdown
st.header("Performance Report")
st.markdown("""
### Achievements
-  Excellent Performance
-  Good Attendance
-  Active in Practical Sessions
**Congratulations on your excellent academic performance!**
""")

# Caption
st.caption("Academic Year : 2026-27")

# Code Example
st.header(" Percentage Calculation Code")
code = '''
marks = [90,85,88,80,92]
percentage = sum(marks) / len(marks)
print(percentage)
'''
st.code(code, language="python")

# Latex
st.header(" Percentage Formula")
st.latex(r'''
Percentage=\frac{Total\ Marks}{Number\ of\ Subjects}
''')

# Horizonal Line
st.markdown("---")

# Footer
st.markdown("###  Important Notice")
st.markdown("""
- Carry your ID card during examinations.
- Check the timetable regularly.
- Contact your class teacher for any corrections.
""")

st.write("🎉 Thank you for using Student Result Management Dashboard!")