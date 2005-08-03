%define __python /usr/bin/python2
Summary: Python wrapper module around the OpenSSL library
Name: pyOpenSSL
Version: 0.6
Release: 1.p24.5
Source0: http://pyopenssl.sf.net/%{name}-%{version}.tar.gz
Patch0: pyOpenSSL-0.5.1-openssl097.patch
Patch2: pyOpenSSL-elinks.patch
Patch3: pyOpenSSL-nopdfout.patch
License: LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
Url: http://pyopenssl.sourceforge.net/
Requires: python
BuildRequires: elinks openssl-devel python-devel perl tetex-dvips tetex-latex

%description
High-level wrapper around a subset of the OpenSSL library, includes
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes
...  and much more ;)

%prep
%setup -q
%patch0 -p1 -b .openssl097
%patch2 -p1 -b .elinks
%patch3 -p1 -b .nopdfout

%build
%{__python} setup.py build
make -C doc ps
# ia64 does not have latex2html
%ifarch i386
make -C doc text html
%endif

%install
%{__python} setup.py install \
--root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
sed -e 's|/[^/]*$||' INSTALLED_FILES | grep "site-packages/" | \
    sort | uniq | awk '{ print "%attr(755,root,root) %dir " $1}' > INSTALLED_DIRS
cat INSTALLED_FILES INSTALLED_DIRS > INSTALLED_OBJECTS

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_OBJECTS
/usr/lib/python2.4/site-packages/OpenSSL/*.pyo
%defattr(-,root,root)
%doc README doc/pyOpenSSL.ps 
%ifarch i386
%doc doc/pyOpenSSL.txt doc/html
%endif

%changelog
* Wed Aug 03 2005 Karsten Hopp <karsten@redhat.de> 0.6-1.p24.5
- current rpm creates .pyo files, include them in filelist

* Thu Mar 17 2005 Mihai Ibanescu <misa@redhat.com> 0.6-1.p24.4
- rebuilt

* Mon Mar 14 2005 Mihai Ibanescu <misa@redhat.com> 0.6-1.p24.3
- rebuilt

* Mon Mar  7 2005 Tomas Mraz <tmraz@redhat.com> 0.6-1.p23.2
- rebuild with openssl-0.9.7e

* Tue Nov  9 2004 Nalin Dahyabhai <nalin@redhat.com> 0.6-1.p23.1
- rebuild

* Fri Aug 13 2004 Mihai Ibanescu <misa@redhat.com> 0.6-1
- 0.6 is out

* Tue Aug 10 2004 Mihai Ibanescu <misa@redhat.com> 0.6-0.90.rc1
- release candidate

* Thu Jun 24 2004 Mihai Ibanescu <misa@redhat.com> 0.5.1-24
- rebuilt

* Mon Jun 21 2004 Mihai Ibanescu <misa@redhat.com> 0.5.1-23
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Nov  5 2003 Mihai Ibanescu <misa@redhat.com> 0.5.1-20
- rebuilt against python 2.3.2

* Fri Aug  8 2003 Mihai Ibanescu <misa@redhat.com> 0.5.1-12
- lynx no longer supported, using elinks instead (patch from
  Michael Redinger <michael.redinger@uibk.ac.at>, bug #101947 )

* Wed Jun  4 2003 Elliot Lee <sopwith@redhat.com> 0.5.1-11
- Rebuilt

* Wed Jun  4 2003 Mihai Ibanescu <misa@redhat.com> 0.5.1-10.7.x
- Built on 7.x

* Mon Mar  3 2003 Mihai Ibanescu <misa@redhat.com> 0.5.1-9
- bug #73967: Added Requires: python 

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 21 2003 Mihai Ibanescu <misa@redhat.com> 0.5.1-7
- bug #84803: Added patch to expose more flags

* Fri Jan 31 2003 Mihai Ibanescu <misa@redhat.com> 0.5.1-5
- installing to %%{_libdir}

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 0.5.1-3
- rebuild

* Fri Jan  3 2003 Nalin Dahyabhai <nalin@redhat.com>
- Add -I and -L flags for finding Kerberos headers and libraries, in case
  they're referenced

* Tue Dec  3 2002 Mihai Ibanescu <misa@redhat.com>
- Fix for bug 73967: site-packages/OpenSSL not owned by this package
- Adding hacks around the lack of latex2html on ia64

* Tue Sep 24 2002 Mihai Ibanescu <misa@redhat.com>
- 0.5.1

* Thu Aug 29 2002 Mihai Ibanescu <misa@redhat.com>
- Building 0.5.1rc1 with version number 0.5.0.91 (this should also fix the big
  error of pushing 0.5pre previously, since it breaks rpm's version comparison
  algorithm).
- We use %{__python}. Too bad I can't pass --define's to distutils.

* Fri Aug 16 2002 Mihai Ibanescu <misa@redhat.com>
- Building 0.5

* Fri Jun 14 2002 Mihai Ibanescu <misa@redhat.com>
- Added documentation
