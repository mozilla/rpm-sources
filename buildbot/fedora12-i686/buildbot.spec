Name: buildbot
Summary: buildbot
Version: 0.8.0
Release: 0moz1
License: ???
Group: Python
Source: buildbot-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: python

%define _prefix /tools/%{name}-%{version}
%define _localstatedir %{_prefix}/var
%define _mandir %{_prefix}/man
%define _infodir %{_prefix}/info

%define toplevel_dir %{name}-%{version}
%define install_dir %{toplevel_dir}
%define __os_install_post %{nil}
%define __prelink_undo_cmd %{nil}

%description
%{name}

%prep
rm -rf $RPM_BUILD_DIR/%{toplevel_dir}
tar zxf %{SOURCE0} >/dev/null

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
%{_prefix}
