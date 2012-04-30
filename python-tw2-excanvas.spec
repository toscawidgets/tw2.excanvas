%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global modname tw2.excanvas

Name:           python-tw2-excanvas
Version:        2.0.0
Release:        2%{?dist}
Summary:        Excanvas for ToscaWidgets2

Group:          Development/Languages
License:        MIT
URL:            http://toscawidgets.org
Source0:        http://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

# For building
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-tw2-core

# For tests
BuildRequires:  python-nose
BuildRequires:  python-BeautifulSoup
BuildRequires:  python-genshi

# Runtime requirements
Requires:       python-tw2-core

%description
Simple excanvas resource wrapper for ToscaWidgets2.

%prep
%setup -q -n %{modname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build \
    --install-data=%{_datadir} --root %{buildroot}

%check
PYTHONPATH=$(pwd) python setup.py test

%files
%doc README.rst
%{python_sitelib}/*

%changelog
* Mon Apr 30 2012 Ralph Bean <rbean@redhat.com> - 2.0.0-2
- Removed clean section
- Removed defattr in files section
- Removed unnecessary references to buildroot

* Wed Apr 11 2012 Ralph Bean <rbean@redhat.com> - 2.0.0-1
- Initial packaging for Fedora
