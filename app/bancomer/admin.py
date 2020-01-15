from django.contrib import admin
from .models import Transaction, Category, Summary
from django.db.models import Count, Sum
from rangefilter.filter import DateRangeFilter
from django.conf import settings


class AdminTrans(admin.ModelAdmin):
    date_hierarchy  = "applied"
    list_editable = ("category",)
    list_display = ("applied", "description", "amount", "category")
    list_filter = (
        ("category"),
        ('applied', DateRangeFilter),
    )


class AdminSummary(AdminTrans):

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data["cl"].queryset
        except (AttributeError, KeyError):
            return response

        qs= qs.exclude(category__name=settings.IGNORE_CATEGORY_NAME)
        metrics = {
            "total": Count("id"),
            "total_sales": Sum("amount"),
        }
        response.context_data.update({
        'summary':list(
            qs
            .values("category__name")
            .annotate(**metrics)
            .order_by("-total_sales")),
        'bigtotal': qs.aggregate(bigtotal=Sum("amount")),
        'ignore': settings.IGNORE_CATEGORY_NAME,
         })
        return response

#admin.site.register(Summary, AdminSummary)
admin.site.register(Transaction, AdminSummary)
admin.site.register(Category)
