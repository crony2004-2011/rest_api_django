from rest_framework.pagination import PageNumberPagination


class MyPageNmberPagination(PageNumberPagination):
    page_size = 5  # developer defines no of data
    page_query_param = 'page'  # directs directly to page number
    # user can define how much data he/she wants to see on one page
    page_size_query_params = 'records'
