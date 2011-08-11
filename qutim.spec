%global gitdate 20110811
%global gitcommit 6f9eed4
#git rev-parse --short HEAD

Name:           qutim
Version:        0.3
Release:        1.%{gitdate}git%{gitcommit}%{?dist}.R
Summary:        Multiprotocol (ICQ, Jabber, IRC etc) instant messenger with modern Qt4 interface
Summary(ru):    Мультиплатформенный, мультипротокольный (ICQ, Jabber, IRC...) мессенджер на QT4

License:        GPLv2+ and CC-BY-SA
URL:            http://www.qutim.org/
Source0:        %{name}-%{version}-git%{gitdate}.tar.xz

BuildRequires:  cmake >= 2.6, desktop-file-utils, qca2-devel
BuildRequires:  qt-devel >= 1:4.0, libidn-devel, dos2unix, qt-webkit-devel         

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
%{cmake} .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc



%changelog
