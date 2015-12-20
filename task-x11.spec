Name:		task-x11
Version:	2015.0
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
Requires:	x11-server-xwayland
Requires:	xinit
Requires:	dri-drivers
# for debugging multimedia keyboard inet(common) (cf x11-data-xkbdata):
Suggests:	xev
# needed for locales cache
Requires:	x11-compose-cache

BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running X.org X11.

%prep

%build

%install

%files

