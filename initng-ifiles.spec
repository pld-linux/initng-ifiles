Summary:	.i files for initng
Summary(pl.UTF-8):	Pliki .i dla initng
Name:		initng-ifiles
Version:	0.1.5
Release:	0.1
License:	GPL v2
Group:		Base
Source0:	http://download.initng.org/initng-ifiles/v0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	23a06cf1c8c25e049a8c962acfda9ea7
URL:		http://www.initng.org/
BuildRequires:	cmake
BuildRequires:	initng-devel
Requires:	initng
Requires:	initng-tools = %{version}-%{release}
Obsoletes:	initng-ifiles-fixes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_sysconfdir		/etc/initng
%define		_libdir			/%{_lib}/initng
%define		_vimdatadir		%{_datadir}/vim/vimfiles

%description
Official initng .i files.

%package -n initng-tools
Summary:	Tools used by initng .i files
Summary(pl.UTF-8):	Narzędzia używane przez pliki .i z initng
Group:		Base

%description -n initng-tools
Shared tools used by initng-ifiles and initng-pld packages.

%description -n initng-tools -l pl.UTF-8
Współdzielone narzędzia używane przez pakiety initng-ifiles i
initng-pld.

%package -n vim-syntax-initng
Summary:	Vim syntax: initng
Summary(pl.UTF-8):	Składnia dla Vima: initng
Epoch:		1
Group:		Applications/Editors/Vim
# for _vimdatadir existence
Requires:	vim-rt >= 4:6.3.058-3

%description -n vim-syntax-initng
This plugin provides syntax highlighting for initng files.

%description -n vim-syntax-initng -l pl.UTF-8
Ta wtycza dostarcza podświetlanie składni dla plików initng.

%prep
%setup -q

%build
%cmake . \
	-DLIB_INSTALL_DIR=/%{_lib}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}
mv -f $RPM_BUILD_ROOT/%{_lib}/libgenrunlevel{.generic,}
rm -f $RPM_BUILD_ROOT/%{_lib}/libgenrunlevel.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog TODO
%doc doc/{iimanual,imanual}.txt
%attr(755,root,root) %{_sbindir}/genrunlevel
%attr(755,root,root) %{_sbindir}/install_service
%attr(755,root,root) /%{_lib}/libgenrunlevel
%dir %{_sysconfdir}/daemon
%dir %{_sysconfdir}/daemon/bluetooth
%dir %{_sysconfdir}/daemon/exim
%dir %{_sysconfdir}/daemon/lirc
%dir %{_sysconfdir}/daemon/nut
%dir %{_sysconfdir}/daemon/vmware
%dir %{_sysconfdir}/net
%dir %{_sysconfdir}/runlevel
%dir %{_sysconfdir}/service
%dir %{_sysconfdir}/system
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daemon/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daemon/bluetooth/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daemon/exim/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daemon/lirc/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daemon/nut/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daemon/vmware/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/net/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/runlevel/*.runlevel
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/service/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/system/*.i

%dir %{_libdir}/scripts
%dir %{_libdir}/scripts/net
%attr(755,root,root) %{_libdir}/scripts/net/dhclient-wrapper
%attr(755,root,root) %{_libdir}/scripts/net/dhcp
%attr(755,root,root) %{_libdir}/scripts/net/dhcpcd-backgrounder
%attr(755,root,root) %{_libdir}/scripts/net/essidnet
%attr(755,root,root) %{_libdir}/scripts/net/functions
%attr(755,root,root) %{_libdir}/scripts/net/gentoo-functions
%attr(755,root,root) %{_libdir}/scripts/net/ifconfig
%attr(755,root,root) %{_libdir}/scripts/net/interface
%attr(755,root,root) %{_libdir}/scripts/net/iproute2
%attr(755,root,root) %{_libdir}/scripts/net/iwconfig
%attr(755,root,root) %{_libdir}/scripts/net/system
%attr(755,root,root) %{_libdir}/scripts/net/udhcpc-wrapper
%attr(755,root,root) %{_libdir}/scripts/net/wpa_supplicant
%attr(755,root,root) %{_libdir}/scripts/net/wpa_cli.action
%{_mandir}/man8/genrunlevel.8*
%{_mandir}/man8/install_service.8*

%files -n initng-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ng-update
%{_mandir}/man8/ng-update.8*

%files -n vim-syntax-initng
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*
%{_vimdatadir}/ftdetect/*
