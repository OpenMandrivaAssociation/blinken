#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Simon Says Game
Name:		plasma6-blinken
Version:	24.05.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/blinken/
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/blinken/-/archive/%{gitbranch}/blinken-%{gitbranchd}.tar.bz2#/blinken-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/blinken-%{version}.tar.xz
%endif
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(PythonInterp)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Crash)

%description
Blinken is the KDE version of the well-known game Simon Says.
Follow the pattern of sounds and lights as long as you can! Press the
start game button to begin. Watch the computer and copy the pattern it
makes. Complete the sequence in the right order to win.

%files -f blinken.lang
%doc AUTHORS
%{_bindir}/blinken
%{_iconsdir}/*/*/apps/blinken.*
%{_datadir}/blinken
%{_datadir}/metainfo/*.xml
%{_datadir}/config.kcfg/blinken.kcfg
%{_docdir}/HTML/*/blinken
%{_datadir}/applications/org.kde.blinken.desktop
#----------------------------------------------------------------------

%prep
%autosetup -p1 -n blinken-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang blinken
