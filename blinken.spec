Summary:	Simon Says Game
Name:		blinken
Version:	4.10.5
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://edu.kde.org/blinken/
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
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

%changelog
* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2
- Update doc files

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0

* Thu Jul 19 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.97-1
- New version 4.8.97

* Mon Jul 02 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95

* Sat Jun 09 2012 Crispin Boylan <crisb@mandriva.org> 4.8.4-1
+ Revision: 803729
- New release

* Fri May 04 2012 Crispin Boylan <crisb@mandriva.org> 4.8.3-1
+ Revision: 796276
- New release

* Thu Apr 19 2012 Crispin Boylan <crisb@mandriva.org> 4.8.2-1
+ Revision: 792018
- New release

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.8.0-1
+ Revision: 762441
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758032
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744508
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.90-1
+ Revision: 739344
- New upstream tarball

* Sat Nov 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 731865
- New upstream tarball 4.7.80

* Mon Nov 07 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.41-1
+ Revision: 727114
- New version 4.7.41

* Mon Jul 11 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.6.90-1
+ Revision: 689480
- import blinken

