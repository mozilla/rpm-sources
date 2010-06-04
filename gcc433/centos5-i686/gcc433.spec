Name: gcc433
Summary: An interpreted, interactive, object-oriented programming language.
Version: 4.3.3
Release: 0moz1
License: ???
Group: C
# This isn't the original source package but rather a Mozilla built tarball.
# The original source package requires downloading additional pieces from
# the Internet, which is difficult to do in RPM, and makes reproducability
# impossible.
Source0: gcc433-4.3.3.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
AutoReqProv: no

%define __strip /bin/true
%define __os_install_post %{nil}

%define toplevel_dir gcc-4.3.3
%define install_dir %{toplevel_dir}

%description
%{name}

%prep
rm -rf $RPM_BUILD_DIR/%{toplevel_dir}
tar -zxf %{SOURCE0} >/dev/null

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
