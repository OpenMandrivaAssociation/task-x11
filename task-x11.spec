Name:		task-x11
Version:	2015.0
Release:	14
Summary:	Metapackage for X.org X11
Group:		System/X11
License:	GPL
Requires:	xauth
Requires:	iceauth
Requires:	rgb
Requires:	x11-data-cursor-themes
Requires:	xhost
Recommends:	x11-driver-video
Recommends:	x11-driver-input
Requires:	x11-font-misc-misc
Requires:	x11-font-cursor-misc
Recommends:	fonts-ttf-dejavu
Recommends:	fonts-ttf-liberation
Requires:	x11-font-alias
Requires:	setxkbmap
Requires:	x11-server-xorg
Requires:	x11-server-xwayland
Requires:	xinit
Requires:	dri-drivers
# for debugging multimedia keyboard inet(common) (cf x11-data-xkbdata):
Recommends: xev

BuildArch:	noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running X.org X11.

%prep

%build

%install

%files

