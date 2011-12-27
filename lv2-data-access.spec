Summary:	LV2 Data Access extension - access to LV2_Descriptor::extension_data()
Summary(pl.UTF-8):	Rozszerzenie LV2 Data Access - dostęp do LV2_Descriptor::extension::data()
Name:		lv2-data-access
Version:	1.4
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	e8bb5e5d3cd3ac05c5b78565f3c4ec66
URL:		http://lv2plug.in/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
Requires:	lv2core >= 6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 Data Access extension defines a method for (e.g.) plugin UIs to
have (possibly marshalled) access to the
LV2_Descriptor::extension_data() function on a plugin instance.

%description -l pl.UTF-8
Rozszerzenie LV2 Data Access definiuje metodę dla (przykładowo)
interfejsów użytkownika wtyczek, pozwalającą im na dostęp do funkcji
LV2_Descriptor::extension_data() z instancji wtyczki.

%package devel
Summary:	Header file for LV2 Data Access extension
Summary(pl.UTF-8):	Plik nagłówkowy rozszerzenia LV2 Data Access
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lv2core-devel >= 6.0

%description devel
Header file for LV2 Data Access extension.

%description devel -l pl.UTF-8
Plik nagłówkowy rozszerzenia LV2 Data Access.

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%dir %{_libdir}/lv2/data-access.lv2
%{_libdir}/lv2/data-access.lv2/data-access.ttl
%{_libdir}/lv2/data-access.lv2/manifest.ttl

%files devel
%defattr(644,root,root,755)
%{_libdir}/lv2/data-access.lv2/data-access.h
%{_includedir}/lv2/lv2plug.in/ns/ext/data-access
%{_pkgconfigdir}/lv2-lv2plug.in-ns-ext-data-access.pc
