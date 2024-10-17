Summary:	Memcached mysql UDFs (user defined functions) to work with libmemcached
Name:		memcached_functions_mysql
Version:	1.0
Release:	%mkrel 2
Group:		System/Servers
License:	BSD
URL:		https://tangent.org/
Source0:	http://download.tangent.org/%{name}-%{version}.tar.gz
Patch0:		memcached_functions_mysql-0.7-avoid-version.diff
Requires:	mysql
BuildRequires:	autoconf2.5
BuildRequires:	libtool
BuildRequires:	memcached-devel
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is the memcached mysql UDFs (user defined functions) to work with
libmemcached, Brian Aker's super duper new fast client library for memcached.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0

chmod 644 benchmarks/* sql/* utils/*

%build
autoreconf -fis

%configure2_5x \
    --libdir=%{_libdir}/mysql/plugin
%make

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -f %{buildroot}%{_libdir}/mysql/plugin/*.*a

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc benchmarks sql utils AUTHORS ChangeLog README
%{_libdir}/mysql/plugin/*.so
%{_mandir}/man3/*.3*

