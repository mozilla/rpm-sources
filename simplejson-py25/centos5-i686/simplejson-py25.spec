Name: simplejson-py25
Summary: simplejson-py25
Version: 2.1.1
Release: 0moz1
License: ???
Group: Python
Source: http://pypi.python.org/packages/source/s/simplejson/simplejson-%version.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: python25

%define _python /tools/python-2.5.1/bin/python

%description
%{name}

%prep
%setup -q -n simplejson-%{version}

%build
%{_python} setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
%{_python} setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/tools
