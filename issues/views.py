from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Reporter, Issue, CriticalIssue, LowPriorityIssue
import json,os
# Create your views here.

BASE_DIR = os.path.dirname(__file__)
REPORTERS_FILE = os.path.join(BASE_DIR, 'reporters.json')
ISSUES_FILE = os.path.join(BASE_DIR, 'issues.json')

def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)
def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


@csrf_exempt
def reporters(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            reporter = Reporter(
                data["id"],
                data["name"],
                data["email"],
                data["team"]
            )
            reporter.validate()
            reporters_list = load_data(REPORTERS_FILE)
            reporters_list.append(reporter.to_dict())
            save_data(REPORTERS_FILE, reporters_list)
            return JsonResponse(
                reporter.to_dict(),
                status=201
            )
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
    elif request.method == 'GET':
        reporters_list = load_data(REPORTERS_FILE)
        reporter_id = request.GET.get('id')
        if reporter_id:
            for reporter in reporters_list:
                if reporter["id"] == int(reporter_id):
                    return JsonResponse(reporter, safe=False)
            return JsonResponse({"error": "Reporter not found"}, status=404)
        return JsonResponse(reporters_list, safe=False)

@csrf_exempt
def issues(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if data["priority"] == "critical":
                issue = CriticalIssue(
                    data["id"],
                    data["title"],
                    data["description"],
                    data["status"],
                    data["priority"],
                    data["reporter_id"]
                )
            elif data["priority"] == "low":
                issue = LowPriorityIssue(
                    data["id"],
                    data["title"],
                    data["description"],
                    data["status"],
                    data["priority"],
                    data["reporter_id"]
                )
            else:
                issue = Issue(
                    data["id"],
                    data["title"],
                    data["description"],
                    data["status"],
                    data["priority"],
                    data["reporter_id"]
                )
            issue.validate()
            issues_list = load_data(ISSUES_FILE)
            issues_list.append(issue.to_dict())
            save_data(ISSUES_FILE, issues_list)
            response_data = issue.to_dict()
            response_data["message"] = issue.describe()  # Add the description to the response
            return JsonResponse(
                response_data,
                status=201
            )
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
    elif request.method == 'GET':
        issues_list = load_data(ISSUES_FILE)
        issue_id = request.GET.get('id')
        if issue_id:
            for issue in issues_list:
                if issue["id"] == int(issue_id):
                    return JsonResponse(issue, safe=False)
            return JsonResponse({"error": "Issue not found"}, status=404)
        # Filtering by status
        status = request.GET.get('status')
        if status:
            filtered_issues = []
            for issue in issues_list:
                if issue["status"] == status:
                    filtered_issues.append(issue)
            return JsonResponse(filtered_issues, safe=False)
        return JsonResponse(issues_list, safe=False)

















#errror- something crfs - 
# add try catch after dinner
        