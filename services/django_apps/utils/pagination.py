# Standard Library
import os
from collections import OrderedDict

# Django
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomPagination(LimitOffsetPagination):

    default_limit = int(os.getenv("DEFAULT_LIMIT_PAGINATE", "3"))

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("results", data),
                    (
                        "links",
                        {
                            "next": self.get_next_link(),
                            "previous": self.get_previous_link(),
                        },
                    ),
                ]
            )
        )
