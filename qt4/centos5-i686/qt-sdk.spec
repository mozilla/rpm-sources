Name: qt-sdk
Summary: %{name}
Version: 4.6.3
Release: 2010.04moz2
License: LGPL
Group: QT
#Source0: http://get.qt.nokia.com/qtsdk/qt-sdk-linux-x86-opensource-2010.04.bin
Source0: qt-sdk-2010.04-4.6.3.tar.gz
Source1: qt-sdk-4.6.3.conf
BuildRoot: %{_tmppath}/%{name}-%{version}

Requires: fontconfig >= 2.4.2

AutoReqProv: no

%description
%{name}-%{version}

%prep
#none

%build
# To create the tarball required, run:
#su -c './qt-sdk-linux-x86-opensource-2010.04.bin --enable-components qtlibs --installdir /builds/qt-4.6.3 --mode text'
#cd /builds
#tar qt-sdk-2010.04-4.6.3.tar.gz qt-4.6.3
# Note: this installer does some weird things, so don't try to run it
# directly in a spec file.  You will end up with a broken install

%install
mkdir -p $RPM_BUILD_ROOT/builds
tar zxvf %{SOURCE0} -C $RPM_BUILD_ROOT/builds
mkdir -p $RPM_BUILD_ROOT/etc/ld.so.conf.d
install %{SOURCE1} $RPM_BUILD_ROOT/etc/ld.so.conf.d/qt-%{version}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-, root, root)
/builds/qt-%{version}
/etc/ld.so.conf.d/qt-%{version}.conf
