Summary:	EFI Boot Manager
Summary(pl.UTF-8):	Boot Manager dla EFI
Name:		efibootmgr
Version:	0.11.0
Release:	2
License:	GPL v2+
Group:		Base
#Source0:	http://linux.dell.com/efibootmgr/permalink/%{name}-%{version}.tar.gz
Source0:	https://github.com/rhinstaller/efibootmgr/archive/%{name}-%{version}.tar.gz
# Source0-md5:	3732e841bb644df71500971910420267
Patch0:		%{name}-efivar.patch
URL:		http://linux.dell.com/projects.shtml#efibootmgr
BuildRequires:	efivar-devel
BuildRequires:	pciutils-devel
ExclusiveArch:	%{ix86} %{x8664} ia64 x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
efibootmgr displays and allows the user to edit the Intel Extensible
Firmware Interface (EFI) Boot Manager variables. Additional
information about EFI can be found at
<http://developer.intel.com/technology/efi/efi.htm>.

%description -l pl.UTF-8
efibootmgr wyświetla i pozwala modyfikować wartości Boot Managera
EFI (Extensible Firmware Interface) Intela. Dodatkowe informacje o EFI
można znaleźć pod adresem
<http://developer.intel.com/technology/efi/efi.htm>.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	EXTRA_CFLAGS="%{rpmcflags} -I/usr/include/efivar" \
	VPATH=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install src/efibootmgr/efibootmgr $RPM_BUILD_ROOT%{_sbindir}
install src/man/man8/efibootmgr.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README doc/{ChangeLog,TODO}
%attr(755,root,root) %{_sbindir}/efibootmgr
%{_mandir}/man8/efibootmgr.8*
