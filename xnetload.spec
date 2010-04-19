Name: xnetload
Summary: A program to display load on network device
Version: 1.11.3
Release: %mkrel 7
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


