Name: kerry
Version: 0.2.1
Release: %mkrel 11
Summary: Desktop search tool
License: GPL
Group: Graphical desktop/KDE
URL: http://en.opensuse.org/Kerry
Source: http://developer.kde.org/~binner/%{name}/%{name}-%{version}.tar.bz2
Patch0:	kerry-fr.patch
Patch1:	kerry-pt_BR.patch
Patch2: kerry-no-indexing-on-battery.patch
Patch3: kerry-libbeagle-0.3.0.patch
BuildRequires: openldap-devel
BuildRequires: kdebase-devel
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

%build
# new pot files. Need regenerate entries
make -f admin/Makefile.common

%configure2_5x

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

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_libdir}/*kerry*
%_datadir/applications/kde/kcmbeagle.desktop
%_datadir/applnk/.hidden/kcmkerry.desktop

%{_datadir}/applications/kde/kerry.desktop
%{_datadir}/autostart/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/apps/kerry/search-running.mng


