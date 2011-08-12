%global gitdate 20110811
%global gitcommit 5431b1f
#git rev-parse --short HEAD

Name:           qutim
Version:        0.3
Release:        1.%{gitdate}git%{gitcommit}%{?dist}.R
Summary:        Multiprotocol (ICQ, Jabber, IRC etc) instant messenger with modern Qt4 interface
Summary(ru):    Мультиплатформенный, мультипротокольный (ICQ, Jabber, IRC...) мессенджер на QT4

License:        GPLv2+ and CC-BY-SA
URL:            http://www.qutim.org/
Source0:        %{name}-%{version}-git%{gitcommit}.tar.xz

BuildRequires:  cmake >= 2.6, desktop-file-utils, qca2-devel
BuildRequires:  qt-devel >= 1:4.0, libidn-devel, dos2unix, qt-webkit-devel         
BuildRequires:  chrpath
#BuildRequires:  aspell-devel, libpurple-devel

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


%doc

%files devel
%{_includedir}/jreen
%{_includedir}/%{name}
%{_datadir}/cmake/Modules/*

%changelog
