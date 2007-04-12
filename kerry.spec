Name:           kerry
Version:        0.2.1
Release:        %mkrel 3
Summary:        Desktop search tool
License:        GPL
Group:          Graphical desktop/KDE
Source:         http://developer.kde.org/~binner/%{name}/%{name}-%{version}.tar.bz2
Patch0:		kerry-fr.patch
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
%build
./configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

desktop-file-install --vendor="" \
  --add-only-show-in="KDE" \
  --remove-category="Application" \
  --remove-category="Utility" \
  --add-category="X-MandrivaLinux-System-FileTools" \
  --add-category="System" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications/kde $RPM_BUILD_ROOT%{_datadir}/applications/kde/kerry.desktop

#install -d $RPM_BUILD_ROOT%{_menudir}
#kdedesktop2mdkmenu.pl %{name} "Office/Accessories" $RPM_BUILD_ROOT%{_datadir}/applications/kde/*.desktop $RPM_BUILD_ROOT%{_menudir}/%{name}

rm -f $RPM_BUILD_ROOT/%{_prefix}/shutdown/beagled-shutdown.sh
%find_lang %{name}
%find_lang kcmbeagle
cat kcmbeagle.lang >> %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
%if %mdkversion > 200600
%update_icon_cache hicolor
%endif

%postun
%{clean_menus}
%if %mdkversion > 200600
%clean_icon_cache hicolor
%endif


%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_libdir}/*kerry*
%_datadir/applications/kde/kcmbeagle.desktop
%_datadir/applnk/.hidden/kcmkerry.desktop
#%_menudir/*

%{_datadir}/applications/kde/kerry.desktop
%{_datadir}/autostart/*.desktop
%{_iconsdir}/hicolor/*/apps/*
# %{_prefix}/shutdown/beagled-shutdown.sh
%{_datadir}/apps/kerry/search-running.mng


