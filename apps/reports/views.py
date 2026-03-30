from django.http import HttpResponse, FileResponse
from django.shortcuts import get_object_or_404
from django.views import View
from io import BytesIO
from .models.report_card import ReportCard
from .services.pdf_service import PDFService

class DownloadReportCardView(View):
    def get(self, request, pk):
        report_card = get_object_or_404(ReportCard, pk=pk)
        pdf_content = PDFService.generate_report_card(report_card.student, report_card.term)
        
        if pdf_content:
            response = HttpResponse(pdf_content, content_type='application/pdf')
            filename = f"Report_Card_{report_card.student.full_name}_{report_card.term.name}.pdf".replace(" ", "_")
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
        
        return HttpResponse("Error generating PDF", status=500)
