Name: libvhdi
Version: 20160108
Release: 1
Summary: Library to access the Virtual Hard Disk (VHD) image format
Group: System Environment/Libraries
License: LGPL
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libvhdi/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
              
              

%description
libvhdi is a library to access the Virtual Hard Disk (VHD) image format

%package devel
Summary: Header files and libraries for developing applications for libvhdi
Group: Development/Libraries
Requires: libvhdi = %{version}-%{release}

%description devel
Header files and libraries for developing applications for libvhdi.

%package tools
Summary: Several tools for reading Virtual Hard Disk (VHD) image files
Group: Applications/System
Requires: libvhdi = %{version}-%{release}  fuse-libs
BuildRequires: fuse-devel

%description tools
Several tools for reading Virtual Hard Disk (VHD) image files

%package python
Summary: Python 2 bindings for libvhdi
Group: System Environment/Libraries
Requires: libvhdi = %{version}-%{release} python
BuildRequires: python-devel

%description python
Python 2 bindings for libvhdi

%package python3
Summary: Python 3 bindings for libvhdi
Group: System Environment/Libraries
Requires: libvhdi = %{version}-%{release} python3
BuildRequires: python3-devel

%description python3
Python 3 bindings for libvhdi

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir} --enable-python2 --enable-python3
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_instal

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvhdi.pc
%{_includedir}/*
%{_mandir}/man3/*

%files tools
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_bindir}/vhdiinfo
%attr(755,root,root) %{_bindir}/vhdimount
%{_mandir}/man1/*

%files python
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/python2*/site-packages/*.a
%{_libdir}/python2*/site-packages/*.la
%{_libdir}/python2*/site-packages/*.so

%files python3
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/python3*/site-packages/*.a
%{_libdir}/python3*/site-packages/*.la
%{_libdir}/python3*/site-packages/*.so

%changelog
* Fri Jan  8 2016 Joachim Metz <joachim.metz@gmail.com> 20160108-1
- Auto-generated

