from setuptools import setup, find_packages

setup(
    name='tw2.excanvas',
    version='2.0a1',
    description='toscawidgets2 wrapper for excanvas.js resource',
    long_description='',
    author='Ralph Bean',
    author_email='ralph.bean@gmail.com',
    license='MIT',
    url='http://github.com/ralphbean/tw2.excanvas',
    install_requires=[
        "tw2.core>=2.0b2",
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.excanvas
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
