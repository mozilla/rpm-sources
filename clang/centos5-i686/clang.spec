%define REPO_REV 132336
Name: clang
Summary: clang
Version: 3.0
Release: r%{REPO_REV}.moz0
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%define toplevel_dir clang-%{version}-%{release}
%define install_dir /tools/%{name}-%{version}

%description
clang snapshot packaged for mozilla build machines

%prep
rm -rf $RPM_BUILD_DIR/%{toplevel_dir}
svn co -r %{REPO_REV} http://llvm.org/svn/llvm-project/llvm/trunk $RPM_SOURCE_DIR/llvm
svn co -r %{REPO_REV} http://llvm.org/svn/llvm-project/cfe/trunk $RPM_SOURCE_DIR/clang
ln -sf ../../clang $RPM_SOURCE_DIR/llvm/tools
mkdir -p %{toplevel_dir}

%build
cd %{toplevel_dir}
# CC and CXX here are specific to our build machines
# For testing you may want to use the commented out line below
$RPM_SOURCE_DIR/llvm/configure --enable-optimized --prefix=%{install_dir} CC="ccache /tools/gcc-4.5/bin/gcc -static-libgcc" CXX="ccache /tools/gcc-4.5/bin/g++ -static-libgcc -static-libstdc++"
#$RPM_SOURCE_DIR/llvm/configure --enable-optimized --prefix=%{install_dir} CC="ccache gcc" CXX="ccache g++"
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
