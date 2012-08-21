Summary:	Utilities for monitoring your system and processes on your system
Name:		procps
Version:	3.3.2
Release:	3
Epoch:		1
License:	GPL
Group:		Applications/System
# http://gitorious.org/procps/procps/archive-tarball/v3.3.2
Source0:	%{name}-%{name}-v%{version}.tar.gz
# Source0-md5:	89fca32782f9174cf03b5b6b0f76c5ad
URL:		http://gitorious.org/procps/
BuildRequires:	ncurses-devel
Requires(post):	/sbin/ldconfig
Requires:	fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The procps package contains a set of system utilities which provide
system information. Procps includes ps, free, skill, snice, tload,
top, uptime, vmstat, w and watch. The ps command displays a snapshot
of running processes. The top command provides a repetitive update of
the statuses of running processes. The free command displays the
amounts of free and used memory on your system. The skill command
sends a terminate command (or another specified signal) to a specified
set of processes. The snice command is used to change the scheduling
priority of specified processes. The tload command prints a graph of
the current system load average to a specified tty. The uptime command
displays the current time, how long the system has been running, how
many users are logged on and system load averages for the past one,
five and fifteen minutes. The w command displays a list of the users
who are currently logged on and what they're running. The watch
program watches a running program. The vmstat command displays virtual
memory statistics about processes, memory, paging, block I/O, traps
and CPU activity.

%package devel
Summary:	libproc header files
License:	LGPL
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
libproc header files.

%prep
%setup -qn %{name}-%{name}

sed -i -e "s#usrbin_execdir=.*#usrbin_execdir='\${bindir}'#g" configure.ac

%build
po/update-potfiles
%{__autopoint}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="-I%{_includedir}/ncurses"	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# kill is packaged in util-linux
%{__rm} $RPM_BUILD_ROOT%{_bindir}/kill
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/kill.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/ps
%attr(755,root,root) %{_sbindir}/sysctl
%attr(755,root,root) %{_bindir}/free
%attr(755,root,root) %{_bindir}/pgrep
%attr(755,root,root) %{_bindir}/pkill
%attr(755,root,root) %{_bindir}/pmap
%attr(755,root,root) %{_bindir}/pwdx
%attr(755,root,root) %{_bindir}/skill
%attr(755,root,root) %{_bindir}/slabtop
%attr(755,root,root) %{_bindir}/snice
%attr(755,root,root) %{_bindir}/tload
%attr(755,root,root) %{_bindir}/top
%attr(755,root,root) %{_bindir}/uptime
%attr(755,root,root) %{_bindir}/vmstat
%attr(755,root,root) %{_bindir}/w
%attr(755,root,root) %{_bindir}/watch

%attr(755,root,root) %ghost %{_libdir}/libprocps.so.?
%attr(755,root,root) %{_libdir}/libprocps.so.*.*.*

%{_mandir}/man1/free.1*
%{_mandir}/man1/pgrep.1*
%{_mandir}/man1/pkill.1*
%{_mandir}/man1/pmap.1*
%{_mandir}/man1/ps.1*
%{_mandir}/man1/pwdx.1*
%{_mandir}/man1/skill.1*
%{_mandir}/man1/slabtop.1*
%{_mandir}/man1/snice.1*
%{_mandir}/man1/tload.1*
%{_mandir}/man1/top.1*
%{_mandir}/man1/uptime.1*
%{_mandir}/man1/w.1*
%{_mandir}/man1/watch.1*
%{_mandir}/man5/sysctl.conf.5*
%{_mandir}/man8/sysctl.8*
%{_mandir}/man8/vmstat.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libprocps.so
%{_includedir}/proc
%{_pkgconfigdir}/libprocps.pc

