%define version 2.0.2
%define rel     3
%define release %mkrel %rel

Summary:	The GNU Image Manipulation Program
Name:		gimp-data-extras
Version:	%version
Release:	%release
License:	GPL
Group:		Graphics
URL:		https://www.gimp.org/
Source0:	ftp://ftp.gimp.org/pub/gimp/extras/gimp-data-extras-%{PACKAGE_VERSION}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
#BuildRequires:	gimp2-devel
#Requires:	gimp2_0
Requires:	gimp > 2
BuildRequires:	gimp-devel

%description
Patterns, gradients etc. for gimp. This package isn't required, but contains
lots of goodies for gimp.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall GIMP_DATA_DIR=$RPM_BUILD_ROOT/%{_datadir}/gimp/2.0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc README NEWS
%{_datadir}/gimp/*




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-3mdv2011.0
+ Revision: 618945
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 2.0.2-2mdv2010.0
+ Revision: 437692
- rebuild

* Tue Jan 13 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.0.2-1mdv2009.1
+ Revision: 329006
- update to new version 2.0.2

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.0.1-5mdv2009.0
+ Revision: 140737
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 2.0.1-5mdv2008.0
+ Revision: 43119
- fix URL


* Fri Jan 13 2006 Eskild Hustvedt <eskild@mandriva.org> 2.0.1-4mdk
- Fixed deps

* Fri Dec 02 2005 Eskild Hustvedt <eskild@mandriva.org> 2.0.1-3mdk
- Fixed support for gimp 2.x
- mkrel

* Thu Nov 11 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.1-2mdk
- fix deps

* Wed Nov 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.0.1-1mdk
- new release

* Tue Jun 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2.0-8mdk
- fix buildrequires
- wipe out buildroot before installing
- cosmetics

* Thu Sep 04 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.2.0-7mdk
- fix buildrequires for 64bit ports

* Thu Jul 24 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.2.0-6mdk
- rebuil
- adjusted buildrequires so that we get the correct gimp-devel (not 1.3)
- quiet setup

