Name: jdk1.5
Summary: An interpreted, interactive, object-oriented programming language.
Version: 1.5.0_15
Release: 0moz1
License: ???
Group: Java
Source0: jdk-%{version}-linux-amd64.bin
BuildRoot: %{_tmppath}/jdk1.5.0_15-root
AutoReqProv: no
%define __strip /bin/true
%define __os_install_post %{nil}

%define toplevel_dir jdk1.5.0_15
%define install_dir jdk-1.5.0_15

%description
%{name}

%prep
rm -rf $RPM_BUILD_DIR/%{toplevel_dir}
export MORE=100000
sh %{SOURCE0} <<EOF >/dev/null
yes
EOF

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
