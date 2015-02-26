Django Extra Sensitive Variables
================================
``extra_sensitive_variables`` is a third-party exception filter for Django. This allows you to
globally censor a set of default variable names in Django's error reports regardless of a function's
lack of ``@sensitive_*`` decorators. Basically, any variable matching the names provided in
``settings.EXTRA_SENSITIVE_VARIABLES`` or ``settings.EXTRA_SENSITIVE_POST_PARAMETERS`` will be censored.

Installation
------------
1. Install the package via pip ::

    pip install django-extra-sensitive-variables

2. Tell Django to use the *Extra Sensitive Variable* filter by overriding ``DEFAULT_EXCEPTION_REPORTER_FILTER``
   in your ``settings.py`` ::

    DEFAULT_EXCEPTION_REPORTER_FILTER = 'extra_sensitive_variables.ExtraSensitiveReporterFilter'

3. Then add the following variables to your ``settings.py`` and modify them as you see fit ::

    # Variable names to always censor from "local vars" output
    EXTRA_SENSITIVE_VARIABLES = ['password', 'credentials']

    # Censor anything from the POST QueryDict matching these names
    EXTRA_SENSITIVE_POST_PARAMETERS = ['password', 'credentials', 'credit_card_number']
