from setuptools import setup, find_packages

try:
    import multiprocessing, logging
except Exception:
    pass

setup(
    name='tw2.excanvas',
    version='2.0.2',
    description='toscawidgets2 wrapper for excanvas.js resource',
    long_description='',
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    license='MIT',
    url='http://github.com/toscawidgets/tw2.excanvas',
    install_requires=[
        "tw2.core>=2.0b2",
        ],
    tests_require = ['nose', 'BeautifulSoup', 'genshi'],
    packages=['tw2', 'tw2.excanvas'],
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
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
