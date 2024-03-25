#!/usr/bin/env python
import pytest

# Run tests using pytest-cov
pytest.main(["-v", "--cov=app", "--cov-report=term-missing", "tests"])
