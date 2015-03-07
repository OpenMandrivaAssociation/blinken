%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Simon Says Game
Name:		blinken
Version:	14.12.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/blinken/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel

%description
Blinken is the KDE version of the well-known game Simon Says.
Follow the pattern of sounds and lights as long as you can! Press the
start game button to begin. Watch the computer and copy the pattern it
makes. Complete the sequence in the right order to win.

%files
%doc AUTHORS
%{_kde_appsdir}/blinken
%{_kde_bindir}/blinken
%{_kde_iconsdir}/*/*/apps/blinken.*
%{_kde_applicationsdir}/blinken.desktop
%{_kde_datadir}/appdata/blinken.appdata.xml
%{_kde_datadir}/config.kcfg/blinken.kcfg
%{_kde_docdir}/HTML/*/blinken

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
