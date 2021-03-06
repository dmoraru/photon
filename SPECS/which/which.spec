Summary:	Program shows full path of (shell) commands
Name:		which
Version:	2.21
Release:	1%{?dist}
License:	GPLv3+
URL:		http://savannah.gnu.org/projects/which
Source0:	http://ftp.gnu.org/gnu/which/%{name}-%{version}.tar.gz
%define sha1 which=6b6bec3d2b3d4661c164feb81b9b1d22d1359ded
Group:		Development/Tools
Vendor:		VMware, Inc.
Distribution: Photon
%description
Program for showing the full the path of (shell) commands.
%prep
%setup -q
%build
./configure \
	--prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%files
%defattr(-,root,root)
%{_bindir}/*
/usr/share/info/*
%{_mandir}/man1/*
%changelog
*	Wed Jan 20 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.21-1
-	Update to 2.21-1.
*	Wed Oct 21 2014 Divya Thaluru <dthaluru@vmware.com> 2.20-1
-	Initial build. First version
