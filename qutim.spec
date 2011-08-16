%global gitdate 20110815
%global gitcommit 18f571a
#git rev-parse --short HEAD

Name:           qutim
Version:        0.3
Release:        2.%{gitdate}git%{gitcommit}%{?dist}.R
Summary:        Multiprotocol (ICQ, Jabber, IRC etc) instant messenger with modern Qt4 interface
Summary(ru):    Мультиплатформенный, мультипротокольный (ICQ, Jabber, IRC...) мессенджер на QT4

License:        GPLv2+ and CC-BY-SA
URL:            http://www.qutim.org/
Source0:        %{name}-%{version}-git%{gitcommit}.tar.xz

BuildRequires:  cmake >= 2.6, desktop-file-utils, qca2-devel
BuildRequires:  qt-devel >= 1:4.0, libidn-devel, dos2unix, qt-webkit-devel
BuildRequires:  aspell-devel, libpurple-devel, doxygen

Requires:       qca-cyrus-sasl


%description
qutIM - free open-source multiprotocol ( ICQ, Jabber/GTalk/
/Ya.Online/LiveJournal.com, Mail.Ru, IRC ) instant messenger for
Windows and Linux systems.

%description -l ru
qutIM - Открытый мультипротокольный (уже поддерживаются:
ICQ, Jabber, GTalk, Ya.Online, LiveJournal.com, Mail.Ru, IRC клиент
обмена сообщениями для Linux и Windows.
Написан с нуля и призван быть лёгким, простым, быстрым, красивым и
расширяемым за счёт модулей-плагинов.

%package        devel
Summary:        Development files for qutIM

%description    devel
Development files for qutIM

%package        doc
Summary:        Documentation files for qutIM

%description    doc
Documentation files for qutIM


%prep
%setup -q -n qutim


%build
%{cmake} -DCMAKE_SKIP_RPATH:BOOL=ON .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
#find $RPM_BUILD_ROOT -name "*" -exec chrpath --delete {} \; 2>/dev/null

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_libdir}/libjreen.so.0.1.0
%{_libdir}/libqutim.so.0.2.80.0
%{_libdir}/libjreen.so
%{_libdir}/libqutim.so
%{_libdir}/libjreen.so.0
%{_libdir}/libqutim.so.0
%{_datadir}/applications/%{name}.desktop
%{_datadir}/apps/%{name}
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/*x*/places/user-identity.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/oxygen/scalable/status/*%{name}*.svg
%{_datadir}/icons/ubuntu-mono-dark/scalable/status/*%{name}*.svg
%{_datadir}/icons/ubuntu-mono-light/scalable/status/*%{name}*.svg
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}/config/profile.json

%files doc
%defattr(-,root,root)
%doc %{_datadir}/%{name}/doc

%files devel
%defattr(-,root,root)
%{_includedir}/jreen
%{_includedir}/%{name}
%{_datadir}/cmake/Modules/*

%changelog
* Tue Aug 16 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.3-2.20110815git18f571a.R
- Added requires qca-cyrus-sasl

* Mon Aug 15 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.3-1.20110815git18f571a.R
- Update from git

* Fri Aug 12 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.3-1.20110811git5431b1f.R
- Initial release
