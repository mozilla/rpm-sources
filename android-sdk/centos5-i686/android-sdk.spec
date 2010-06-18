Name: android-sdk
Summary: An interpreted, interactive, object-oriented programming language.
Version: r8
Release: 0moz2
License: ???
Group: Java
# This isn't the original source package but rather a Mozilla built tarball.
# The original source package requires downloading additional pieces from
# the Internet, which is difficult to do in RPM, and makes reproducability
# impossible.
Source0: android-sdk-r8.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-root
AutoReqProv: no

%define toplevel_dir %{name}-%{version}
%define install_dir %{toplevel_dir}
%define __os_install_post %{nil}
%define __strip /bin/true

%description
%{name}

%prep
rm -rf $RPM_BUILD_DIR/%{toplevel_dir}
unzip %{SOURCE0} >/dev/null
find platforms/android-8 \
    -name "*" -type f | xargs chmod 0644

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
