%define		_modname	lithium
Summary:	Server-side deathmatch modification for Quake II
Name:		quake2-mod-%{_modname}
Version:	1.24
Release:	0.1
License:	?
Group:		Applications/Games
# Source0Download:	http://asp.planetquake.com/dl/dl.asp?lithium/lithium2_%{version}-i386-unknown-linux2.0.tar.gz
Source0:	lithium2_%{version}-i386-unknown-linux2.0.tar.gz
# NoSource0-md5:	9b84269fb49d208598d1658226e4135e
NoSource:	0
# Source1Download:	http://asp.planetquake.com/dl/dl.asp?lithium/lithium2_%{version}-axp-unknown-linux2.0.tar.gz
Source1:	lithium2_%{version}-axp-unknown-linux2.0.tar.gz
# NoSource1-md5:	-
NoSource:	1
URL:		http://lithium.planetquake.gamespy.com/
Requires:	quake2-common
ExclusiveArch:	%{ix86} alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamelibdir	%{_libdir}/quake2

%ifarch %{ix86}
%define		qarch	i386
%else
%ifarch alpha
%define		qarch	axp
%else
%define		qarch	%{nil}
%endif
%endif

%description
Lithium II is a very configurable server-side deathmatch modification
for Quake II. It adds many features and options to the game, while not
requiring clients to download anything special.

%prep
%setup -qcT
%ifarch %{ix86}
%{__tar} xzf %{SOURCE0}
%endif
%ifarch alpha
%{__tar} xzf %{SOURCE1}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamelibdir}/%{_modname}
cd lithium
install game%{qarch}.so $RPM_BUILD_ROOT%{_gamelibdir}/%{_modname}
cp -a admin.lst ctf.lst maps.lst $RPM_BUILD_ROOT%{_gamelibdir}/%{_modname}
cp -a lithctf.cfg lithium.cfg procket.cfg stock.cfg stockctf.cfg $RPM_BUILD_ROOT%{_gamelibdir}/%{_modname}
cp -a lithium2.qst $RPM_BUILD_ROOT%{_gamelibdir}/%{_modname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lithium/*.txt
%dir %{_gamelibdir}/%{_modname}
%{_gamelibdir}/%{_modname}/*.lst
%{_gamelibdir}/%{_modname}/*.cfg
%{_gamelibdir}/%{_modname}/*.qst
%attr(755,root,root) %{_gamelibdir}/%{_modname}/game%{qarch}.so
