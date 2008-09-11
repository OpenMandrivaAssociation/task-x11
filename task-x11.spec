Name: task-x11
Version: 2009.0
Release: %mkrel 2
Summary: Metapackage for X.org X11
Group: System/X11
License: GPL
#
Requires: xauth
Requires: iceauth
Requires: rgb
Requires: x11-data-cursor-themes
Requires: xhost
#
Suggests: x11-driver-video
#
Requires: x11-font-misc-misc
Requires: x11-font-cursor-misc
Requires: fonts-ttf-dejavu
Requires: fonts-ttf-liberation
Requires: x11-font-alias
#
Requires: setxkbmap
Requires: xkbcomp
#
Requires: x11-server-xorg
#
Requires: xinit
#
# for debugging multimedia keyboard inet(common) (cf x11-data-xkbdata):
Suggests: xev


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running X.org X11.

%files

