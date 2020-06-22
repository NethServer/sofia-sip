
Name:		sofia-sip
Version:	1.12.11
Release:	99%{?dist}
Summary:	Open-source SIP User-Agent library

Group:		Network
License:	LGPL
URL:		http://sofia-sip.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
Patch0:		0001-fix-undefined-behaviour.patch

BuildRequires:	autoconf nethserver-devtools
AutoReq: no
BuildRequires: libubsan libasan
Requires:   libubsan libasan


%description
Sofia-SIP is an open-source SIP User-Agent library, compliant with the
IETF RFC3261 specification.

It can be used as a building block for SIP client software for uses such
as VoIP, IM, and many other real-time and person-to-person communication services.

The primary target platform for Sofia-SIP is GNU/Linux. Sofia-SIP is based on
a SIP stack developed at the Nokia Research Center. Sofia-SIP is licensed
under the LGPL.


%prep
%setup -q
%patch0 -p1

%build
#DEB_FLAGS="-O0 -fno-omit-frame-pointer -g3 -ggdb3 -fsanitize=address,undefined"
DEB_FLAGS="-O0 -fno-omit-frame-pointer -g3 -ggdb3 -fsanitize=address"
export CFLAGS="$DEB_FLAGS"
export LDFLAGS="$DEB_FLAGS"

%configure --prefix=%{_prefix} \
  --exec-prefix=%{_prefix} \
  --sysconfdir=%{_sysconfdir} \
  --bindir=%{_bindir} \
  --datadir=%{_var}/www

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} make install
rm -rf %{buildroot}/usr/share/man/man1
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%clean
rm -rf %{buildroot}

%files -f %{name}-%{version}-filelist
%defattr(-,root,root,-)

%doc


%changelog
* Thu Mar 9 2017 Giovanni Bezicheri <giovanni.bezicheri@nethesis.it> - 1.12.11-1
- First Release.

