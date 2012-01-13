%global date 20120113
%global gitcommit 6a8a205
%global realver 0.3

Name:           qutim
Version:        %{realver}.%{date}git%{gitcommit}
Release:        1%{dist}.R
Summary:        Multiprotocol (ICQ, Jabber, IRC etc) instant messenger with modern Qt4 interface
Summary(ru):    Мультиплатформенный, мультипротокольный (ICQ, Jabber, IRC...) мессенджер на QT4

License:        GPLv2+ and CC-BY-SA
URL:            http://www.qutim.org/
Source0:        %{name}-%{realver}.git.tar.xz

BuildRoot:      /{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  qca2-devel
BuildRequires:  qt-devel
BuildRequires:  libidn-devel
BuildRequires:  dos2unix
BuildRequires:  qt-webkit-devel
BuildRequires:  aspell-devel
BuildRequires:  libpurple-devel
BuildRequires:  doxygen
BuildRequires:  libXScrnSaver-devel
BuildRequires:  phonon-devel
BuildRequires:  telepathy-qt4-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  dbusmenu-qt-devel
BuildRequires:  qt-mobility-devel

Requires:       qca-cyrus-sasl
Requires:       jreen


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
BuildArch:      noarch

%description    doc
Documentation files for qutIM

%package -n jreen
Summary:        Jreen library for qutim

%description -n jreen
Jreen library for qutim

%package -n jreen-devel
Summary:        Development files for Jreen library for qutim

%description -n jreen-devel
Development files for Jreen library for qutim


%prep
%setup -q -n %{name}-%{realver}.git


%build
%{cmake} -DCMAKE_SKIP_RPATH:BOOL=ON .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n jreen -p /sbin/ldconfig

%postun -n jreen -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_libdir}/libqutim.so.*
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
%{_includedir}/%{name}
%{_datadir}/cmake/Modules/*
%{_libdir}/libqutim.so

%files -n jreen
%defattr(-,root,root)
%{_libdir}/libjreen.so.*

%files -n jreen-devel
%defattr(-,root,root)
%{_includedir}/jreen
%{_libdir}/pkgconfig/libjreen.pc
%{_libdir}/libjreen.so


%changelog
* Thu Jun 13 2012 Vladimir V. Lopatin <skyb.calista@gmail.com> 0.3.20120113git6a8a205-1.R
- Update to last revision

* Thu Dec 13 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.3.20111213gitf50a28a-1.R
- Update to last revision

* Thu Nov 14 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.3.20111114git7943460-1.R
- Update to last revision

* Thu Oct 27 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.3.20111028git9d9536b-1.R
- Update to last revision

* Thu Oct 27 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.3.20111027gitb2dfec3-1.R
- Update to last revision

* Wed Oct 26 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.3.20111026git7fbd44c-1.R
- Update to last revision
- Added some buildrequires

* Tue Oct 18 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.3.20111018gitaa4ae98-1.R
- Update to last revision
- Split package

* Tue Aug 16 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.3-1.gita4487a5.R
- Update to last revision

* Tue Aug 16 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.3-2.20110815git18f571a.R
- Added requires qca-cyrus-sasl

* Mon Aug 15 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.3-1.20110815git18f571a.R
- Update from git

* Fri Aug 12 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.3-1.20110811git5431b1f.R
- Initial release
