from setuptools import setup, find_packages
import sys

PY2 = sys.version_info[0] == 2
PY26 = PY2 and sys.version_info[1] < 7

NAME = "sphinx-sdg"
AUTHOR = "Travis"
VERSION = "0.0.1"
EMAIL = "travis.collins@analog.com"
LICENSE = "GNU Public License V3"
DESCRIPTION = "SDG sphinx extension" + ""
URL = "https://github.com/tfcollins/sphinx-sdg"
DOWNLOAD_URL = "%s/archive/%s.tar.gz" % (URL, VERSION)
FILES = ["README.rst", "CHANGELOG.rst"]
KEYWORDS = ["python", "sphinx", "excel"]

CLASSIFIERS = [
    "Topic :: Utilities",
    "Topic :: Software Development :: Libraries",
    "Programming Language :: Python",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "License :: OSI Approved :: Apache Software License",
]

INSTALL_REQUIRES = [
    "docutils",
    "sphinx",
    "jinja2",
]


PACKAGES = find_packages(exclude=["ez_setup", "examples", "tests"])
EXTRAS_REQUIRE = {}


def read_files(*files):
    """Read files into setup"""
    text = ""
    for single_file in files:
        content = read(single_file)
        text = text + content + "\n"
    return text


def read(afile):
    """Read a file into setup"""
    with open(afile, "r") as opened_file:
        content = filter_out_test_code(opened_file)
        content = "".join(list(content))
        return content


def filter_out_test_code(file_handle):
    found_test_code = False
    for line in file_handle.readlines():
        if line.startswith(".. testcode:"):
            found_test_code = True
            continue
        if found_test_code is True:
            if line.startswith("  "):
                continue
            else:
                empty_line = line.strip()
                if len(empty_line) == 0:
                    continue
                else:
                    found_test_code = False
                    yield line
        else:
            for keyword in ["|version|", "|today|"]:
                if keyword in line:
                    break
            else:
                yield line


if __name__ == "__main__":
    setup(
        name=NAME,
        author=AUTHOR,
        version=VERSION,
        author_email=EMAIL,
        description=DESCRIPTION,
        url=URL,
        download_url=DOWNLOAD_URL,
        long_description=read_files(*FILES),
        license=LICENSE,
        keywords=KEYWORDS,
        extras_require=EXTRAS_REQUIRE,
        tests_require=["pytest"],
        install_requires=INSTALL_REQUIRES,
        packages=PACKAGES,
        include_package_data=True,
        zip_safe=False,
        classifiers=CLASSIFIERS,
    )
