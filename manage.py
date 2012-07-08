from django.core.management import execute_manager

try:
    from settings import active as settings
except ImportError:
    try:
        from settings import settings
    except ImportError:
        import sys
        sys.stderr.write("Error: Can't find the file 'settings.py'")
        sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
