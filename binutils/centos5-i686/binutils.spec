# Named with the moz_ prefix so it doesn't conflict with the existing binutils
# package. Include the version in the same so we can have multiple versions of
# it installed.
%define real_name binutils
Version: 2.22
Name: moz_%{real_name}_%{version}
Summary: %{real_name}
Release: 0moz1
License: GPL
Group: C
Source0: http://ftp.gnu.org/gnu/%{real_name}/%{real_name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%define toplevel_dir %{real_name}-%{version}
%define install_dir /tools/%{toplevel_dir}

%description
binutils packaged for mozilla build machines

%prep
%setup -n %{real_name}-%{version}

%build
# CC and CXX here are specific to our build machines
# For testing you may want to use the commented out line below
#./configure --enable-gold=default --prefix=%{install_dir} CC="ccache gcc" CXX="ccache g++"
./configure --enable-gold=default --enable-lto --enable-plugins --prefix=%{install_dir} CC="/tools/gcc-4.5/bin/gcc -static-libgcc" CXX="/tools/gcc-4.5/bin/g++ -static-libgcc -static-libstdc++"
make

%install
install -d -m 755 $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{install_dir}
make install DESTDIR=$RPM_BUILD_ROOT
# Make another directory available where ld.bfd is the default
cp -al $RPM_BUILD_ROOT/%{install_dir}/bin $RPM_BUILD_ROOT/%{install_dir}/bin.bfd
ln -f $RPM_BUILD_ROOT/%{install_dir}/bin.bfd/ld.bfd $RPM_BUILD_ROOT/%{install_dir}/bin.bfd/ld

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{install_dir}

%changelog
* Mon Dec 19 2011 Chris AtLee <catlee@mozilla.com> 2.22-0moz1
- Updated to binutils 2.22

* Wed Jul 20 2011 Chris AtLee <catlee@mozilla.com> 2.21.1-1
- Initial spec for binutils 2.21.1
