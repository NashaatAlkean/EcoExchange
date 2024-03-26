from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Report
from .forms import ReportForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

from django.http import JsonResponse

@login_required
def report_issue(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('home')  # Redirect to home page after successful submission
    else:
        form = ReportForm()
    return render(request, 'reportsSection\\report_issue.html', {'form': form})

@login_required
def view_reports(request):
    if request.user.is_superuser:
        reports = Report.objects.all()
        return render(request, 'reportsSection\\view_reports.html', {'reports': reports})
    else:
        return redirect('home')  # Redirect non-superusers to home page
    


@login_required
@require_POST
def delete_report(request, report_id):
    if not request.user.is_superuser:
        return redirect('home')  # Redirect non-admin users
    
    report = Report.objects.get(id=report_id)
    report.delete()
    return redirect('view_reports')

@login_required
@require_POST
def resolve_report(request, report_id):
    if not request.user.is_superuser:
        return redirect('home')  # Redirect non-admin users
    
    report = Report.objects.get(id=report_id)
    report.resolved = not report.resolved  # Toggle the 'resolved' status
    report.save()

    if report.resolved:
        messages.success(request, f"Report '{report.title}' resolved successfully.")
    else:
        messages.info(request, f"Report '{report.title}' marked as unresolved.")

    return redirect('view_reports')  # Redirect back to view_reports page
