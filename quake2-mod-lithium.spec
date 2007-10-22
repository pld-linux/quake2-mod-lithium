%define		_modname	lithium
Summary:	Server-side deathmatch modification for Quake II
Name:		quake2-mod-%{_modname}
Version:	1.24
Release:	0.1
License:	?
Group:		Applications/Games
# Source0Download:	http://asp.planetquake.com/dl/dl.asp?lithium/lithium2_1.24-i386-unknown-linux2.0.tar.gz
Source0:	lithium2_%{version}-i386-unknown-linux2.0.tar.gz
# NoSource0-md5:	9b84269fb49d208598d1658226e4135e
NoSource:	0
URL:		http://lithium.planetquake.gamespy.com/
Requires:	quake2-common
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamelibdir	%{_libdir}/quake2
%define		_gamedatadir	%{_datadir}/quake2
%define		_gamehomedir	/var/games/quake2

# because of gl_image.c:1559
%define		specflags	-fno-strict-aliasing

%description
Lithium II is a very configurable server-side deathmatch modification
for Quake II. It adds many features and options to the game, while not
requiring clients to download anything special.

%prep
%setup -q -n %{_modname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamelibdir}/%{_modname}
install game*.so $RPM_BUILD_ROOT%{_gamelibdir}/%{_modname}
cp -a admin.lst ctf.lst maps.lst $RPM_BUILD_ROOT%{_gamelibdir}/%{_modname}
cp -a lithctf.cfg lithium.cfg procket.cfg stock.cfg stockctf.cfg $RPM_BUILD_ROOT%{_gamelibdir}/%{_modname}
cp -a lithium2.qst $RPM_BUILD_ROOT%{_gamelibdir}/%{_modname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%dir %{_gamelibdir}/%{_modname}
%{_gamelibdir}/%{_modname}/*.lst
%{_gamelibdir}/%{_modname}/*.cfg
%{_gamelibdir}/%{_modname}/*.qst
%attr(755,root,root) %{_gamelibdir}/%{_modname}/game*.so
