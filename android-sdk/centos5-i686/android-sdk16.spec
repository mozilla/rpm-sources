%define debug_package %{nil}
%define upstream_name android-sdk
%define upstream_ver r16
%define install_dir_name %{upstream_name}-%{upstream_ver}
Name: android-sdk16
Summary: An interpreted, interactive, object-oriented programming language.
Version: %{upstream_ver}
Release: 0moz1
License: ???
Group: Java
# This isn't the original source package but rather a Mozilla built tarball.
#
# The original source package comes from Google and has to be un-tar'd and
# a GUI tool run to then install the proper SDK platforms:
#    # cltbld@mv-moz2-linux-ix-slave01
#    cd $HOME
#    mv android-sdk-linux android-sdk-linux.${prev_version}
#    wget http://dl.google.com/android/android-sdk_r16-linux.tgz
#    tar xzvf android-sdk_r16-linux.tgz
#    cd android-sdk-linux
#    tools/android update sdk --no-ui
#    ps auxww | grep adb
#    # Kill the adb server process returned by ps, just in case it 
#    # is holding something open.
#    cd ..
#    rm android-sdk_r16-linux.tgz
#    tar czvf android-sdk_r16-linux.tgz android-sdk-linux
#    cp android-sdk_r16-linux.tgz rpmbuild/SOURCES/
#    cd rpmbuild
#    rpmbuild -ba --define "_topdir $PWD" SPECS/android-sdk16.spec
#
Source0: %{upstream_name}_%{upstream_ver}-linux.tgz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
AutoReqProv: no

%define __os_install_post %{nil}
%define __strip /bin/true

%description
%{name}

%prep
%setup -q -n %{upstream_name}-linux

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
