%define datestamp 2010-03-30-1129
%define source scratchbox-%{datestamp}.tar.bz2

Name: scratchbox
Summary: Scratchbox
Version: 20100330
Release: 0moz1
License: ???
Group: Scratchbox
# This isn't the original source package but rather a Mozilla built tarball.
# The original source package requires downloading additional pieces from
# the Internet, which is difficult to do in RPM, and makes reproducability
# impossible.
Source0: %{source}
BuildRoot: %{_tmppath}/%{name}-%{version}-root
AutoReqProv: no

%define __os_install_post %{nil}
%define __strip /bin/true

%description
%{name}

%prep
# none

%build
# none

%install
mkdir -p $RPM_BUILD_ROOT/tmp
cp -a %{SOURCE0} $RPM_BUILD_ROOT/tmp

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/tmp

%post
err=0
if [[ -e /builds/scratchbox/sbin/sbox_ctl ]]; then
    /builds/scratchbox/sbin/sbox_ctl stop
fi
if [[ -e /builds/scratchbox/sbin/sbox_umount_all ]]; then
    /builds/scratchbox/sbin/sbox_umount_all
fi
while [[ `mount | grep "^/builds/slave"` ]] ; do
    umount /builds/slave || err=1
    sleep 2
done
while [[ `mount | grep "^/home/cltbld/.ssh"` ]] ; do
    umount /home/cltbld/.ssh || err=1
    sleep 2
done
tar -C /builds -jxpsf /tmp/%{source}
if [ $? != 0 ]; then
    err=1
fi
if [ $err != 0 ]; then
    rm -rf /builds/scratchbox
    rm -f /tmp/%{source}
    exit 1
fi
touch /builds/scratchbox/deployed
touch /builds/scratchbox/deployed-%{datestamp}
/builds/scratchbox/sbin/sbox_ctl start
rm -f /tmp/%{source}

%postun
if [[ -e /builds/scratchbox/sbin/sbox_ctl ]]; then
    /builds/scratchbox/sbin/sbox_ctl stop
fi
if [[ -e /builds/scratchbox/sbin/sbox_umount_all ]]; then
    /builds/scratchbox/sbin/sbox_umount_all
fi
while [[ `mount | grep "^/builds/slave"` ]] ; do
    umount /builds/slave
    sleep 2
done
while [[ `mount | grep "^/home/cltbld/.ssh"` ]] ; do
    umount /home/cltbld/.ssh
    sleep 2
done
rm -rf /builds/scratchbox
