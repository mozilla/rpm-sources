Name: mercurial
Summary: Mercurial
Version: 1.1.2
Release: 0moz1
License: ???
Group: Python
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%define _python /tools/python-2.5.1/bin/python

%description
%{name}

%prep
%setup -q

%build
%{_python} setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
%{_python} setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/tools/python-2.5.1/lib/python2.5/site-packages
/tools/python-2.5.1/bin/hg
