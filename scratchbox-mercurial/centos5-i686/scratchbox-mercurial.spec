Name: scratchbox-mercurial
Summary: scratchbox-mercurial
Version: 1.5.1
Release: 0moz1
License: ???
Group: Python
Source: mercurial-%{version}.linux-arm.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: scratchbox
AutoReqProv: no

%define unpack_dir builds/scratchbox/users/cltbld/targets/FREMANTLE_ARMEL
%define toplevel_dir usr

%description
%{name}

%prep
%setup -q -c -n scratchbox-mercurial

%build
# None

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{unpack_dir}
rsync -av %{toplevel_dir}/ $RPM_BUILD_ROOT/%{unpack_dir}/%{toplevel_dir}/

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/%{unpack_dir}/%{toplevel_dir}
