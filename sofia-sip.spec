Name:           sofia-sip
Version:        1.12.11
Release:        19.2%{?dist}
Summary:        Sofia SIP User-Agent library

License:        LGPLv2+
URL:            http://sofia-sip.sourceforge.net/
Source0:        https://sourceforge.net/projects/sofia-sip/files/sofia-sip/%{version}/sofia-sip-%{version}.tar.gz/download
Patch0:         0001-fix-undefined-behaviour.patch
#BuildRequires:  doxygen >= 1.3
#BuildRequires:  graphviz
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel >= 0.9.7
BuildRequires:  glib2-devel >=  2.4
BuildRequires:  lksctp-tools-devel
BuildRequires:  devtoolset-9-libasan-devel

%description
Sofia SIP is a RFC-3261-compliant library for SIP user agents and
other network elements.  The Session Initiation Protocol (SIP) is an
application-layer control (signaling) protocol for creating,
modifying, and terminating sessions with one or more
participants. These sessions include Internet telephone calls,
multimedia distribution, and multimedia conferences.

%package devel
Summary:        Sofia-SIP Development Package
Requires:       sofia-sip = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development package for Sofia SIP UA library.

%package glib
Summary:        Glib bindings for Sofia-SIP 
Requires:       sofia-sip = %{version}-%{release}

%description glib
GLib interface to Sofia SIP User Agent library.

%package glib-devel
Summary:        Glib bindings for Sofia SIP development files
Requires:       sofia-sip-glib = %{version}-%{release}
Requires:       sofia-sip-devel = %{version}-%{release}
Requires:       pkgconfig

%description  glib-devel
Development package for Sofia SIP UA Glib library. This package
includes libraries and include files for developing glib programs
using Sofia SIP.

%package utils
Summary:        Sofia-SIP Command Line Utilities
Requires:       sofia-sip = %{version}-%{release}

%description utils
Command line utilities for the Sofia SIP UA library.

%prep
%setup0 -q -n sofia-sip-%{version}%{?work:work%{work}}
%patch0 -p1


%build
set -x
DBG_FLAGS="-O0 -fno-omit-frame-pointer -g3 -ggdb3 -fsanitize=address -frecord-gcc-switches"
%configure --disable-rpath CFLAGS="$DBG_FLAGS" LDFLAGS="$DBG_FLAGS"
make %{?_smp_mflags}
#make doxygen

%check
#TPORT_DEBUG=9 TPORT_TEST_HOST=0.0.0.0 make check

%install
export QA_RPATHS=0x0001
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name \*.la -delete
find %{buildroot} -name \*.h.in -delete
find . -name installdox -delete

%ldconfig_scriptlets

%ldconfig_scriptlets glib

%files
%doc AUTHORS ChangeLog ChangeLog.ext-trees COPYING COPYRIGHTS
%doc README README.developers RELEASE TODO 
%{_libdir}/libsofia-sip-ua.so.*

%files devel
#%doc libsofia-sip-ua/docs/html
%dir %{_includedir}/sofia-sip-1.12
%dir %{_includedir}/sofia-sip-1.12/sofia-sip
%{_includedir}/sofia-sip-1.12/sofia-sip/*.h
%exclude %{_includedir}/sofia-sip-1.12/sofia-sip/su_source.h
%dir %{_includedir}/sofia-sip-1.12/sofia-resolv
%{_includedir}/sofia-sip-1.12/sofia-resolv/*.h
%{_libdir}/libsofia-sip-ua.so
%{_libdir}/pkgconfig/sofia-sip-ua.pc
%{_datadir}/sofia-sip
%{_libdir}/libsofia-sip-ua.a

%files glib
%{_libdir}/libsofia-sip-ua-glib.so.*

%files glib-devel
#%doc libsofia-sip-ua-glib/docs/html
%{_includedir}/sofia-sip-1.12/sofia-sip/su_source.h
%{_libdir}/libsofia-sip-ua-glib.so
%{_libdir}/pkgconfig/sofia-sip-ua-glib.pc
%{_libdir}/libsofia-sip-ua-glib.a

%files utils
%{_bindir}/*
%{_mandir}/man1/*.1*

%changelog
* Wed Jun 24 2020 Davide Principi <davide.principi@nethesis.it> - 1.12.11-19.1
- Debug build on CentOS 7
