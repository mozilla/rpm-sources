Name: gcc411
Summary: An interpreted, interactive, object-oriented programming language.
Version: 4.1.1
Release: 0moz1
License: GPL
Group: Mozilla
Source: gcc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%define _prefix /tools/gcc-%{version}
%define _localstatedir %{_prefix}/var
%define _mandir %{_prefix}/man
%define _infodir %{_prefix}/info

%description
%{name}

%prep
%setup -q -n gcc-%{version}-20061011

%build
./configure --enable-long-long --enable-threads=posix --enable-__cxa_atexit --enable-languages=c,c++ --with-system-zlib --prefix=%{_prefix}
make

%install
[ -d $RPM_BUILD_ROOT ] && rm -fr $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_prefix}
