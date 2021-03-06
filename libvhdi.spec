Name: libvhdi
Version: 20200810
Release: 1
Summary: Library to access the Virtual Hard Disk (VHD) image format
Group: System Environment/Libraries
License: LGPL
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libvhdi
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
             
BuildRequires: gcc             

%description -n libvhdi
Library to access the Virtual Hard Disk (VHD) image format

%package -n libvhdi-static
Summary: Library to access the Virtual Hard Disk (VHD) image format
Group: Development/Libraries
Requires: libvhdi = %{version}-%{release}

%description -n libvhdi-static
Static library version of libvhdi.

%package -n libvhdi-devel
Summary: Header files and libraries for developing applications for libvhdi
Group: Development/Libraries
Requires: libvhdi = %{version}-%{release}

%description -n libvhdi-devel
Header files and libraries for developing applications for libvhdi.

%package -n libvhdi-python2
Obsoletes: libvhdi-python < %{version}
Provides: libvhdi-python = %{version}
Summary: Python 2 bindings for libvhdi
Group: System Environment/Libraries
Requires: libvhdi = %{version}-%{release} python2
BuildRequires: python2-devel

%description -n libvhdi-python2
Python 2 bindings for libvhdi

%package -n libvhdi-python3
Summary: Python 3 bindings for libvhdi
Group: System Environment/Libraries
Requires: libvhdi = %{version}-%{release} python3
BuildRequires: python3-devel

%description -n libvhdi-python3
Python 3 bindings for libvhdi

%package -n libvhdi-tools
Summary: Several tools for reading Virtual Hard Disk (VHD) image files
Group: Applications/System
Requires: libvhdi = %{version}-%{release} fuse-libs
BuildRequires: fuse-devel

%description -n libvhdi-tools
Several tools for reading Virtual Hard Disk (VHD) image files

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir} --enable-python2 --enable-python3
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -n libvhdi
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/*.so.*

%files -n libvhdi-static
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/*.a

%files -n libvhdi-devel
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvhdi.pc
%{_includedir}/*
%{_mandir}/man3/*

%files -n libvhdi-python2
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/python2*/site-packages/*.a
%{_libdir}/python2*/site-packages/*.la
%{_libdir}/python2*/site-packages/*.so

%files -n libvhdi-python3
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/python3*/site-packages/*.a
%{_libdir}/python3*/site-packages/*.la
%{_libdir}/python3*/site-packages/*.so

%files -n libvhdi-tools
%defattr(644,root,root,755)
%license COPYING COPYING.LESSER
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Aug 10 2020 Joachim Metz <joachim.metz@gmail.com> 20200810-1
- Auto-generated

