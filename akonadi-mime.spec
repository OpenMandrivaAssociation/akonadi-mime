Name:		akonadi-mime
# (tpg) add epoch to keep compatability with kdepimlibs
Epoch:		3
Version:	23.08.1
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
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz

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
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

%description
Akonadi Mime Integration.

%files -f libakonadi-kmime5.lang
%{_datadir}/qlogging-categories5/akonadi-mime.categories
%{_libdir}/qt5/plugins/akonadi_serializer_mail.so
%{_datadir}/akonadi/plugins/serializer/*
%{_bindir}/akonadi_benchmarker
%{_datadir}/config.kcfg/specialmailcollections.kcfg
%{_datadir}/mime/packages/x-vnd.kde.contactgroup.xml

#--------------------------------------------------------------------

%define major 5
%define oldlibname %mklibname KF5AkonadiMime 5
%define libname %mklibname KPim5AkonadiMime

%package -n %{libname}
Summary:      Akonadi Mime Integration main library
Group:        System/Libraries
Requires:	%{name} >= %{EVRD}
%rename %{oldlibname}

%description -n %{libname}
Akonadi Mime Integration main library.

%files -n %{libname}
%{_libdir}/libKPim5AkonadiMime.so.%{major}*

#--------------------------------------------------------------------

%define olddevelname %mklibname KF5AkonadiMime -d
%define develname %mklibname KPim5AkonadiMime -d

%package -n %{develname}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:       %{name} = %{EVRD}
Requires:       %{libname} = %{EVRD}
Obsoletes:      kdepimlibs-devel < 3:16.08.2
Provides:       kdepimlibs-devel = 3:%{version}
%rename %{olddevelname}

%description -n %{develname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{develname}
%{_includedir}/KPim5/AkonadiMime
%{_libdir}/*.so
%{_libdir}/cmake/KPim5AkonadiMime/
%{_libdir}/cmake/KF5AkonadiMime/
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/*.{tags,qch}

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libakonadi-kmime5
