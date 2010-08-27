Name: build-tools
Summary: Build-tools repo
Version: ac05929dc0b1
Release: 0moz1
License: ???
Group: Python
Source0: build-tools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
AutoReqProv: no

%define toplevel_dir tools-%{version}
%define install_dir %{name}-%{version}

%description
%{name}

%prep
rm -rf $RPM_BUILD_DIR/%{toplevel_dir}
tar -zxf %{SOURCE0} >/dev/null

%build
# nothing

%install
install -d -m 755 $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/tools/%{install_dir}
rsync --exclude=.hg -av %{toplevel_dir}/ $RPM_BUILD_ROOT/tools/%{install_dir}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/tools/%{install_dir}
