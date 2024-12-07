#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Name:		plasma6-akonadi-mime
Version:	24.08.3
Release:	%{?git:0.%{git}.}2
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
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/akonadi-mime/-/archive/%{gitbranch}/akonadi-mime-%{gitbranchd}.tar.bz2#/akonadi-mime-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/akonadi-mime-%{version}.tar.xz
%endif

BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6Mime)
BuildRequires:	xsltproc
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(shared-mime-info)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

%description
Akonadi Mime Integration.

%files -f libakonadi-kmime6.lang
%{_datadir}/qlogging-categories6/akonadi-mime.categories
%{_libdir}/qt6/plugins/akonadi_serializer_mail.so
%{_datadir}/akonadi/plugins/serializer/*
%{_bindir}/akonadi_benchmarker
%{_datadir}/config.kcfg/specialmailcollections.kcfg
%{_datadir}/mime/packages/x-vnd.kde.contactgroup.xml

#--------------------------------------------------------------------

%define major 6
%define libname %mklibname KPim6AkonadiMime

%package -n %{libname}
Summary:      Akonadi Mime Integration main library
Group:        System/Libraries
Requires:	%{name} >= %{EVRD}

%description -n %{libname}
Akonadi Mime Integration main library.

%files -n %{libname}
%{_libdir}/libKPim6AkonadiMime.so*

#--------------------------------------------------------------------

%define develname %mklibname KPim6AkonadiMime -d

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
%{_includedir}/KPim6/AkonadiMime
%{_libdir}/cmake/KPim6AkonadiMime/

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n akonadi-mime-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libakonadi-kmime6
