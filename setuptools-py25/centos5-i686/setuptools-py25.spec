%define _python /tools/python-2.5.1/bin/python
%{!?python_sitelib: %define python_sitelib %(%{_python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python25-setuptools
Version:        0.6c5
Release:        2%{?dist}moz1
Summary:        Download, build, install, upgrade, and uninstall Python packages

Group:          Development/Languages
License:        PSFL/ZPL
URL:            http://peak.telecommunity.com/DevCenter/setuptools
Source0:        http://cheeseshop.python.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz
Source1:        psfl.txt
Source2:        zpl.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildArch:      noarch
Requires: python25

%description
setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.


%prep
%setup -q -n setuptools-%{version}
chmod -x *.txt
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{_python}|'


%build
CFLAGS="$RPM_OPT_FLAGS" %{_python} setup.py build_ext


%install
rm -rf $RPM_BUILD_ROOT
%{_python} setup.py install --root=$RPM_BUILD_ROOT
install -p -m 0644 %{SOURCE1} %{SOURCE2} .
find $RPM_BUILD_ROOT%{python_sitelib} -name '*.exe' | xargs rm -f
find $RPM_BUILD_ROOT%{python_sitelib} -name '*.txt' | xargs chmod -x
chmod +x $RPM_BUILD_ROOT%{python_sitelib}/setuptools/command/easy_install.py


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc *.txt
/tools
