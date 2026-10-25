"""Views for displaying and working with learning resources."""
from django.shortcuts import get_object_or_404, render

from .models import StudyResource


def resource_list(request):
    resources = StudyResource.objects.all().order_by("title")

    # TODO (Engineering Challenge): filter resources by the submitted subject.
    subject = request.GET.get("subject", "")

    return render(
        request,
        "resources/resource_list.html",
        {"resources": resources, "subject": subject},
    )


def resource_detail(request, pk):
    resource = get_object_or_404(StudyResource, pk=pk)
    return render(
        request,
        "resources/resource_detail.html",
        {"resource": resource},
    )


def add_resource(request):
    # TODO (Implementation Lab): connect StudyResourceForm to GET and POST requests.
    return render(request, "resources/resource_form.html")


def delete_resource(request, pk):
    resource = get_object_or_404(StudyResource, pk=pk)
    # TODO (Engineering Challenge): implement deletion only after a valid POST.
    return render(
        request,
        "resources/resource_confirm_delete.html",
        {"resource": resource, "feature_incomplete": request.method == "POST"},
    )
