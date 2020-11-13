import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-rest-framework-social-oauth2-rebirth-ashdaily',
    version="0.0.1",
    author="Ashish Singh Bardhan",
    author_email="ashtokyo31@gmail.com",
    description="Useful tools for daily python/django hustles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ashdaily/django-rest-framework-social-oauth2-rebirth',
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'djangorestframework>=3.10.3',
        'django-oauth-toolkit>=0.12.0',
        'social-auth-app-django>=3.1.0',
    ],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.6',
)