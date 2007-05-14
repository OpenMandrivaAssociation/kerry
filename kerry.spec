%define __libtoolize    /bin/true

Name:           kerry
Version:        0.2.1
Release:        %mkrel 4
Summary:        Desktop search tool
License:        GPL
Group:          Graphical desktop/KDE
Source:         http://developer.kde.org/~binner/%{name}/%{name}-%{version}.tar.bz2
Patch0:		kerry-fr.patch
Patch1:		kerry-pt_BR.patch
BuildRequires:  kdebase-devel
BuildRequires:  libbeagle-devel >= 0.2.5
BuildRequires:  desktop-file-utils
URL:		http://en.opensuse.org/Kerry
Requires:	beagle
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A desktop search tool integrated with Beagle and KDE.

%prep
%setup -q 
%patch0 -p0
%patch1 -p1

%build
# new pot files. Need regenerate entries
make -f admin/Makefile.common

%configure2_5x

%make

%install
rm -rf %buildroot
%makeinstall_std

desktop-file-install --vendor="" \
  --add-only-show-in="KDE" \
  --remove-category="Application" \
  --remove-category="Utility" \
  --add-category="X-MandrivaLinux-System-FileTools" \
  --add-category="System" \
  --dir %buildroot%{_datadir}/applications/kde %buildroot%{_datadir}/applications/kde/kerry.desktop

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


