%define svn 874937

Name: kerry
Version: 0.2.90
Release: %mkrel 3
Summary: Desktop search tool
License: GPL
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://en.opensuse.org/Kerry
Source: http://developer.kde.org/~binner/%{name}/%{name}-%{version}.%svn.tar.bz2
Patch4: only_kde.patch 
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: kdebase4-devel
BuildRequires: openldap-devel
BuildRequires: libbeagle-devel >= 0.3.0
Requires: beagle

%description
A desktop search tool integrated with Beagle and KDE.

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

%files
%defattr(-,root,root)
%{_kde_bindir}/*
%{_kde_datadir}/applications/kde4/kerry.desktop
%{_kde_iconsdir}/hicolor/*/apps/*.png
%{_kde_iconsdir}/hicolor/*/apps/*.svgz

#--------------------------------------------------------------------

%prep
%setup -q  -n %name
%patch4 -p1

%build

%cmake_kde4

%make

%install
rm -rf %buildroot

%makeinstall_std -C build

%clean
rm -rf %buildroot
