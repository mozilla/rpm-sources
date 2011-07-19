%define debug_package %{nil}
%define upstream_name android-ndk
%define upstream_ver r5c
%define install_dir_name %{upstream_name}-%{upstream_ver}
Name: android-ndk5
Summary: An interpreted, interactive, object-oriented programming language.
Version: %{upstream_ver}
Release: 0moz3
License: ???
Group: Java
# This is the upstream NDK binary distribution tarball.  All modifications are
# performed in this spec file's %build section.  If extra files need to be 
# included for modifications, they should use Source1: <path> and be copied
# as needed.
Source0: http://dl.google.com/android/ndk/%{upstream_name}-%{upstream_ver}-linux-x86.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
AutoReqProv: no

%define __os_install_post %{nil}
%define __strip /bin/true

%description
%{name}

%prep
%setup -q -n android-ndk-%{upstream_ver}

%build
chmod -R a+rX *

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/tools/%{install_dir_name}
cp -a * $RPM_BUILD_ROOT/tools/%{install_dir_name}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/tools/%{install_dir_name}
