Name: twisted
Summary: twisted
Version: 2.4.0
Release: 0moz1
License: ???
Group: Python
Source: Twisted-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: python25
Requires: zope.interface
Requires: twisted-core

%define _python /tools/python-2.5.1/bin/python
%define _prefix /tools/%{name}-%{version}
%define _localstatedir %{_prefix}/var
%define _mandir %{_prefix}/man
%define _infodir %{_prefix}/info

%description
%{name}

%prep
%setup -q -n Twisted-%{version}

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
