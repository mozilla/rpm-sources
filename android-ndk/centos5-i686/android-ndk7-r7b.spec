%define upstream_name android-ndk
%define ndk_name android-ndk7
%define ndk_ver r7b
%define gcc_ver 4.6.3
%define binutils_ver 2.22
%define binutils_type releases
%define gmp_ver 5.0.4
%define mpc_ver 0.9
%define mpfr_ver 3.0.1
%define gdb_ver 6.6a
%define ndk_dir %{upstream_name}-%{ndk_ver}
Name: %{ndk_name}
Summary: An interpreted, interactive, object-oriented programming language.
Version: %{ndk_ver}
Release: 0moz2
License: ???
Group: Java
Source0: http://dl.google.com/android/ndk/%{upstream_name}-%{ndk_ver}-linux-x86.tar.bz2
Source1: ndk-build-%{ndk_ver}.tar.bz2
Source2: ftp://ftp.gnu.org/gnu/gcc/gcc-%{gcc_ver}/gcc-%{gcc_ver}.tar.bz2
Source3: ftp://sourceware.org/pub/binutils/%{binutils_type}/binutils-%{binutils_ver}.tar.bz2
Source4: ftp://ftp.gmplib.org/pub/gmp-%{gmp_ver}/gmp-%{gmp_ver}.tar.bz2
Source5: http://www.multiprecision.org/mpc/download/mpc-%{mpc_ver}.tar.gz
Source6: http://mpfr.loria.fr/mpfr-%{mpfr_ver}/mpfr-%{mpfr_ver}.tar.bz2
Source7: ftp://sourceware.org/pub/gdb/releases/gdb-%{gdb_ver}.tar.bz2
Patch0: ndk-build-tools.patch
Patch1: ndk-gcc.patch
Patch2: gold-thumb-plt-2.22.diff
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
AutoReqProv: no

%define __os_install_post %{nil}
%define __strip /bin/true
%define debug_package %{nil}

%description
%{name}

%prep
%setup -q -n %{ndk_dir}
%patch0 -p1
for i in gcc binutils gmp mpc mpfr gdb; do
  mkdir -p src/$i
done
%setup -q -D -T -a 1 -n %{ndk_dir}
%setup -q -D -T -a 2 -n %{ndk_dir}/src/gcc
cd gcc-%{gcc_ver}
%patch1 -p1
cd ..
%setup -q -D -T -a 3 -n %{ndk_dir}/src/binutils
cd binutils-%{binutils_ver}
%patch2 -p1
cd ..
cp $RPM_SOURCE_DIR/gmp-%{gmp_ver}.tar.bz2 $RPM_BUILD_DIR/%{ndk_dir}/src/gmp
cp $RPM_SOURCE_DIR/mpc-%{mpc_ver}.tar.gz $RPM_BUILD_DIR/%{ndk_dir}/src/mpc
cp $RPM_SOURCE_DIR/mpfr-%{mpfr_ver}.tar.bz2 $RPM_BUILD_DIR/%{ndk_dir}/src/mpfr
%setup -q -D -T -a 7 -n %{ndk_dir}/src/gdb

%build
# Mozilla buildbots specific settings
export LDFLAGS=-Wl,-rpath,/tools/gcc-4.5/lib
export CC=/tools/gcc-4.5/bin/gcc
export CXX=/tools/gcc-4.5/bin/g++
$RPM_BUILD_DIR/%{ndk_dir}/build/tools/build-gcc.sh \
  --binutils-version=%{binutils_ver} \
  --gmp-version=%{gmp_ver} \
  --mpfr-version=%{mpfr_ver} \
  --mpc-version=%{mpc_ver} \
  --build-out=$RPM_BUILD_DIR/%{ndk_dir}/build-tmp \
%if %_target_cpu == x86_64
  --try-64 \
%endif
  $RPM_BUILD_DIR/%{ndk_dir}/src/ \
  $RPM_BUILD_DIR/%{ndk_dir} \
  arm-linux-androideabi-%{gcc_ver}

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/tools/%{ndk_dir}
tar -C $RPM_BUILD_DIR/%{ndk_dir} -cf - --exclude ./src --exclude ./build-tmp . | tar -C $RPM_BUILD_ROOT/tools/%{ndk_dir} -xf -

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(755, root, root)
/tools/%{ndk_dir}
