import sys
"""
This module contains utility functions that are used by the main module
"""

def exit_gracefully(signum, frame):
    print()
    print("Exiting gracefully")
    sys.exit(0)