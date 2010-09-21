%define debug_package %{nil}
%define mpc_version 0.8.1
%define mpfr_version 2.4.2
%define gmp_version 5.0.1
%define gcc_prefix /tools/gcc-4.5

Name: gcc45
Summary: An interpreted, interactive, object-oriented programming language.
Version: 4.5.1
Release: 0moz2
License: GPL
Group: Development/Languages
Source: http://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.bz2
Source1: http://www.mpfr.org/mpfr-current/mpfr-%{mpfr_version}.tar.bz2
Source2: http://ftp.gnu.org/gnu/gmp/gmp-%{gmp_version}.tar.bz2
Source3: http://www.multiprecision.org/mpc/download/mpc-%{mpc_version}.tar.gz
# https://bugzilla.mozilla.org/attachment.cgi?id=457606
Patch0: plugin_finish_decl.diff
Patch1: linux64-ffi.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-root


%description
Mozilla specific GCC 4.5 version. Includes GMP, MPC and MPFR libraries.
Compiled with CXXFLAGS set to "-fPIC"

%prep
%setup -q -b 1 -b 2 -b 3 -n gcc-%{version}
%patch0 -p0
%patch1 -p0

%build
cd ../gmp-%{gmp_version}
./configure --prefix=%{gcc_prefix}
make
make install

#fix la
sed -i "s,libdir='/tools/gcc-%{version}/lib',libdir='%{gcc_prefix}/lib',g" \
  %{gcc_prefix}/lib/libgmp.la

cd ../mpfr-%{mpfr_version}
./configure --prefix=%{gcc_prefix} --with-gmp=%{gcc_prefix}
make
make install

cd ../mpc-%{mpc_version}
./configure --prefix=%{gcc_prefix} --with-gmp=%{gcc_prefix} --with-mpfr=%{gcc_prefix}
make
make install

cd ../gcc-%{version}
export LDFLAGS="-L%{gcc_prefix}/lib -Wl,-rpath,%{gcc_prefix}/lib"
export BOOT_LDFLAGS="$LDFLAGS"
export CXXFLAGS="-fPIC"
./configure --prefix=%{gcc_prefix} \
    --enable-__cxa_atexit \
    --enable-languages=c,c++ \
    --with-gmp=%{gcc_prefix} \
    --with-mpfr=%{gcc_prefix} \
    --with-mpc=%{gcc_prefix}
make BOOT_LDFLAGS="$BOOT_LDFLAGS" LDFLAGS="$LDFLAGS" bootstrap
make install

%install
# fake install, make files section happy
mkdir -p $RPM_BUILD_ROOT/%{gcc_prefix}
cp -a %{gcc_prefix}/* $RPM_BUILD_ROOT/%{gcc_prefix}/

%clean
echo rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{gcc_prefix}

%changelog
* Tue Jun 01 2010 Rail Aliev <rail@mozilla.com>
- Initial spec
