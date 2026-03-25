from apps.notifications.services.sms_service import send_sms
from apps.students.models import Guardian

def process_grade_notification(grade):
    """
    Business logic to notify parent/guardian when a grade is recorded.
    """
    student = grade.student
    subject = grade.subject
    guardians = Guardian.objects.filter(student=student)

    message = f"{student.full_name} scored {grade.score} in {subject.name}"

    for guardian in guardians:
        if guardian.phone:
            send_sms(student.school, guardian.phone, message)
