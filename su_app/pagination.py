from rest_framework.response import Response

from rest_framework import pagination
# from rest_framework.compat import OrderedDict


class YookorePagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'page': {
            	'size': self.page_size,
                'totalElements': self.page.paginator.count,
                'totalPages': self.page.paginator.num_pages,
                'number':self.page.number,
            },
            'count': self.page.paginator.count,
            'list': data
        })


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):

        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'page': {
            	'size': self.page_size,
                'totalElements': self.page.paginator.count,
                'totalPages': self.page.paginator.num_pages,
                'number':self.page.number,
            },
            'list': data
        })
