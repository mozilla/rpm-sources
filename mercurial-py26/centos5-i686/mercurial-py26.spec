Name: mercurial-py26
Summary: Mercurial
Version: 1.5.1
Release: 0moz1
License: ???
Group: Python
Source: mercurial-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: python26

%define _python /tools/python-2.6.5/bin/python

%description
%{name}

%prep
%setup -q -n mercurial-%{version}

%build
%{_python} setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
%{_python} setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/tools/python-2.6.5/lib/python2.6/site-packages
/tools/python-2.6.5/bin/hg
