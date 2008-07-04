Name: kerry
Version: 0.2.1
Release: %mkrel 14
Summary: Desktop search tool
License: GPL
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://en.opensuse.org/Kerry
Source: http://developer.kde.org/~binner/%{name}/%{name}-%{version}.tar.bz2
Patch0:	kerry-fr.patch
Patch1:	kerry-pt_BR.patch
Patch2: kerry-no-indexing-on-battery.patch
Patch3: kerry-libbeagle-0.3.0.patch
Patch4: only_kde.patch 
BuildRequires: openldap-devel
BuildRequires: kdebase3-devel
BuildRequires: libbeagle-devel >= 0.3.0
BuildRequires: desktop-file-utils
Requires: beagle

%description
A desktop search tool integrated with Beagle and KDE.

%prep
%setup -q 
%patch0 -p0
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1

%build
# new pot files. Need regenerate entries
make -f admin/Makefile.common

%configure_kde3

%make

%install
rm -rf %buildroot
%makeinstall_std

rm -f %buildroot/%{_prefix}/shutdown/beagled-shutdown.sh
%find_lang %{name}
%find_lang kcmbeagle
cat kcmbeagle.lang >> %{name}.lang

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%{_kde3_bindir}/*
%{_kde3_libdir}/kde3/*.so
%{_kde3_libdir}/kde3/*.la
%{_kde3_libdir}/*kerry*
%_kde3_datadir/applications/kde/kcmbeagle.desktop
%_kde3_datadir/applnk/.hidden/kcmkerry.desktop
%{_kde3_datadir}/applications/kde/kerry.desktop
%{_kde3_datadir}/autostart/*.desktop
%{_kde3_iconsdir}/hicolor/*/apps/*
%{_kde3_appsdir}/kerry/search-running.mng
%{_kde3_prefix}/shutdown/*

