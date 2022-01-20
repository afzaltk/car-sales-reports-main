"""
Entry point to revenue report generator application
"""

import os
import sys

from reports.conversion_report import generate_conversion_report


def main(project_dir):
    generate_conversion_report(project_dir)


if __name__ == '__main__':
    # TODO:
    #  To integrate the following
    #       Command line arguments to pass input and output location.
    #       Util class to read and write files from different sources such as cloud storage, hdfs etc..
    #       Parameterize all the hardcoded values
    #       Exception handling.
    #       Unit test case.
    #       Config files.
    #       Customize output file formats.

    print("[info] - Job has started")
    project_directory = os.path.dirname(sys.path[0])
    main(project_directory)
    print("[info] - Job has finished")
