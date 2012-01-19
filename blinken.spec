Name: blinken
Summary: Simon Says Game
Version: 4.8.0
Release: 1
Group: Graphical desktop/KDE
License: GPLv2
URL: http://edu.kde.org/blinken/
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}

%description
Blinken is the KDE version of the well-known game Simon Says.
Follow the pattern of sounds and lights as long as you can! Press the
start game button to begin. Watch the computer and copy the pattern it
makes. Complete the sequence in the right order to win.

%files
%doc AUTHORS Changelog
%_kde_appsdir/blinken
%_kde_bindir/blinken
%_kde_iconsdir/*/*/apps/blinken.*
%_kde_datadir/applications/kde4/blinken.desktop
%_kde_datadir/config.kcfg/blinken.kcfg
%_kde_docdir/HTML/*/blinken

#----------------------------------------------------------------------

%prep
%setup -q 

%apply_patches

%build

%cmake_kde4	
%make

%install
%makeinstall_std -C build
