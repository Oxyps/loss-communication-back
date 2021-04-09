from rest_framework import pagination
from rest_framework.response import Response

class Pagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'page'

    def get_previous_page(self):
        if not self.page.has_previous():
            return None
        return self.page.previous_page_number()

    def get_next_page(self):
        if not self.page.has_next():
            return None
        return self.page.next_page_number()

    def get_paginated_response(self, data):
        return Response({
            'previous_page': self.get_previous_page(),
            'next_page': self.get_next_page(),
            'page_size': self.page_size,
            'data_length': self.page.paginator.count,
            'data': data
        })
