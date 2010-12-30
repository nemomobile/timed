Name:     timed
Version:  2.32
Release:  1
Summary:  Time daemon
Group:    System/System Control
License:  LGPLv2
URL:      http://meego.gitorious.org/meego-middleware/timed
Source0:  %{name}-%{version}.tar.bz2
Source1:  %{name}.init
Source2:  %{name}.conf
Patch1:   %{name}-2.11-run-as-system-service.patch
Patch2:   %{name}-2.27-enable-creds.patch
Patch3:   %{name}-2.27-debugflag-fix.patch
Patch5:   %{name}-2.27-typofix.patch
Patch6:   %{name}-2.31-add-missing-if.patch

BuildRequires: pkgconfig(contextprovider-1.0)
BuildRequires: pkgconfig(dsme_dbus_if)
BuildRequires: pkgconfig(libpcrecpp)
BuildRequires: pkgconfig(QtCore) >= 4.6
BuildRequires: asciidoc
BuildRequires: dblatex
BuildRequires: docbook-style-xsl
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: libcreds2-devel
BuildRequires: libiodata-devel
BuildRequires: libqmlog-devel >= 0.0.9
BuildRequires: libxslt
BuildRequires: python >= 2.5

Requires: tzdata

%description
The time daemon (%{name}) managing system time, time zone and settings,
executing actions at given time and managing the event queue.

%package devel
Summary:  Development package for %{name}
Group:    Development/Libraries
Requires: pkgconfig(QtCore) >= 4.6
Requires: %{name} = %{version}-%{release}

%description devel
Header files and shared lib symlink for %{name}.

%package tests
Summary:  Test cases for %{name}
Group:    Development/System
Requires: testrunner-lite
Requires: %{name}-tools = %{version}-%{release}

%description tests
Simple automated test cases, to be executed in cita.

%package tools
Summary:  Command line tools for communication with the time daemon
Group:    Development/Tools
Requires: %{name} = %{version}-%{release}

%description tools
Command line timed tools: 'simple-client' - a command line
simple client for time daemon; 'fake-dialog-ui' - a command
line voland implementation; 'ticker' - a command line clock
and signal notification.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1

%build
mkdir -p src/h
ln -s ../server src/h/daemon
ln -s ../lib    src/h/timed
ln -s ../voland src/h/timed-voland
cd src
%qmake -recursive "CONFIG += MEEGO"
make %{?_smp_mflags}

%install
%qmake_install -C src
cd src/political
INSTALL_ROOT=%{buildroot} ./debian-install.sh
cd ../..
ln -s %{_bindir}/%{name} %{buildroot}/%{_bindir}/cute-timed
install -m 644 -D src/doc/timed.8 %{buildroot}/%{_mandir}/man8/timed.8
install -m 644 -D src/doc/libtimed.3 %{buildroot}/%{_mandir}/man3/libtimed.3
install -m 644 src/doc/libtimed-voland.3 %{buildroot}/%{_mandir}/man3/libtimed-voland.3

install -D %{SOURCE1} %{buildroot}/%{_sysconfdir}/rc.d/init.d/%{name}
install -m 644 -D %{SOURCE2} %{buildroot}/%{_sysconfdir}/dbus-1/system.d/%{name}.conf
install -d %{buildroot}/%{_localstatedir}/cache/%{name}/

%post
/sbin/ldconfig
/sbin/chkconfig --add %{name}

%preun
if [ $1 = 0 ]; then
  /sbin/service %{name} stop > /dev/null 2>&1
  /sbin/chkconfig --del %{name}
fi

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING debian/changelog debian/copyright
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/%{name}.conf
%{_sysconfdir}/rc.d/init.d/%{name}
%{_sysconfdir}/osso-cud-scripts/timed-clear-device.sh
%{_sysconfdir}/osso-rfs-scripts/timed-restore-original-settings.sh
%{_bindir}/cute-timed
%{_bindir}/%{name}
%{_libdir}/libtimed.so.*
%{_libdir}/libtimed-voland.so.*
%{_datadir}/backup-framework/applications/timedbackup.conf
%{_datadir}/contextkit/providers/com.nokia.time.context
%{_mandir}/man3/libtimed.3.gz
%{_mandir}/man3/libtimed-voland.3.gz
%{_mandir}/man8/timed.8.gz
%{_datadir}/%{name}/typeinfo/*.type
%{_datadir}/tzdata-timed/*.data
%{_datadir}/zoneinfo/Mobile/UTC*
%{_localstatedir}/cache/timed/

%files devel
%defattr(-,root,root,-)
%doc COPYING
%{_includedir}/%{name}/*
%{_includedir}/timed-voland/*
%{_libdir}/libtimed.so
%{_libdir}/libtimed-voland.so
%{_libdir}/pkgconfig/timed.pc
%{_libdir}/pkgconfig/timed-voland.pc
%{_datadir}/qt4/mkspecs/features/timed.prf
%{_datadir}/qt4/mkspecs/features/timed-voland.prf

%files tests
%defattr(-,root,root,-)
%doc COPYING
%{_datadir}/%{name}-tests/tests.xml

%files tools
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/fake-dialog-ui
%{_bindir}/logging-test
%{_bindir}/logging-test.launch
%{_bindir}/ntp-helper
%{_bindir}/memory
%{_bindir}/qmtime-users.sh
%{_bindir}/simple-client
%{_bindir}/ticker
