%define name    wmcalc
%define version 0.3
%define release %mkrel 6

Name:		%name
Version:	%version
Release:	%release
Summary:	Calculator dockapp for windowmaker
Url:		http://packages.debian.org/unstable/x11/wmcalc.html
Source:		http://ftp.debian.org/debian/pool/main/w/wmcalc/wmcalc_0.3.orig.tar.bz2
PAtch1:         %name-patch_other_locales.bz2
License:	GPL
Group:		Graphical desktop/Other
BuildRequires:	X11-devel libxpm-devel libx11-devel

%description
wmcalc is a small calculator meant for the WindowMaker dock or Afterstep
Wharf.  It is a simple calculator with basic functions and memory slots,
and can launch any external application for more complex calculations.

%prep
%setup -q -n %name-%version.orig
%patch1 -p1 -b .orig

%build
# (tv) fix build:
perl -pi -e 's!/usr/local/include!/usr/include/X11/!' Makefile
%make


%install
%__rm -rf %buildroot
%__install -D %name	%buildroot/usr/X11R6/bin/%name

%clean
%__rm -rf %buildroot


%files
%defattr(0644,root,root,0755)
%doc README .wmcalc
%defattr(0755,root,root,0755)
/usr/X11R6/bin/%name

