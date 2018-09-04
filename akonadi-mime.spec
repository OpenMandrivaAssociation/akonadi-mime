Name:		akonadi-mime
# (tpg) add epoch to keep compatability with kdepimlibs
Epoch:		3
Version:	 18.08.1
Release:	1
Summary:	Akonadi Mime Integration
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/KDE
URL:		https://www.kde.org/
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Akonadi) >= 5.3.1
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	xsltproc
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(shared-mime-info)

%description
Akonadi Mime Integration.

%files -f libakonadi-kmime5.lang
%{_sysconfdir}/xdg/akonadi-mime.categories
%{_libdir}/qt5/plugins/akonadi_serializer_mail.so
%{_datadir}/akonadi/plugins/serializer/*
%{_bindir}/akonadi_benchmarker
%{_datadir}/config.kcfg/specialmailcollections.kcfg
%{_datadir}/mime/packages/x-vnd.kde.contactgroup.xml

#--------------------------------------------------------------------

%define major 5
%define libname %mklibname KF5AkonadiMime %{major}

%package -n %{libname}
Summary:      Akonadi Mime Integration main library
Group:        System/Libraries

%description -n %{libname}
Akonadi Mime Integration main library.

%files -n %{libname}
%{_libdir}/libKF5AkonadiMime.so.%{major}*

#--------------------------------------------------------------------

%define develname %mklibname KF5AkonadiMime -d

%package -n %{develname}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:       %{name} = %{EVRD}
Requires:       %{libname} = %{EVRD}
Obsoletes:      kdepimlibs-devel < 3:16.08.2
Provides:       kdepimlibs-devel = 3:%{version}

%description -n %{develname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{develname}
%{_includedir}/KF5/Akonadi/KMime/
%{_includedir}/KF5/akonadi/kmime/
%{_includedir}/KF5/*_version.h
%{_libdir}/*.so
%{_libdir}/cmake/KF5AkonadiMime/
%{_libdir}/qt5/mkspecs/modules/*.pri

#--------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libakonadi-kmime5
