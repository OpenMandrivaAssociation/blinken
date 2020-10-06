%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Simon Says Game
Name:		blinken
Version:	20.08.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/blinken/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(PythonInterp)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Crash)

%description
Blinken is the KDE version of the well-known game Simon Says.
Follow the pattern of sounds and lights as long as you can! Press the
start game button to begin. Watch the computer and copy the pattern it
makes. Complete the sequence in the right order to win.

%files -f %{name}.lang
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
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name}
