Summary:	The Ultimate desktop environment
Name:		uwm
Version:	0.2.10
Release:	0.a.2
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/udeproject/%{name}-%{version}a.tar.gz
# Source0-md5:	1370418179f56612ffe63d6ed0c89d13
URL:		http://udeproject.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linuxberg (Tucows) says: UDE - The Unix Desktop Environment is more
then just another windows manager. Designed to compensate for the
shortcomings of many other similar packages, UDE features many
innovative improvements. The project does not use any special
GUI-Libraries such as QT or GTK+ and is based on the standard Xlibs
(also to make UDE faster).

%prep
%setup -q -n %{name}-%{version}a

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/uwm
%dir %{_datadir}/uwm
%dir %{_datadir}/%{name}/config
%attr(755,root,root) %{_datadir}/%{name}/config/StartScript
%attr(755,root,root) %{_datadir}/%{name}/config/StopScript

%{_datadir}/%{name}/config/appmenu
%{_datadir}/%{name}/config/mountmenu
%{_datadir}/%{name}/config/urdb

%{_datadir}/%{name}/config/uwmrc
%{_datadir}/%{name}/config/uwmrc-behaviour.hook
%{_datadir}/%{name}/config/uwmrc-layout.hook
%{_datadir}/%{name}/config/uwmrc-ws.hook

%dir %{_datadir}/%{name}/extras
%dir %{_datadir}/%{name}/extras/tools
%{_datadir}/%{name}/extras/tools/dirtomenu
%{_datadir}/%{name}/extras/tools/dirtomenu-recursive

%{_datadir}/%{name}/gfx
