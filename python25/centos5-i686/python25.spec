%define pybasever 2.5

Name: python25
Summary: An interpreted, interactive, object-oriented programming language.
Version: %{pybasever}.1
Release: 0moz1%{?dist}
License: PSF - see LICENSE
Group: Development/Languages
Source: Python-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://www.python.org/

%define _prefix /tools/python-%{version}
%define _localstatedir %{_prefix}/var
%define _mandir %{_prefix}/man
%define _infodir %{_prefix}/info

%description
%{name}

%prep
%setup -q -n Python-%{version}

# Temporary workaround to avoid confusing find-requires: don't ship the tests
# as executable files
chmod 0644 Lib/test/test_*.py

# Make rpm happy
sed -i 's,/usr/local/bin/python,/usr/bin/env python,g' Lib/cgi.py

%build
./configure --prefix=%{_prefix}

make

%install
[ -d $RPM_BUILD_ROOT ] && rm -fr $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Clean up the testsuite - we don't need compiled files for it
find $RPM_BUILD_ROOT%{_libdir}/python%{pybasever}/test \
    -name "*.pyc" -o -name "*.pyo" | xargs rm -f

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_prefix}
