%define name pyOpenSSL
%define version 0.5pre
%define release 1

Summary: Python wrapper module around the OpenSSL library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
Copyright: LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
Vendor: Martin Sjögren, AB Strakt <martin@strakt.com>
Url: http://pyopenssl.sourceforge.net/
BuildRequires: openssl-devel tetex-latex

%description
High-level wrapper around a subset of the OpenSSL library, includes
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes
...  and much more ;)

%prep
%setup

%build
make -C doc text ps html


%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc doc/pyOpenSSL.txt doc/pyOpenSSL.ps doc/html README
