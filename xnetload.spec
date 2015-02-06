Summary:	A program to display load on network device
Name:		xnetload
Version:	1.11.3
Release:	10
License:	GPLv2+
Group:		File tools
Url:		http://www.xs4all.nl/~rsmith/software/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		xnetload-1.11.3-flags.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)

%description
This application, that runs under the X Window System, displays a count
and a graph of the traffic over a specified network connection.

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

find . -perm 0400 | xargs chmod 0644

%build
%make depend
%make OPTFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
chmod 644 README
%makeinstall BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}/man1

