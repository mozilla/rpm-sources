Name: scratchbox-host-usr
Summary: scratchbox-host-usr
Version: 1
Release: 0moz1
License: ???
Group: Python
Source0: scratchbox-host-usr-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: scratchbox
Conflicts: scratchbox-mercurial
AutoReqProv: no

%description
%{name}

%prep
%setup -q -c -n %{name}

%build
# None

%pre
rm -f /builds/scratchbox/users/cltbld/targets/CHINOOK-ARMEL-2007/usr/bin/hg
find /builds/scratchbox/devkits -type d -name 'mercurial' -exec rm -rf {} \;
find /builds/scratchbox/devkits -type d -name 'hgext' -exec rm -rf {} \;
su cltbld -c "/builds/scratchbox/moz_scratchbox sb-conf select CHINOOK-ARMEL-2007"
su cltbld -c "/builds/scratchbox/moz_scratchbox fakeroot apt-get remove -y python2.5"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/builds/scratchbox/users/cltbld/host_usr/
rsync -av scratchbox/users/cltbld/host_usr/ \
       $RPM_BUILD_ROOT/builds/scratchbox/users/cltbld/host_usr/
mkdir -p $RPM_BUILD_ROOT/builds/scratchbox/users/cltbld/home/cltbld

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/builds/scratchbox/users/cltbld/host_usr
