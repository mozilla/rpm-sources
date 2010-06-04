Name: zope.interface
Summary: Zope.Interface
Version: 3.3.0
Release: 0moz1
License: ???
Group: Python
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/zope-interface-%{version}-root
Requires: python25

%define _python /tools/python-2.5.1/bin/python
%define _prefix /tools/zope-interface-%{version}
%define _localstatedir %{_prefix}/var
%define _mandir %{_prefix}/man
%define _infodir %{_prefix}/info

%description
%{name}

%prep
%setup -q

%build
%{_python} setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
%{_python} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_prefix}
