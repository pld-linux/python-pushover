#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	pushover
Summary:	Bindings for the Pushover notification service
Name:		python-%{module}
Version:	0.4
Release:	7
License:	GPL v3+
Group:		Libraries/Python
Source0:	https://github.com/Thibauth/python-pushover/archive/v%{version}.tar.gz
# Source0-md5:	306c1fea53917263f854cd63b17c7fa0
URL:		https://github.com/Thibauth/python-pushover
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.713
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bindings for the Pushover notification service

%package -n python3-%{module}
Summary:	Bindings and command line utility for the Pushover notification service
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Bindings and command line utility for the Pushover notification
service.

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGES.rst README.rst
%{py_sitescriptdir}/%{module}.py[co]
%{py_sitescriptdir}/python_%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGES.rst README.rst
%attr(755,root,root) %{_bindir}/pushover
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}.*.pyc
%{py3_sitescriptdir}/python_%{module}-%{version}-py*.egg-info
%endif
