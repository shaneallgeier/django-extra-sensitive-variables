from django.conf import settings
from django.views.debug import SafeExceptionReporterFilter, CLEANSED_SUBSTITUTE


class ExtraSensitiveReporterFilter(SafeExceptionReporterFilter):

    def get_post_parameters(self, *args, **kwargs):
        cleansed = super(ExtraSensitiveReporterFilter, self).get_post_parameters(*args, **kwargs)
        for param in settings.EXTRA_SENSITIVE_POST_PARAMETERS:
            if param in cleansed:
                cleansed[param] = CLEANSED_SUBSTITUTE
        return cleansed

    def get_traceback_frame_variables(self, *args, **kwargs):
        cleansed = dict(super(ExtraSensitiveReporterFilter, self).get_traceback_frame_variables(*args, **kwargs))
        for param in settings.EXTRA_SENSITIVE_VARIABLES:
            if param in cleansed:
                cleansed[param] = CLEANSED_SUBSTITUTE
        return cleansed.items()
