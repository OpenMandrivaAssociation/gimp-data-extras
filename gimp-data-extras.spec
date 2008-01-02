%define version 2.0.1
%define rel     5
%define release %mkrel %rel

Summary:	The GNU Image Manipulation Program
Name:		gimp-data-extras
Version:	%version
Release:	%release
License:	GPL
Group:		Graphics
URL:		http://www.gimp.org/
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


