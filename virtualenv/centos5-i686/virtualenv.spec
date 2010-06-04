%define changeset 8dd7663d9811

Name: virtualenv
Summary: virtualenv
Version: 1.4.8
Release: 0moz1
License: ???
Group: Python
Source: virtualenv-%{changeset}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: python26

%define _python /tools/python-2.6.5/bin/python

%description
%{name}

%prep
%setup -q -n virtualenv-%{changeset}

%build
%{_python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{_python} setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/tools/python-2.6.5/lib/python2.6/site-packages
/tools/python-2.6.5/bin
