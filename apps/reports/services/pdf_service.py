from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.db.models import Sum, Avg
from apps.academics.models import Grade

class PDFService:
    @staticmethod
    def generate_report_card(student, term):
        """
        Generates a PDF report card for a student and term.
        """
        template = get_template('reports/report_card.html')
        
        # Get all grades for this student and term
        grades = Grade.objects.filter(student=student, term=term).select_related('subject')
        
        # Calculate summary statistics
        total_score = grades.aggregate(Sum('score'))['score__sum'] or 0
        average_score = grades.aggregate(Avg('score'))['score__avg'] or 0
        subject_count = grades.count()
        
        context = {
            'student': student,
            'term': term,
            'grades': grades,
            'total_score': total_score,
            'average_score': round(average_score, 2),
            'subject_count': subject_count,
            'school': student.school,
        }
        
        html = template.render(context)
        result = BytesIO()
        
        # Create PDF
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
        
        if not pdf.err:
            return result.getvalue()
        return None
