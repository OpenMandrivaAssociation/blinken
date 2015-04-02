%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Simon Says Game
Name:		blinken
Version:	15.03.97
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/blinken/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
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

%description
Blinken is the KDE version of the well-known game Simon Says.
Follow the pattern of sounds and lights as long as you can! Press the
start game button to begin. Watch the computer and copy the pattern it
makes. Complete the sequence in the right order to win.

%files
%doc AUTHORS
%{_datadir}/blinken
%{_kde_bindir}/blinken
%{_kde_iconsdir}/*/*/apps/blinken.*
%{_datadir}/applications/org.kde.blinken.desktop
%{_kde_datadir}/appdata/blinken.appdata.xml
%{_kde_datadir}/config.kcfg/blinken.kcfg
%{_kde_docdir}/HTML/*/blinken

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake -G Ninja
ninja

%install
DESTDIR="%{buildroot}" ninja install -C build
