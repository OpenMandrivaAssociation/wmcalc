Name:		wmcalc
Version:	0.7
Release:	1
Summary:	Calculator dockapp for windowmaker
Url:		http://packages.debian.org/unstable/x11/wmcalc.html
Source:		http://ftp.debian.org/debian/pool/main/w/wmcalc/wmcalc_%{version}.orig.tar.gz
#PAtch1:         %name-patch_other_locales.bz2
License:	GPL
Group:		Graphical desktop/Other
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)

%description
wmcalc is a small calculator meant for the WindowMaker dock or Afterstep
Wharf.  It is a simple calculator with basic functions and memory slots,
and can launch any external application for more complex calculations.

%prep
%setup -q -n %name-%version.orig
#patch1 -p1 -b .orig

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



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 0.3-11mdv2011.0
+ Revision: 634781
- simplify  BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.3-10mdv2010.0
+ Revision: 434774
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.3-9mdv2009.0
+ Revision: 262016
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.3-8mdv2009.0
+ Revision: 256042
- rebuild
- fix no-buildroot-tag
- fix spacing at top of description

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 0.3-6mdv2008.1
+ Revision: 135832
- fix build
- BR libx11-devel
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import wmcalc


* Mon Jan 02 2006 Lenny Cartier <lenny@mandriva.com> 0.3-6mdk
- rebuild

* Fri Oct 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.3-5mdk
- rebuild

* Wed Sep 24 2003 Han Boetes <han@linux-mandrake.com> 0.3-4mdk
- Added patch to fix other locales: qa.mandrakesoft.com/show_bug.cgi?id=5923
- Cleanups

* Fri Apr 25 2003 Han Boetes <han@linux-mandrake.com> 0.3-3mdk
- Stephans magic bot found some missing deps.
- Few more minor cleanups

* Fri Dec 27 2002 Han Boetes <han@linux-mandrake.com> 0.3-2mdk
- rebuild because of new rpm macros and new glibc

* Sun Jun  9 2002 Han Boetes <han@mijncomputer.nl> 0.3-1mdk
- Initial mdk release.
