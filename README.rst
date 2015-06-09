Log django request data for the diagnostic purposes
---------------------------------------------------

All requests matching filter functions will be logged
in the database.

The following data is logged::
* user (if authenticated)
* IP address
* request path (url)
* request method
* request parameters
* session key
* session snapshot
* request META dictionary
* COOKIES dictionary

Filters are functions defined via settings parameter
`REQUEST_LOGGING_FILTERS`. For example::

    from myapp.request_logging_filters import post_from_some_ips

    REQUEST_LOGGING_FILTERS = (
        'myapp.request_logging_filters.authenticated_posts',
        posts_from_some_ips
    )

Filters may be defined either as a callable function or
as a python dotted path to such function.
Filter functions must take `request` instance as argument
and return either `True` or `False`, when the request
matches the filter or not, correspondingly.

.. note::
    Keep in mind that `request_logging` will store data
    in the database which will take storage space and
    computing resources. In production use sparingly,
    for diagnostinc purposes.

Configuration settings
======================

The following `settings.py` entries are available::
* `REQUEST_LOGGING_FILTERS` - a tuple of filter functions or dotted paths.
* `REQUEST_LOGGING_HIDE_PARAMETERS` - a tuple of parameter names that will be hidden
   (e.g. `('password', 'credit_card_number')`)
