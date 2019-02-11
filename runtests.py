#!/usr/bin/env python
import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner
if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'stackable_plugins.tests.settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["stackable_plugins.tests"])
    sys.exit(bool(failures))