Name: android-ndk
Summary: An interpreted, interactive, object-oriented programming language.
Version: r3
Release: 0moz1
License: ???
Group: Java
Source0: android-ndk-r3-linux-x86.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%define toplevel_dir %{name}-%{version}
%define install_dir %{toplevel_dir}
%define __os_install_post %{nil}
%define __strip /bin/true

%description
%{name}

%prep
rm -rf $RPM_BUILD_DIR/%{toplevel_dir}
unzip %{SOURCE0} >/dev/null

%build
# none

%install
install -d -m 755 $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/tools/%{install_dir}
rsync -av %{toplevel_dir}/ $RPM_BUILD_ROOT/tools/%{install_dir}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/tools/%{install_dir}
