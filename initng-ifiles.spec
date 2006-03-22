Summary:	.i files for initng
Name:		initng-ifiles
Version:	0.0.1
Release:	0.3
License:	GPL v2
Group:		Base
Source0:	http://download.initng.thinktux.net/initng-ifiles/%{name}-%{version}.tar.bz2
# Source0-md5:	9ec4f3b8c1a9a2af2e8254d28345c75f
URL:		http://initng.thinktux.net/
Requires:	initng
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_sysconfdir		/etc/initng
%define		_libdir			/%{_lib}/initng
%define		_vimdatadir		%{_datadir}/vim/vimfiles

%description
Official initng .i files.

# just temp placeholder for those scripts
%package fixes
Summary:	initng experimental patches and fixes
Summary(pl):	Eksperymentalne ³aty i poprawki do initng
Group:		Base
Requires:	%{name} = %{version}-%{release}

%description fixes
Contains fixes directory from initng distribution, which appear to
replace few system files. You should probably install this package
with --replacefiles rpm option.

%description fixes -l pl
Ten pakiet zawiera katalog fixes z dystrybucji initng, który wydaje
siê zastêpowaæ niektóre pliki systemowe. Prawdopodobnie nale¿y
instalowaæ ten pakiet z opcj± rpm-a --replacefiles.

%package -n vim-syntax-initng
Summary:	Vim syntax: initng
Summary(pl):	Sk³adnia dla Vima: initng
Epoch:		1
Group:		Applications/Editors/Vim
# for _vimdatadir existence
Requires:	vim >= 4:6.3.058-3

%description -n vim-syntax-initng
This plugin provides syntax highlighting for initng files.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog NEWS TEMPLATE_HEADER TODO CODING_STANDARDS
%doc doc/{iimanual,imanual}.txt
%attr(755,root,root) %{_sbindir}/gen_system_runlevel
%attr(755,root,root) %{_sbindir}/initng-segfault
%attr(755,root,root) %{_sbindir}/install_service
%attr(755,root,root) %{_sbindir}/killalli5
%attr(755,root,root) %{_sbindir}/ng-update
%attr(755,root,root) %{_sbindir}/shutdown_script
%attr(755,root,root) %{_sbindir}/system_off
%attr(755,root,root) %{_prefix}%{_sbindir}/ngcupdown
%dir %{_sysconfdir}/daemon
%dir %{_sysconfdir}/daemon/bluetooth
%dir %{_sysconfdir}/debug
%dir %{_sysconfdir}/net
%dir %{_sysconfdir}/system
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daemon/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daemon/bluetooth/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/debug/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/system/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/net/*.i
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.runlevel
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
%{_mandir}/man8/ng-update.8*
%{_mandir}/man8/install_service.8*
%{_mandir}/man8/gen_system_runlevel.8*

%files fixes
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/pcmcia/network
%config(noreplace) %verify(not md5 mtime size) /etc/hotplug/net.agent
%attr(755,root,root) %{_prefix}%{_sbindir}/ifplugd.action
%attr(755,root,root) %{_prefix}%{_sbindir}/wpa_cli.action
/etc/ifplugd/action.d/ngcupdown

%files -n vim-syntax-initng
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*
%{_vimdatadir}/ftdetect/*
