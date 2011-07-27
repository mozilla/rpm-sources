%define REPO_REV 135723
Name: clang
Summary: clang
Version: 3.0
Release: r%{REPO_REV}.moz0
License: BSD
Group: Development/Libraries
Patch0: pr671711-hack.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%define toplevel_dir clang-%{version}-%{release}
%define install_dir /tools/%{name}-%{version}

%description
clang snapshot packaged for mozilla build machines

%prep
rm -rf $RPM_BUILD_DIR/%{toplevel_dir}
svn co -r %{REPO_REV} http://llvm.org/svn/llvm-project/llvm/trunk $RPM_SOURCE_DIR/llvm
svn co -r %{REPO_REV} http://llvm.org/svn/llvm-project/cfe/trunk $RPM_SOURCE_DIR/clang
cd $RPM_SOURCE_DIR/clang
%patch0 -p1
cd -
ln -sf ../../clang $RPM_SOURCE_DIR/llvm/tools
mkdir -p %{toplevel_dir}

%build
cd %{toplevel_dir}

%ifarch x86_64
TRIPLE=x86_64-unknown-linux-gnu
MULTILIB="--with-cxx-include-32bit-dir=32"
%else
TRIPLE=i686-pc-linux-gnu
MULTILIB=""
%endif

# CC and CXX here are specific to our build machines
# The *-include-* options make clang use the same c++ headers as the gcc 4.5
# that we use.
$RPM_SOURCE_DIR/llvm/configure \
  --enable-optimized \
  --prefix=%{install_dir} \
  --with-cxx-include-root=/tools/gcc-4.5/include/c++/4.5.2/ \
  --with-cxx-include-arch=$TRIPLE \
  $MULTILIB \
  CC="/tools/gcc-4.5/bin/gcc -static-libgcc" \
  CXX="/tools/gcc-4.5/bin/g++ -static-libgcc -static-libstdc++"
make -j4

%install
install -d -m 755 $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{install_dir}
cd %{toplevel_dir}
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root ,root)
%{install_dir}

%changelog
* Tue May 31 2011 Chris AtLee <catlee@mozilla.com>
- Initial spec
