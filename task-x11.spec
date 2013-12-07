Name:		task-x11
Version:	%mandriva_release
Release:	9
Summary:	Metapackage for X.org X11
Group:		System/X11
License:	GPL
Requires:	xauth
Requires:	iceauth
Requires:	rgb
Requires:	x11-data-cursor-themes
Requires:	xhost
Suggests:	x11-driver-video
Suggests:	x11-driver-input
Requires:	x11-font-misc-misc
Requires:	x11-font-cursor-misc
Suggests:	fonts-ttf-dejavu
Suggests:	fonts-ttf-liberation
Requires:	x11-font-alias
Requires:	setxkbmap
Requires:	x11-server-xorg
Requires:	xinit
# for debugging multimedia keyboard inet(common) (cf x11-data-xkbdata):
Suggests:	xev

BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running X.org X11.

%prep

%build

%install

%files



%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 2011.0-2mdv2011.0
+ Revision: 670667
- mass rebuild

* Wed Dec 01 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2011.0-1mdv2011.0
+ Revision: 604468
- Change hardcoded version number for %%mandriva_release, which will change from
  2010.1 to 2011.0, so we can also reset "Release".

* Thu Apr 08 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2010.1-4mdv2010.1
+ Revision: 533012
- Suggest x11-driver-input too

* Wed Jan 06 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2010.1-3mdv2010.1
+ Revision: 486902
- Removed xkbcomp dependency (it's an indirect dependency now)

* Thu Dec 03 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2010.1-2mdv2010.1
+ Revision: 473031
- Obsolete task-x11_1.5

* Fri Nov 13 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2010.1-1mdv2010.1
+ Revision: 465891
- We're 2010.1 now

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 2009.0-5mdv2010.0
+ Revision: 423766
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2009.0-4mdv2009.1
+ Revision: 351483
- rebuild

* Tue Sep 16 2008 Frederic Crozat <fcrozat@mandriva.com> 2009.0-3mdv2009.0
+ Revision: 285294
- Replace hard requires by suggests on dejavu / liberation (Mdv bug #39761)

* Thu Sep 11 2008 Pixel <pixel@mandriva.com> 2009.0-2mdv2009.0
+ Revision: 283821
- allow to have task-x11 without the many video drivers (see #41060)

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 2009.0-1mdv2009.0
+ Revision: 226260
- bump version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2008.1-4mdv2009.0
+ Revision: 225642
- rebuild

* Thu Apr 03 2008 Pixel <pixel@mandriva.com> 2008.1-3mdv2008.1
+ Revision: 192082
- suggests xev instead of requiring it (#39729)

* Tue Jan 22 2008 Pixel <pixel@mandriva.com> 2008.1-2mdv2008.1
+ Revision: 156275
- add xev to allow debugging multimedia keyboard inet(common)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2008.1-1mdv2008.1
+ Revision: 98598
- new version (for mdv 2008.1)

* Thu Aug 30 2007 Frederic Crozat <fcrozat@mandriva.com> 2008.0-4mdv2008.0
+ Revision: 75336
- Enable dependency on fonts-ttf-liberation

* Fri Jul 06 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2008.0-3mdv2008.0
+ Revision: 49024
- removing xfs requirement since it was deprecated in favor
  of the new fontpath.d schema

* Mon May 21 2007 Thierry Vignaud <tv@mandriva.org> 2008.0-2mdv2008.0
+ Revision: 29316
- disable require fonts-ttf-liberation

* Mon May 21 2007 Thierry Vignaud <tv@mandriva.org> 2008.0-1mdv2008.0
+ Revision: 29242
- install fonts-ttf-liberation by default


* Wed Mar 21 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2007.1-2mdv2007.1
+ Revision: 147248
- Requires xhost (#25624)

* Tue Mar 20 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2007.1-1mdv2007.1
+ Revision: 146915
- Bump version for 2007.1
- Removed unneeded requires
- Added requires for video drivers (#26088)
- Import task-x11

* Sat Jun 24 2006 Frederic Crozat <fcrozat@mandriva.com> 2006-3mdv2007.0
- Add cursor theme dependency

* Wed May 24 2006 Pixel <pixel@mandriva.com> 2006-2mdk
- have xinit/startx always installed even if we use xdm/kdm/gdm

* Sat May 20 2006 Pixel <pixel@mandriva.com> 2006-1mdk
- package created for Mandriva
- minimal at the moment

