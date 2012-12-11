Name: xnetload
Summary: A program to display load on network device
Version: 1.11.3
Release: %mkrel 8
Source: %{name}-%{version}.tar.bz2
Patch: %{name}-install.patch
URL: http://www.xs4all.nl/~rsmith/software/
Group: File tools
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libxaw-devel
License: GPL

%description
This application, that runs under the X Window System, displays
a count and a graph of the traffic over a specified network
connection.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q
%patch -p1

%build
%make depend
%make

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{_mandir}/man1
chmod 644 README
%makeinstall BINDIR=$RPM_BUILD_ROOT/%{_bindir} MANDIR=$RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*




%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.11.3-8mdv2011.0
+ Revision: 615728
- the mass rebuild of 2010.1 packages

* Mon Apr 19 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.11.3-7mdv2010.1
+ Revision: 536810
- Remove name/version/release redefinitions
- Remove trailing whitespaces
- Fix BR (libaxaw-devel, not X11-devel)
- Use -q in %%setup
- Don't mkdir %%_menudir
- Don't manually bzme manpages

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 1.11.3-7mdv2010.0
+ Revision: 446259
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 1.11.3-6mdv2009.0
+ Revision: 262634
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.11.3-5mdv2009.0
+ Revision: 257603
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.11.3-3mdv2008.1
+ Revision: 136618
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 02 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.11.3-3mdv2007.0
+ Revision: 131163
- remove old menu entries
- rebuild against newer X libraries
- Import xnetload

* Sat May 14 2005 Emmanuel Blindauer <blindauer@mandriva.org> 1.11.3-2mdk
- modify patch0 for build on x86_64

* Fri Feb 18 2005 Emmanuel Blindauer <mdk@agat.net> 1.11.3-1mdk
- new version
- menu added

